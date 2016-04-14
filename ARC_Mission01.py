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

def mission01(clock, fps):
    pygame.init()

    #Basic settings
    mission01 = True
    pygame.display.set_caption("Project ARC")
    screen = pygame.display.set_mode((WIN_W, WIN_H), pygame.SRCALPHA)

    #Group creation
    platform_group = pygame.sprite.Group()
    hero_group = pygame.sprite.Group()
    secguard_group = pygame.sprite.Group()
    motsen_group = pygame.sprite.Group()
    movelaser_group = pygame.sprite.Group()

    #Object creation
    hero = Hero(64, 64)
    hero_group.add(hero)

    #Load the level
    mission01_level = [
        "I     I       PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP"
        "I     I       P                                                   P"
        "I     I       P                                                   P"
        "I     PPPPPPPPP  PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP   P"
        "I     P                                                     P     P"
        "I     L         P                                           P     P"
        "I              PP                                           P     P"
        "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP"
    ]   #0123456789012345678901234567890123456789012345678901234567890123456
        #          1         2         3         4         5         6

    #Build level
    x = y = 0
    platforms = []
    for row in mission01_level:
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
                l = MotionSensor(x, y, 120, 120)
                motsen_group.add(l)
            if col == "I":
                i = InvisibleWall(x, y)
                platform_group.add(i)
            x += 32
        y += 32
        x = 0

    #Set Up Camera
    total_width_app = len(mission01_level[0]) * 32
    total_height_app = len(mission01_level) * 32
    camera = Camera(total_width_app, total_height_app)

    while mission01:
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
        #trig1.update(hero)
        #platform_group.update(trig1)
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

        pygame.display.flip()

if __name__ == "__main__":
    mission01(clock, fps)