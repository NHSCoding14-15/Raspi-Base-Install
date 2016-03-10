from mcpi.minecraft import Minecraft
from mcpi import block
import time
import math
import random
        
mc = Minecraft.create()
x = playerPos.x
y

playerPos = mc.player.getPos()
mc.setBlock(playerPos.x + 1, playerPos.y + 1, playerPos.z + 1, 46, 1)

