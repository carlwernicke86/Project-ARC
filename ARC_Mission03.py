__author__ = 'cardg_000'
import pygame, os, sys, math
from object_classes import *

TIMER = 0

#Time Variables are defined below
clock = pygame.time.Clock()            #The clock which can be used to set fps
beg_time = pygame.time.get_ticks()     #The time the game first begins
fps = 60

#Constants
WIN_W = 1600
WIN_H = 900

def mission03(clock, fps):
    pygame.init()

    #Basic settings
    mission03_loop = True
    pygame.display.set_caption("Project ARC")
    screen = pygame.display.set_mode((WIN_W, WIN_H), pygame.SRCALPHA)

    #Group creation
    platform_group = pygame.sprite.Group()
    hero_group = pygame.sprite.Group()
    secguard_group = pygame.sprite.Group()
    motsen_group = pygame.sprite.Group()
    movelaser_group = pygame.sprite.Group()

    #Object creation
    hero = Hero(64, 160)
    sec1 = SecGuard("right", 384, (38*32), 160) #Farthest right is 1152 [36] (end of flashlight)
    sec2 = SecGuard("left", 352, 2912, 160) #Farthest right is 1856 [58]
    '''
    trig1 = Trigger(288, 192)
    triggerdoor1 = TriggerDoor(320, 160) #Just triggerdoor1 is updated later, independent of the platform_group.
                                        # We can use this method for future objects that need collision but have different update arguments.
    trig2 = Trigger(1056, 192)
    triggerdoor2 = TriggerDoor(1088, 160)

    trig3 = Trigger(1632, 192)
    triggerdoor3 = TriggerDoor(1664,160)

    trig4 = Trigger(2304, 192)
    triggerdoor4 = TriggerDoor(2336, 160)

    trig5 = Trigger(92*32, 192)
    triggerdoor5 = TriggerDoor(106*32, 64)
    '''
    hero_group.add(hero)
    secguard_group.add(sec1)
    secguard_group.add(sec2)
    #platform_group.add(triggerdoor1, triggerdoor2, triggerdoor3, triggerdoor4, triggerdoor5)

    #Load the level
    mission03_level = [
        "IPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP",#0
        "I                                                               P",
        "I                                                               P",
        "I                                                               P",
        "I                                                               P",
        "IPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP",#5
        "I                                                               P",
        "I                                                               P",
        "I                                                               P",
        "I                                                               P",
        "IPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP      P",#10
        "P                               P                               P",
        "P                               P                               P",
        "P                               P            PPPPPPPPPPPPPPPPPPPP",
        "P                               P                               P",
        "P                               P                               P",#15
        "P                               P               PPPPPPPPPPPPPPPPP",
        "P                               P                               P",
        "P                               P                               P",
        "P                               P              PPPPPPPP         P",
        "P                               P                            PPPP",#20
        "P                               P      PPPPPPPP                 P",
        "P                               P                               P",
        "P                               PPPPPPPPPPPPPPPPPPPPPPPPPPPPPP  P",
        "P                               P                               P",
        "P                               P                               P",#25
        "P                               PPPPPPPPPPP            PPPPPPPPPP",
        "P                               P                               P",
        "P                               P                               P",
        "P                               P                               P",
        "P                               P                               P",#30
        "P                               P                               P",
        "P                               P                               P",
        "P                               P                               P",
        "P                               P                               P",
        "P                               P                               P",#35
        "P                               P                               P",
        "P                               P                               P",
        "P                               P                               P",
        "P                               P                               P",
        "P                               P                               P",#40
        "P                               P                               P",
        "P                               P                               P",
        "P                               P                               P",
        "P                               P                               P",
        "P                               P                               P",#45
        "P                               P                               P",
        "P                               P                               P",
        "P                               P                               P",
        "P                               P                               P",
        "P                               P                               P",#50
        "P                               P                               P",
        "P                               P                               P",
        "P                               P                               P",
        "P                               P                               P",
        "P                               P                               P",#55
        "P                               P                               P",
        "P                               P                               P",
        "P                               P                               P",
        "P                               P                               P",
        "P                               P                               P",#60
        "P                               P                               P",
        "P                               P                               P",
        "P                               P                               P",
        "P                               P                               P",
        "P                               P                               P",#65
        "P                               P                               P",
        "P                               P                               P",
        "P                               P                               P",
        "P                               P                               P",
        "P                               P                               P",#70
        "I                               P                               P",
        "P                               P                               P",
        "I                               P                               P",
        "I                               P                               P",
        "I                               P                               P",#75
        "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP"
    ]   #01234567890123456789012345678901234567890123456789012345678901234
        #          1         2         3         4         5         6

    #Build level
    x = y = 0
    platforms = []
    for row in mission02_level:
        for col in row:
            if col == "P":
                p = Platform([61, 61, 61], x, y)
                platform_group.add(p)
            if col == "D":
                d = WinDocs(x, y)
                platform_group.add(d)
            if col == "O":
                o = TriggerDoor(x, y)
                platform_group.add(o)
            if col == "L":
                L = MotionSensor(x, y, 45, 60, False)
                motsen_group.add(L)
            if col == "l":
                l = MotionSensor(x,y,45,60, True)
                motsen_group.add(l)
            if col == "d":
                l2 = MotionSensor(x, y, 20, 60, False)
                motsen_group.add(l2)
            if col == "F":
                D = MotionSensor(x, y, 20, 60, True)
                motsen_group.add(D)
            if col == "I":
                i = InvisibleWall(x, y)
                platform_group.add(i)
            x += 32
        y += 32
        x = 0

    #Set Up Camera
    total_width_app = len(mission02_level[0]) * 32
    total_height_app = len(mission02_level) * 32
    camera = Camera(total_width_app, total_height_app)

    while mission03_loop:
        clock.tick(fps)
        screen.fill((255, 255, 255))

        # Quitting the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # Update
        hero_group.update(platform_group)
        camera.update(hero.rect)
        secguard_group.update(hero, secguard_group)
        '''
        trig1.update(hero)
        triggerdoor1.update(trig1)
        trig2.update(hero)
        triggerdoor2.update(trig2)
        trig3.update(hero)
        triggerdoor3.update(trig3)
        trig4.update(hero)
        triggerdoor4.update(trig4)
        trig5.update(hero)
        triggerdoor5.update(trig5)
        '''

        #platform_group.update()
        motsen_group.update(hero)
        movelaser_group.update(hero)

        #Draw something
        for p in platform_group:
            screen.blit(p.image, camera.apply(p))
        for h in hero_group:
            screen.blit(h.image, camera.apply(h))
        for sg in secguard_group:
            screen.blit(sg.image, camera.apply(sg))
        for ms in motsen_group:
            if ms.active == True:
                screen.blit(ms.image, camera.apply(ms))
        screen.blit(trig1.image, camera.apply(trig1))
        screen.blit(trig2.image, camera.apply(trig2))
        screen.blit(trig3.image, camera.apply(trig3))
        screen.blit(trig4.image, camera.apply(trig4))
        screen.blit(trig5.image, camera.apply(trig5))

        pygame.display.flip()

if __name__ == "__main__":
    mission02(clock, fps)