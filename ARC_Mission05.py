__author__ = 'cardg_000'
import pygame, os, sys, math
from object_classes import *
from MazePuzzle4 import *

TIMER = 0

#Time Variables are defined below
clock = pygame.time.Clock()            #The clock which can be used to set fps
beg_time = pygame.time.get_ticks()     #The time the game first begins
fps = 60

#Constants
WIN_W = 1600
WIN_H = 900

def mission05(intro_flag = False):
    pygame.init()

    #Basic settings
    mission05_loop = True
    pygame.display.set_caption("Project ARC")
    screen = pygame.display.set_mode((WIN_W, WIN_H), pygame.SRCALPHA)

    #Group creation
    platform_group = pygame.sprite.Group()
    hero_group = pygame.sprite.Group()
    secguard_group = pygame.sprite.Group()
    motsen_group = pygame.sprite.Group()
    movelaser_group = pygame.sprite.Group()
    puzzle_group = pygame.sprite.Group()

    #Object creation
    hero = Hero(3*32, 71*32)


    hero_group.add(hero)



    trig1 = Trigger(1*32, 55*32)
    triggerdoor1 = TriggerDoor(51*32, 41*32)

    trig2 = Trigger(139*32, 39*32)
    triggerdoor2 = TriggerDoor(140*32, 41*32)

    trig3 = Trigger(103*32, 32*32)
    triggerdoor3 = TriggerDoor(133*32,26*32)

    trig4 = Trigger(134*32,27*32)
    triggerdoor4 = TriggerDoor(128*32,31*32)



    '''

    trig3 = Trigger(60*32,18*32)
    triggerdoor3 = TriggerDoor(59*32, 30*32)

    trig5 = Trigger(28*32, 21*32)
    triggerdoor5 = TriggerDoor(20*32, 30*32)
    '''

    puzzletrigger = PuzzleDoorTrigger(103*32, 21*32)
    puzzledoor = PuzzleDoor(102*32, 21*32)
    puzzle_group.add(puzzletrigger)

    sec1 = SecGuard("left", 15*32, 43*32, 71*32)
    sec2 = SecGuard("left", 6*32, 147*32, 41*32)
    sec3 = SecGuard("right", 15*32, 106*32, 31*32)

    plat1 = HMovPlat(12*32, 65*32, 3*32, "right", 32*4, 3)
    plat2 = HMovPlat(40*32, 64*32, 3*32, "left", 32*4, 3)
    plat3 = HMovPlat(32*32, 58*32, 3*32, "right", 32*4, 3)
    plat4 = HMovPlat(3*32, 57*32, 2*32, "right", 32*3, 4)
    plat5 = HMovPlat(14*32, 54*32, 2*32, "left", 32*3, 4)
    plat6 = HMovPlat(31*32, 46*32, 1*32, "right", 32*3, 3)
    plat7 = HMovPlat(106*32, 25*32, 4*32, "right", 2*32, 5)
    plat8 = HMovPlat(147*32, 30*32, 4*32, "left", 2*32, 5)
    plat9 = HMovPlat(56*32,20*32, 4*32,"right",10*32,4)
    plat10 = HMovPlat(93*32, 17*32, 4*32, "left", 10*32, 4)
    plat11 = HMovPlat(58*32, 14*32, 2*32, "right", 8*32, 5)
    plat12 = HMovPlat(95*32, 11*32, 2*32, "left", 8*32, 5)
    plat13 = HMovPlat(60*32, 8*32, 1*32, "right", 6*32, 6)

    platform_group.add(plat1, plat2, plat3, plat4, plat5, plat6, plat7, plat8, plat9, plat10, plat11, plat12, plat13, triggerdoor1, triggerdoor2, triggerdoor3, triggerdoor4, puzzledoor)
    secguard_group.add(sec1, sec2, sec3)

    mission05_level = [
        "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP", #0
        "P                                                  P                                                  P                                                  P",
        "P                                                  P                                                  P                                                  P",
        "P                                                  PD                                                DP                                                  P",
        "P                                                  PPPPPPPPPPPPPPPPPPPPP          PPPPPPPPPPPPPPPPPPPPP                                                  P",
        "P                                                  P                    P        P                    P                                                  P", #5
        "P                                                  P                                                  P                                                  P",
        "P                                                  P                                                  P                                                  P",
        "P                                                  P                                                  P                                                  P",
        "P                                                  P                                                  P                                                  P",
        "P                                                  P                                                  P                                                  P", #10
        "P                                                  P                                                  P                                                  P",
        "P                                                  P                                                  P                                                  P",
        "P                                                  P                                                  P                                                  P",
        "P                                                  P                                                  P                                                  P",
        "P                                                  P                                                  P                                                  P", #15
        "P                                                  P                                                  P                                                  P",
        "P                                                  P                                                  P                                                  P",
        "P                                                  P                                                  P                                                  P",
        "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP                                                  PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP",
        "P                                                  P                                                  P                              P                   P", #20
        "P                                                  d                                                                                 P                   P",
        "P                                                                                                                                    P                   P",
        "P                                                  PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP                         P                   P",
        "P                                                  P                                                  P                              P                   P",
        "P                                                  P                                                  P                              P                   P", #25
        "P                                                  P                                                  P                                                  P",
        "P                                                  P                                                  P                                                  P",
        "P                                                  P                                                  P                   PPPPPPPPPPPPP                  P",
        "P                                                  PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP                         P                        P",
        "P                                                  P                                                  P                         P                        P", #30
        "P                                                  d                                                  d                                                  P",
        "P                                                                                                                                                  M     P",
        "P                                                  PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP    P",
        "P                                                  P                                                  P~                        P           P            P",
        "P                                                  P                                                  P    q r q r q r q r q r q            P            P", #35
        "P                                                  P                                                  P                                     P           PP",
        "P                                                  P                                                  P   PPPPPPPPPPPPPPPPPPPPPPP           PPPPPPPPPP   P",
        "P                                                  P                                                  P    c  e  c  e  c  e     P           Px          yP",
        "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP                         P           P            P",
        "PPP                                                P                                                  PPPPPPPPPPPPPPPPPPPPPPP   Pj         PP      PPPPPPP", #40
        "PPPP                                                                                                    a    b    a    b   a    P                        P",
        "PPPPP                PPPPPPPPPPPPPPPPPPPPPPPPPPP                                                                                P                        P",
        "PPPPPPPPPPPPPPPP    P                           PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP",
        "P               P                                  P                                                  P                                                  P",
        "P                P                                 P                                                  P                                                  P", #45
        "P                 PPPPPPPPPPPPM           PPP      P                                                  P                                                  P",
        "P                 x L      L y                     P                                                  P                                                  P",
        "P                                               P  P                                                  P                                                  P",
        "P                 x L      L y                     PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP                                                  P",
        "P                                                 PP                                                  P                                                  P", #50
        "P                 x L      L y                     d                                                  d                                                  P",
        "P                                                                                                                                                        P",
        "P                 PPPPPPPPPPPP     P      P     PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP                                                  P",
        "P             M   x L      L y                     P                                                  P                                                  P",
        "P                                                  P                                                  P                                                  P", #55
        "PP                x L      L y                     P                                                  P                                                  P",
        "P   M                                              P                                                  P                                                  P",
        "Pk                PPPPPPPPPPPP                     P                                                  P                                                  P",
        "P                               M                  PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP                                                  P",
        "P                                                 PP                                                  P                                                  P", #60
        "P                                                  d                                                  d                                                  P",
        "P                                                                                                                                                        P",
        "P                                               PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP                                                  P",
        "P                                           M      P                                                  P                                                  P",
        "P        PPPM                                      P                                                  P                                                  P", #65
        "Pm        L                                        P                                                  P                                                  P",
        "P                                                  P                                                  P                                                  P",
        "PPPPPPP   L                P                       P                                                  P                                                  P",
        "P                          P                       PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP                                                  P",
        "P       PPPPP              PP                      P                                                  P                                                  P", #70
        "P           l              P                       d                                                  d                                                  P",
        "P                          P                                                                                                                             P",
        "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP", #73

        ]
    #Load the level
        #0         1         2         3         4         5         6         7         8         9         10       11        12        13        14        15
        #0123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123
     #Build level
    x = y = 0
    platforms = []
    for row in mission05_level:
        for col in row:
            if col == "D":
                d = WinDocs(x,y)
                platform_group.add(d)
            if col == "d":
                DummyDoor = TriggerDoor(x,y)
                platform_group.add(DummyDoor)
            if col == "L":
                l = MotionSensor(x + 12,y, 60, 60, False)
                motsen_group.add(l)
            if col == "l":
                l = MotionSensor(x+12, y, 99999999, 0, False)
                motsen_group.add(l)
            if col == "a":
                l = MotionSensor(x+12, y, 60, 60, False)
                motsen_group.add(l)
            if col == "b":
                l = MotionSensor(x+12,y, 60,60, True)
                motsen_group.add(l)
            if col == "c":
                l = MotionSensor(x+12,y, 45,45, False)
                motsen_group.add(l)
            if col == "e":
                l = MotionSensor(x+12, y, 45,45, True)
                motsen_group.add(l)
            if col == "q":
                l = MotionSensor(x+12,y, 30,30, False)
                motsen_group.add(l)
            if col == "r":
                l = MotionSensor(x+12, y, 30,30, True)
                motsen_group.add(l)
            if col == "j":
                l = HotMotSen(x,y+12, 30,30,False, 10*32)
                motsen_group.add(l)
            if col == "~":
                l = HotMotSen(x,y+12,999999,0, False,25*32)
                motsen_group.add(l)
            if col == "k":
                l = HotMotSen(x,y,0, 60, False, 17*32)
                motsen_group.add(l)
            if col == "m":
                l = MovingLaser(x+12,y, "right", 5*32)
                movelaser_group.add(l)
            if col == "x":
                l = MovingLaser(x+12,y, "right", 11*32)
                movelaser_group.add(l)
            if col == "y":
                l = MovingLaser(x+12, y, "left", 11*32)
                movelaser_group.add(l)
            if col == "P":
                p = Platform("Sprites/BlackBlock.png",x,y)
                platform_group.add(p)
            x += 32
        y += 32
        x = 0

    #Set Up Camera
    total_width_app = len(mission05_level[0]) * 32
    total_height_app = len(mission05_level) * 32
    camera = Camera(total_width_app, total_height_app)


    while mission05_loop:
        clock.tick(fps)
        screen.fill((100, 100,100))

        # Quitting the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # Update

        movelaser_group.update(hero, mission05)
        hero_group.update(platform_group, mission05)
        camera.update(hero.rect)
        motsen_group.update(hero, mission05)
        secguard_group.update(hero, secguard_group, mission05)



        trig1.update(hero)
        triggerdoor1.update(trig1)

        trig2.update(hero)
        triggerdoor2.update(trig2)

        trig3.update(hero)
        triggerdoor3.update(trig3)

        trig4.update(hero)
        triggerdoor4.update(trig4)

        '''

        trig5.update(hero)
        triggerdoor5.update(trig5)

        '''

        puzzletrigger.update(hero, MazePuzzle4, mission05)
        puzzledoor.update(puzzletrigger)

        plat1.update(hero)
        plat2.update(hero)
        plat3.update(hero)
        plat4.update(hero)
        plat5.update(hero)
        plat6.update(hero)
        plat7.update(hero)
        plat8.update(hero)
        plat9.update(hero)
        plat10.update(hero)
        plat11.update(hero)
        plat12.update(hero)
        plat13.update(hero)

        puzzletrigger.update(hero, MazePuzzle4, mission05)
        puzzledoor.update(puzzletrigger)

        if hero.dead == True:
            break

        #Draw something
        for p in platform_group:
            screen.blit(p.image, camera.apply(p))
        for z in puzzle_group:
            screen.blit(z.image, camera.apply(z))
        for h in hero_group:
            screen.blit(h.image, camera.apply(h))
        for sg in secguard_group:
            screen.blit(sg.image, camera.apply(sg))
        for ms in motsen_group:
            if ms.active == True:
                screen.blit(ms.image, camera.apply(ms))
        for mvs in movelaser_group:
            screen.blit(mvs.image, camera.apply(mvs))



        screen.blit(trig1.image, camera.apply(trig1))
        screen.blit(trig2.image, camera.apply(trig2))
        screen.blit(trig3.image, camera.apply(trig3))
        screen.blit(trig4.image, camera.apply(trig4))
        '''
        screen.blit(trig5.image, camera.apply(trig5))
        '''


        pygame.display.flip()



if __name__ == "__main__":
    mission05()
