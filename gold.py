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
    # Places the diamond block within 50 blocks of the player in X and Z directions but only 5 blocks in the y direction

    mc.setBlock(randomBlockPos.x, randomBlockPos.y, randomBlockPos.z, block.GOLD_BLOCK)
    mc.postToChat("The diamond has been hidden - find it!")
    #sets the block in its position and displays the task for the player

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
# Dectects whether or not the player has found the block yet
            else:
                if distanceFromBlock < lastDistanceFromBlock:
                    mc.postToChat("Warmer, " + str(int(distanceFromBlock)) + " blocks away")

                if distanceFromBlock > lastDistanceFromBlock:
                    mc.postToChat("Colder, " + str(int(distanceFromBlock)) + " blocks away")
    #Tells the player whether or not they are getting closer or farther from the diamond block

            lastDistanceFromBlock = distanceFromBlock

        time.sleep(1)

    timeTaken = time.time() - timeStarted
    mc.postToChat("Well done - it took you " + str(int(timeTaken)) + " seconds to find the diamond")
    #Final text when the player finds the diamond, with the amount of time displayed it took to find the block

    

            
                    
    
