__author__ = 'cardg_000'
import pygame, os, sys, math
from object_classes import *
from MazePuzzle1 import *

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

def mission03(intro_flag = False):
    pygame.init()

    event_list[0] = 0
    #Basic settings
    mission03_loop = True
    pygame.display.set_caption("Project ARC")
    screen = pygame.display.set_mode((WIN_W, WIN_H), pygame.SRCALPHA)

    level3 = Regular_Text(100, BLACK, (screen.get_rect().centerx, screen.get_rect().centery/2), "Level 3")
    press_continue = Regular_Text(50, (200, 200, 200), (screen.get_rect().centerx, screen.get_rect().centery), "- Press Any Button to Proceed -")
    
    #Group creation
    platform_group = pygame.sprite.Group()
    hero_group = pygame.sprite.Group()
    secguard_group = pygame.sprite.Group()
    motsen_group = pygame.sprite.Group()
    movelaser_group = pygame.sprite.Group()
    event_group = pygame.sprite.Group()
    puzzle_group = pygame.sprite.Group()

    #BUT SPOOKY THINGS HAPPEN IN THE MIDDLE OF NOWHERE
    onElevator = True

    #Object creation
    hero = Hero(64, 2144)
    sec1 = SecGuard("right", 416, (67*32), 21*32) #Farthest right is 1152 [36] (end of flashlight)
    sec2 = SecGuard("left", 7*32, 84*32, 32*32) #Farthest right is 1856 [58]
    sec3 = SecGuard("left", 6*32, 63*32, 48*32)

    invisTrig = Trigger(256, 128)

    trig1 = Trigger(82*32, 15*32)
    triggerdoor1 = TriggerDoor(81*32, 21*32)

    trig2 = Trigger(73*32, 22*32)
    triggerdoor2 = TriggerDoor(80*32 ,14*32)

    trig3 = Trigger(68*32, 49*32)
    triggerdoor3 = TriggerDoor(57*32, 48*32)

    trig4 = Trigger(60*32, 49*32)
    triggerdoor4 = TriggerDoor(75*32, 42*32)

    puzzletrigger = PuzzleDoorTrigger(83*32, 58*32) #Original x value at 896, y 288
    puzzle_group.add(puzzletrigger)
    puzzledoor = PuzzleDoor(84*32, 58*32)
    platform_group.add(puzzledoor)


    hero_group.add(hero)
    secguard_group.add(sec1,sec2,sec3)
    #platform_group.add(triggerdoor1, triggerdoor2, triggerdoor3, triggerdoor4, triggerdoor5)

    #CREATE THE ELEVATOR BABY CHOO CHOO
    edoor = ElevatorDoor(160, 2144)
    eroof = ElevatorRoof(64, 2080)
    efloor = ElevatorFloor(64, 2208)
    ewall = ElevatorWall(32, 2080)
    edoorframe = ElevatorDoorFrame(160, 2112)

    platform_group.add(eroof, efloor, ewall, edoorframe, edoor, triggerdoor1, triggerdoor2, triggerdoor3, triggerdoor4, puzzledoor)

    #Load the level
    mission03_level = [
        "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP",#0
        "P     P                                                                              P",
        "P     P                                                                              P",
        "P     l                                                                              P",
        "P                          1                                                         P",
        "P     PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP   P",#5
        "P     P                                              P                              bP",
        "P     P                                              P                               P",
        "P     l                                              P      a                        P",
        "P                                                    P                               P",
        "P     PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP      PPPPPPPPPPPPPPPPPPPPPPPPPP",#10
        "P     P                                              P                               P",
        "P     P                                              P                               P",
        "P     l                                              Pe           PPPPPPPPPPPPPPPPPPPP",
        "P                                                    P                               P",
        "P     PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP                               P",#15
        "P     P                                              P                PPPPPPPPPPPPPPPP",
        "P     P                                              P      PPPP                     P",
        "P     l                                              P                               P",
        "P                                                    P             PPPP              P",
        "P     PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP                     PPPPPPPPPPP",#20
        "P     P                                              P      PPPP                     P",
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
        "P     P                                              P          a                    P",
        "P     l                                              P                               P",
        "P                                                    Pw         PPPPPPPPPPPPPPPPPPPPPP",
        "P     PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP                               P",#35
        "P     P                                              P                    b          P",
        "P     P                                              P                               P",
        "P     l                                              PPPPPPPPPPPPPPPPPPPPPPw         P",
        "P                                                    P                               P",
        "P     PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP                               P",#40
        "P     P                                              P   PPPPPPPPPPPPPPPPPPPPPPPPPPPPP",
        "P     P                                              P                               P",
        "P     l                                              P                               P",
        "P                                                    P                     PP        P",
        "P     PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP                    PPP        P",#45
        "P     P                                              P                      P        P",
        "P     P                                              PP  PPPPPPPPPPPPPPPP   P        P",
        "P     l                                              P                      P        P",
        "P                                                    P                      P        P",
        "P     PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPq       P",#50
        "P     P                                              P                               P",
        "P     P                                              P                               P",
        "P     l                                              P       a                       P",
        "P                                                    P                               P",
        "P     PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPq       PPPPPPPPPPPPPPPPPPPPPPPP",#55
        "P     P                                              P                               P",
        "P     P                                              P                               P",
        "P     l                                              P                        b     ZD",
        "P                                                    P                               P",
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
                p = Platform("Sprites/BlackBlock.png", x, y)
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
                    q = HotMotSen(x, y, 30, 120, False, 8*32)
                    motsen_group.add(q)
                if col == "w":
                    w = HotMotSen(x,y,60,90,False, 320)
                    motsen_group.add(w)
                if col == "e":
                    e = HotMotSen(x,y,90,60,False, 12*32)
                    motsen_group.add(e)
            x += 32
        y += 32
        x = 0

    #Set Up Camera
    total_width_app = len(mission03_level[0]) * 32
    total_height_app = len(mission03_level) * 32
    camera = Camera(total_width_app, total_height_app)
    
    if intro_flag == False:

        pre_level_loop_in = True
        while pre_level_loop_in:
            clock.tick(60)
            for event in pygame.event.get():                    #Fading in Loop
                if event.type == pygame.QUIT: sys.exit()
                if event.type == pygame.KEYDOWN:
                    pre_level_loop_in = False

            screen.fill(BLACK)
            level3.fade_in(screen)
            if level3.red > 252:
                cur_time = pygame.time.get_ticks()
                press_continue.blink(screen, cur_time, beg_time)
                
            pygame.display.update()

        for i in range(150):
            clock.tick(60)                                      #Fading out Loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()

            screen.fill(BLACK)
            level3.fade_out(screen)

            pygame.display.update()

    fade_in_screen = pygame.Surface((WIN_W, WIN_H))

    fade_in_screen.set_alpha(255)
    if intro_flag == True:
        fade_in_screen.set_alpha(0)

    while mission03_loop:
        clock.tick(fps)
        screen.fill((255, 255, 255))

        # Quitting the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # Update
        if not efloor.climbing:
            hero_group.update(platform_group, mission03check)
        camera.update(hero.rect)
        secguard_group.update(hero, secguard_group, mission03check)
        if hero.rect.x >= eroof.rect.x - 32 and hero.rect.x <= eroof.rect.x + 128:
            onElevator = True
        else:
            onElevator = False
        if onElevator == True:
            hero.rect.y = efloor.rect.y - 64

        invisTrig.update(hero)
        for e in event_group:
            eroof.update(e)
            efloor.update(e)
            ewall.update(e)
            edoorframe.update(e)
            edoor.update(invisTrig,e)
        movelaser_group.update(hero, mission03check)
        event_group.update(hero, event_list)
        trig1.update(hero)
        triggerdoor1.update(trig1)
        trig2.update(hero)
        triggerdoor2.update(trig2)
        trig3.update(hero)
        triggerdoor3.update(trig3)
        trig4.update(hero)
        triggerdoor4.update(trig4)
        puzzletrigger.update(hero, MazePuzzle1, mission03check)
        puzzledoor.update(puzzletrigger)

        if event_list[0] == 1:
            motsen_group.update(hero, mission03check)

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

        screen.blit(fade_in_screen, (0, 0))
        if fade_in_screen.get_alpha() != 0:
            fade_in_screen.set_alpha(fade_in_screen.get_alpha() - 3)
        pygame.display.flip()

def mission03check(intro_flag = True):
    pygame.init()

    event_list[0] = 1
    #Basic settings
    mission03check_loop = True
    pygame.display.set_caption("Project ARC")
    screen = pygame.display.set_mode((WIN_W, WIN_H), pygame.SRCALPHA)

    #Group creation
    platform_group = pygame.sprite.Group()
    hero_group = pygame.sprite.Group()
    secguard_group = pygame.sprite.Group()
    motsen_group = pygame.sprite.Group()
    movelaser_group = pygame.sprite.Group()
    event_group = pygame.sprite.Group()
    puzzle_group = pygame.sprite.Group()

    #BUT SPOOKY THINGS HAPPEN IN THE MIDDLE OF NOWHERE
    onElevator = True

    #Object creation
    hero = Hero(1280, 96)
    sec1 = SecGuard("right", 416, (67*32), 21*32) #Farthest right is 1152 [36] (end of flashlight)
    sec2 = SecGuard("left", 7*32, 84*32, 32*32) #Farthest right is 1856 [58]
    sec3 = SecGuard("left", 6*32, 63*32, 48*32)

    invisTrig = Trigger(256, 128)

    trig1 = Trigger(82*32, 15*32)
    triggerdoor1 = TriggerDoor(81*32, 21*32)

    trig2 = Trigger(73*32, 22*32)
    triggerdoor2 = TriggerDoor(80*32 ,14*32)

    trig3 = Trigger(68*32, 49*32)
    triggerdoor3 = TriggerDoor(57*32, 48*32)

    trig4 = Trigger(60*32, 49*32)
    triggerdoor4 = TriggerDoor(75*32, 42*32)

    puzzletrigger = PuzzleDoorTrigger(83*32, 58*32) #Original x value at 896, y 288
    puzzle_group.add(puzzletrigger)
    puzzledoor = PuzzleDoor(84*32, 58*32)
    platform_group.add(puzzledoor)


    hero_group.add(hero)
    secguard_group.add(sec1,sec2,sec3)
    #platform_group.add(triggerdoor1, triggerdoor2, triggerdoor3, triggerdoor4, triggerdoor5)

    platform_group.add(triggerdoor1, triggerdoor2, triggerdoor3, triggerdoor4, puzzledoor)

    #Load the level
    mission03check_level = [
        "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP",#0
        "P     P                                                                              P",
        "P     P                                                                              P",
        "P     l                                                                              P",
        "P                          1                                                         P",
        "P     PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP   P",#5
        "P     P                                              P                              bP",
        "P     P                                              P                               P",
        "P     l                                              P      a                        P",
        "P                                                    P                               P",
        "P     PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP      PPPPPPPPPPPPPPPPPPPPPPPPPP",#10
        "P     P                                              P                               P",
        "P     P                                              P                               P",
        "P     l                                              Pe           PPPPPPPPPPPPPPPPPPPP",
        "P                                                    P                               P",
        "P     PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP                               P",#15
        "P     P                                              P                PPPPPPPPPPPPPPPP",
        "P     P                                              P      PPPP                     P",
        "P     l                                              P                               P",
        "P                                                    P             PPPP              P",
        "P     PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP                     PPPPPPPPPPP",#20
        "P     P                                              P      PPPP                     P",
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
        "P     P                                              P          a                    P",
        "P     l                                              P                               P",
        "P                                                    Pw         PPPPPPPPPPPPPPPPPPPPPP",
        "P     PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP                               P",#35
        "P     P                                              P                    b          P",
        "P     P                                              P                               P",
        "P     l                                              PPPPPPPPPPPPPPPPPPPPPPw         P",
        "P                                                    P                               P",
        "P     PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP                               P",#40
        "P     P                                              P   PPPPPPPPPPPPPPPPPPPPPPPPPPPPP",
        "P     P                                              P                               P",
        "P     l                                              P                               P",
        "P                                                    P                     PP        P",
        "P     PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP                    PPP        P",#45
        "P     P                                              P                      P        P",
        "P     P                                              PP  PPPPPPPPPPPPPPPP   P        P",
        "P     l                                              P                      P        P",
        "P                                                    P                      P        P",
        "P     PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPq       P",#50
        "P     P                                              P                               P",
        "P     P                                              P                               P",
        "P     l                                              P       a                       P",
        "P                                                    P                               P",
        "P     PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPq       PPPPPPPPPPPPPPPPPPPPPPPP",#55
        "P     P                                              P                               P",
        "P     P                                              P                               P",
        "P     l                                              P                        b     ZD",
        "P                                                    P                               P",
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
        "P     l                                              P                          a     P",
        "P                                                    P                               P",
        "PIIIIIPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP"
    ]   #012345678901234567890123456789012345678901234567890123456789012345678901234567890123456
        #          1         2         3         4         5         6         7         8

    #Build level
    x = y = 0
    platforms = []
    for row in mission03check_level:
        for col in row:
            if col == "P":
                p = Platform("Sprites/BlackBlock.png", x, y)
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
                    q = HotMotSen(x, y, 30, 120, False, 8*32)
                    motsen_group.add(q)
                if col == "w":
                    w = HotMotSen(x,y,60,90,False, 320)
                    motsen_group.add(w)
                if col == "e":
                    e = HotMotSen(x,y,90,60,False, 12*32)
                    motsen_group.add(e)
            x += 32
        y += 32
        x = 0

    #Set Up Camera
    total_width_app = len(mission03check_level[0]) * 32
    total_height_app = len(mission03check_level) * 32
    camera = Camera(total_width_app, total_height_app)

    while mission03check_loop:
        clock.tick(fps)
        screen.fill((255, 255, 255))

        # Quitting the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # Update
        hero_group.update(platform_group, mission03check)
        camera.update(hero.rect)
        secguard_group.update(hero, secguard_group, mission03check)
        movelaser_group.update(hero, mission03check)
        event_group.update(hero, event_list)
        trig1.update(hero)
        triggerdoor1.update(trig1)
        trig2.update(hero)
        triggerdoor2.update(trig2)
        trig3.update(hero)
        triggerdoor3.update(trig3)
        trig4.update(hero)
        triggerdoor4.update(trig4)
        puzzletrigger.update(hero, MazePuzzle1, mission03check)
        puzzledoor.update(puzzletrigger)

        if event_list[0] == 1:
            motsen_group.update(hero, mission03check)

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


        pygame.display.flip()

if __name__ == "__main__":
    mission03()
