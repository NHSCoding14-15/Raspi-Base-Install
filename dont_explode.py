#! /usr/bin/python

import subprocess
import random
from socket import error
from mcpi.minecraft import Minecraft
from mcpi.block import TNT, LAVA
from mcpi.vec3 import Vec3
from pygame.time import Clock


NUM_TNT = 1


def wait_for_close(mc):
    clock = Clock()
    while not mc.poll():
        clock.tick(30)


def main():
    mc = subprocess.Popen("minecraft-pi")
    timer = 0
    clock = Clock()
    clock.tick(30)
    ready = False
    while not ready:
        try:
            game = Minecraft.create()
            ready = True
        except error:
            stopped = mc.poll()
            if stopped:
                return
            clock.tick(30)
    startpos = game.player.getTilePos()
    tnt_blocks = [[random.randint(startpos.x-50, startpos.x+50),
                   random.randint(startpos.y-50, startpos.y+50),
                   random.randint(startpos.z-50, startpos.z+50)]
                  for z in range(NUM_TNT)]
    for block in tnt_blocks:
        game.setBlock(block[0], block[1], block[2], TNT)
    game.postToChat("{} TNT blocks have been hidden"
                    " around the world.".format(NUM_TNT))
    game.postToChat("Destroy them!")
    game.postToChat("They will explode in {} minutes.".format(NUM_TNT))
    game.postToChat("Good luck")
    while timer < NUM_TNT*60:
        stopped = mc.poll()
        if stopped:
            return
        if timer % 60 == 0:
            game.postToChat("{} minutes remaining.".format(4-(timer/1800)))
        timer += 1
        current_pos = game.player.getTilePos()
        min_dist = 100000000
        blocks_left = False
        for block in tnt_blocks:
            if game.getBlock(*block) != TNT.id:
                print game.getBlock(*block)
                continue
            blocks_left = True
            dist_vec = Vec3(current_pos.x - block[0],
                            current_pos.y - block[1],
                            current_pos.z - block[2])
            dist = abs(dist_vec.x) + abs(dist_vec.y) + abs(dist_vec.z)
            if dist < min_dist:
                min_dist = dist
        if blocks_left:
            game.postToChat("Nearest block: {} blocks away.".format(
                min_dist))
        else:
            game.postToChat("You Win!")
            wait_for_close(mc)
            return
        clock.tick(1)
    game.postToChat("You have Failed!")
    game.postToChat("You have been cursed with Lava!")
    while not mc.poll():
        try:
            pos = game.player.getTilePos()
            game.setBlock(pos.x, pos.y, pos.z, LAVA)
        except mcpi.connection.RequestError:
            wait_for_close(mc)
            return
        clock.tick(30)
    

if __name__ == "__main__":
    main()
