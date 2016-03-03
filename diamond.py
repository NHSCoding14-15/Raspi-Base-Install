from mcpi.minecraft import Minecraft
from mcpi import block
import time
import math
import random
        
mc = Minecraft.create()
mc.postToChat("Hello World")

#def roundVec3(vec3):
#    return Minecraft.Vec3(int(vec3.x), int(vec3.y), int(vec3.z))

def distanceBetweenPoints(point1, point2):
    xd = point2.x - point1.x
    yd = point2.y - point1.y
    zd = point2.z - point1.z
    return math.sqrt((xd*xd) + (yd*yd) + (zd*zd))

if __name__ == "__main__":
    mc.postToChat("Hide and seek has begun")    
    
    time.sleep(2)
    
    playerPos = mc.player.getPos()

#    randomBlockPos = roundVec3(playerPos)
    randomBlockPos = playerPos
    randomBlockPos.x = random.uniform(randomBlockPos.x - 50, randomBlockPos.x + 50)
    randomBlockPos.y = random.uniform(randomBlockPos.y - 5, randomBlockPos.y)
    randomBlockPos.z = random.uniform(randomBlockPos.z - 50, randomBlockPos.z + 50)

    mc.setBlock(randomBlockPos.x, randomBlockPos.y, randomBlockPos.z, block.DIAMOND_BLOCK)
    mc.postToChat("The diamond has been hidden - find it!")

    seeking = True
    lastPlayerPos = playerPos
    lastDistanceFromBlock = distanceBetweenPoints(randomBlockPos, lastPlayerPos)
    timeStarted = time.time()
    while (seeking == True):
        playerPos = mc.player.getPos()
        if lastPlayerPos != playerPos:
            distanceFromBlock = distanceBetweenPoints(randomBlockPos, playerPos)
            if distanceFromBlock < 2:
                seeking = False

            else:
                if distanceFromBlock < lastDistanceFromBlock:
                    mc.postToChat("Warmer, " + str(int(distanceFromBlock)) + " blocks away")

                if distanceFromBlock > lastDistanceFromBlock:
                    mc.postToChat("Colder, " + str(int(distanceFromBlock)) + " blocks away")

            lastDistanceFromBlock = distanceFromBlock

        time.sleep(1)

    timeTaken = time.time() - timeStarted
    mc.postToChat("Well done - it took you " + str(int(timeTaken)) + " seconds to find the diamond")

    

            
                    
    
