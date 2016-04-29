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

#Events
event_list = [0]              #This will help trigger events; # of 0's dictate amount of events in level

def mission03():
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
    event_group = pygame.sprite.Group()

    #BUT SPOOKY THINGS HAPPEN IN THE MIDDLE OF NOWHERE
    onElevator = True

    #Object creation
    hero = Hero(64, 2144)
    sec1 = SecGuard("right", 416, (68*32),21*32) #Farthest right is 1152 [36] (end of flashlight)
    #sec2 = SecGuard("left", 352, 2912, 160) #Farthest right is 1856 [58]
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
    #secguard_group.add(sec2)
    #platform_group.add(triggerdoor1, triggerdoor2, triggerdoor3, triggerdoor4, triggerdoor5)

    #CREATE THE ELEVATOR BABY CHOO CHOO
    edoor = ElevatorDoor(160, 2144)
    eroof = ElevatorRoof(64, 2080)
    efloor = ElevatorFloor(64, 2208)
    ewall = ElevatorWall(32, 2080)
    edoorframe = ElevatorDoorFrame(160, 2112)

    platform_group.add(eroof)
    platform_group.add(efloor)
    platform_group.add(ewall)
    platform_group.add(edoorframe)
    platform_group.add(edoor)

    #Load the level
    mission03_level = [
        "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP",#0
        "P     P                                                                              P",
        "P     P                                                                              P",
        "P     l                                                                              P",
        "P              1                                                                     P",
        "P     PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP   P",#5
        "P     P                                              P                              bP",
        "P     P                                              P                               P",
        "P     l                                              P      a                        P",
        "P                                                    P                               P",
        "P     PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP      PPPPPPPPPPPPPPPPPPPPPPPPPP",#10
        "P     P                                              P                               P",
        "P     P                                              P                               P",
        "P     l                                              P            PPPPPPPPPPPPPPPPPPPP",
        "P                                                    P                               P",
        "P     PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP                               P",#15
        "P     P                                              P               PPPPPPPPPPPPPPPPP",
        "P     P                                              P                               P",
        "P     l                                              P                               P",
        "P                                                    P              PPPPPPPP         P",
        "P     PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP                            PPPP",#20
        "P     P                                              P      PPPPPPPP                 P",
        "P     P                                              P                               P",
        "P     l                                              PPPPPPPPPPPPPPPPPPPPPPPPPPPPPP  P",
        "P                                                    P                               P",
        "P     PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP                               P",#25
        "P     P                                              PPPPPPPPPPPPPq       PPPPPPPPPPPP",
        "P     P                                              P                           b   P",
        "P     l                                              PPPPPPPPPPPPw         PPPPPPPPPPP",
        "P                                                    P   a                           P",
        "P     PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPe           PPPPPPPPPP",#30
        "P     P                                              P                               P",
        "P     P                                              P                               P",
        "P     l                                              P                               P",
        "P                                                    P                   PPPPPPPPPPPPP",
        "P     PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP                               P",#35
        "P     P                                              P                               P",
        "P     P                                              P                               P",
        "P     l                                              PPPPPPPPPPPPPPPP                P",
        "P                                                    P                               P",
        "P     PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP                               P",#40
        "P     P                                              P                               P",
        "P     P                                              P                               P",
        "P     l                                              P                               P",
        "P                                                    P                               P",
        "P     PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP           PPPPPPPPPP",#45
        "P     P                                              P                               P",
        "P     P                                              P                               P",
        "P     l                                              P                               P",
        "P                                                    P                               P",
        "P     PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP      P",#50
        "P     P                                              P                               P",
        "P     P                                              P                               P",
        "P     l                                              P                               P",
        "P                                                    P                               P",
        "P     PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP       PPPPPPPPPPPPPPPPPPPPPPPPP",#55
        "P     P                                              P                               P",
        "P     P                                              P                               P",
        "P     l                                              P                               P",
        "P                                                    P                               D",
        "P     PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP",#60
        "P     P                                              P                               P",
        "P     P                                              P                               P",
        "P     l                                              P                               P",
        "P                                                    P                               P",
        "PE    PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP                               P",#65 #'E' simply denotes where the elevator roof is, does not spawn anything
        "P     P                                              P                               P",
        "P     P                                              P                               P",
        "P     l                                              P                               P",
        "P                                                    P                               P",
        "P     PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP                               P",#70
        "P     P                                              P                               P",
        "P     P                                              P                               P",
        "P     l                                              P                               P",
        "P                                                    P                               P",
        "P     PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP                               P",#75
        "P     P                                              P                               P",
        "P     P                                              P                               P",
        "P     l                                              P                               P",
        "P                                                    P                               P",
        "PIIIIIPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP"
    ]   #012345678901234567890123456789012345678901234567890123456789012345678901234567890123456
        #          1         2         3         4         5         6         7         8

    #Build level
    x = y = 0
    platforms = []
    for row in mission03_level:
        for col in row:
            if col == "P":
                p = Platform([61, 61, 61], x, y)
                platform_group.add(p)
            if col == "D":
                d = WinDocs(x, y)
                platform_group.add(d)
            if col == "L":
                L = MotionSensor(x, y, 45, 60, False)
                motsen_group.add(L)
            if col == "l":
                l = MotionSensor(x, y, 9999999999, 1, True)
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
            if col == "a":
                a = MovingLaser(x, y, "right", 768)
                movelaser_group.add(a)
            if col == "b":
                b = MovingLaser(x,y,"left",768)
                movelaser_group.add(b)
            if col == "1":
                e = Event_Mission03(x, y, 1, 4, 1)
                event_group.add(e)
            if col == "q" or col == "w" or col == "e":
                if col == "q":
                    q = HotMotSen(x, y, 1, 120, False, 8*32)
                    motsen_group.add(q)
                if col == "w":
                    w = HotMotSen(x,y,30,120,False, 320)
                    motsen_group.add(w)
                if col == "e":
                    e = HotMotSen(x,y,60,120,False, 12*32)
                    motsen_group.add(e)
            x += 32
        y += 32
        x = 0

    #Set Up Camera
    total_width_app = len(mission03_level[0]) * 32
    total_height_app = len(mission03_level) * 32
    camera = Camera(total_width_app, total_height_app)

    while mission03_loop:
        clock.tick(fps)
        screen.fill((255, 255, 255))

        # Quitting the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # Update
        if not efloor.climbing:
            hero_group.update(platform_group)
        camera.update(hero.rect)
        secguard_group.update(hero, secguard_group, mission03)
        if hero.rect.x >= eroof.rect.x - 32 and hero.rect.x <= eroof.rect.x + 128:
            onElevator = True
        else:
            onElevator = False
        if onElevator == True:
            hero.rect.y = efloor.rect.y - 64
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

        eroof.update()
        efloor.update(hero)
        ewall.update()
        edoorframe.update(hero)
        edoor.update(hero)
        movelaser_group.update(hero, mission03)
        event_group.update(hero, event_list)

        if event_list[0] == 1:
            motsen_group.update(hero, mission03)

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
        for mvs in movelaser_group:
            screen.blit(mvs.image, camera.apply(mvs))

        #screen.blit(trig1.image, camera.apply(trig1))
        #screen.blit(trig2.image, camera.apply(trig2))
        #screen.blit(trig3.image, camera.apply(trig3))
        #screen.blit(trig4.image, camera.apply(trig4))
        #screen.blit(trig5.image, camera.apply(trig5))

        if hero.dead == True:
            break

        pygame.display.flip()

if __name__ == "__main__":
    mission03()