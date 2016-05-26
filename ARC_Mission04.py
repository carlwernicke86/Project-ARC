__author__ = 'cardg_000'
import pygame, os, sys, math
from object_classes import *
from MazePuzzle3 import *

TIMER = 0

#Time Variables are defined below
clock = pygame.time.Clock()            #The clock which can be used to set fps
beg_time = pygame.time.get_ticks()     #The time the game first begins
fps = 60

#Constants
WIN_W = 1600
WIN_H = 900

def mission04(intro_flag = False):
    pygame.init()
    
    try:
        pygame.mixer.music.stop()
        pygame.mixer.music.load("Sounds/EventHorizonSong.ogg")
        pygame.mixer.music.play(-1)
    except pygame.error:
        pass

    #Basic settings
    mission04_loop = True
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
    hero = Hero(3*32, 7*32)

    hero_group.add(hero)

    trig1 = Trigger(28*32, 8*32)
    triggerdoor1 = TriggerDoor(121*32, 4*32)

    trig2 = Trigger(119*32, 24*32)
    triggerdoor2 = TriggerDoor(95*32, 30*32)

    trig3 = Trigger(60*32,18*32)
    triggerdoor3 = TriggerDoor(59*32, 30*32)

    trig5 = Trigger(28*32, 21*32)
    triggerdoor5 = TriggerDoor(20*32, 30*32)

    puzzletrigger2 = PuzzleDoorTrigger(15*32, 26*32)
    puzzledoor2 = PuzzleDoor(16*32, 26*32)
    puzzle_group.add(puzzletrigger2)

    sec1 = SecGuard("left", 8*32, 20*32, 30*32)
    sec2 = SecGuard("right", 8*32, 40*32, 30*32)
    sec3 = SecGuard("left", 8*32, 60*32, 30*32)
    sec4 = SecGuard("right", 8*32, 80*32, 30*32)
    sec5 = SecGuard("left", 8*32, 115*32, 30*32)

    plat1 = HMovPlat(43*32, 16*32, 2*32, "right", 32*4, 2)
    plat2 = HMovPlat(60*32, 14*32, 4*32, "right", 32*8, 2)
    plat3 = HMovPlat(91*32, 16*32, 4*32, "right", 32*8, 3)
    plat4 = HMovPlat(108*32, 10*32, 4*32, "left", 32*8, 2)
    plat5 = HMovPlat(72*32, 10*32, 4*32, "right", 32*8, 2)
    plat6 = HMovPlat(51*32, 8*32, 4*32, "right", 32*5, 2)
    plat7 = HMovPlat(120*32, 19*32, 4*32, "left", 32*8, 2)

    platform_group.add(triggerdoor1, triggerdoor2, triggerdoor3, triggerdoor5, plat1, plat2, plat3, plat4, plat5, plat6, plat7, puzzledoor2)
    secguard_group.add(sec1, sec2, sec3, sec4, sec5)

    #Load the level
    mission04_level = [
        "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP",  #0
        "P                          P                                                                                             P         P",
        "P                          P                                                                                             P         P",
        "P                          P                                                                                             P         P",
        "P                          P                                                                                                       P",
        "P                          P                                                                                                       P",
        "P                          P                     L                                          L    PPPPPPPPPPPPPPPPPPPPPPPPPPPP      P",
        "P                          Pi  l   L   l                                                                                    P      P",
        "P                          P                    PPPh                                       PPP                    l         P      P",
        "P                          PPPPPPPPPPPPPPPP     LlL                                                                         P      P",
        "P                                                                   PPPPh                                   H   PPPPP     L P      P",  #10
        "P    m                                          LlL                                                                         P      P",
        "PPPPP         o            L              L            m                                                            l   PPPPP      P",
        "PPPPPPPPPP     m                                                                                                            P      P",
        "PPPPPPPPPPPPPPP         o  L  v           L            PPPPPh                    v                                PPPPP     P      P",
        "PPPPPPPPPPPPPPPPPPPP                                                                        h                               P      P",
        "PPPPPPPPPPPPPPPPPPPPPPPPPk    PPPPPPa     Ps                                    PPPPPPPs                                    P      P",
        "P                   P                                      P                                   P                                   P",
        "P                   P                                      P                                  bP                                   P",
        "P                   P                                      PPPPP                               P                            PPPPPPPP",
        "P                   P      LlL   lLl                       Pt            PPPPP             PPPPPt                                 bP", #20
        "P                   P                                      P                                   P                                   P",
        "P                   P      PPP   PPP  LlL   lLl            P  PPPPPPP          PPPPPPPPPPPP   bPe           PPPPPPPPPPPPP          P",
        "PD                  P                                      P                                   P                        PPPP       P",
        "PPPPPPPPPPPPPPPPP   P                 PPP   PPPLlL         Pt           PP                     P                        P          P",
        "P               P  PP                                lLl   P                                   PPPPPPPPPPPPPPPPPPPPPPPPPP          P",
        "P                   P                          PPP         P                                  bP                        P       PPPP",
        "P                   P                                PPP   P          PPPPPPP                  P                        P          P",
        "P   PPPPPPPPPPPPPPPPP                                      Pt                    PPPPP         P                        P          P",
        "PP  P               P                                     PP                              PPPPPP                        PPPP       P",
        "P                                                                                                                                  P", #30
        "P                                                                                                                                  P",
        "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP",
        "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP"

        ]
        #0         1         2         3         4         5         6         7         8         9         10       11        12        13        14
        #012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789
     #Build level
    x = y = 0
    platforms = []
    for row in mission04_level:
        for col in row:
            if col == "D":
                d = WinDocs(x,y)
                platform_group.add(d)
            if col == "L":
                l = MotionSensor(x + 12,y, 60, 60, False)
                motsen_group.add(l)
            if col == "l":
                l = MotionSensor(x+12, y, 60, 60, True)
                motsen_group.add(l)
            if col == "k":
                l = HotMotSen(x,y,0, 60, False, 5*32)
                motsen_group.add(l)
            if col == "a":
                l = HotMotSen(x,y,0,60, False, 6*32)
                motsen_group.add(l)
            if col == "s":
                l = HotMotSen(x,y,0,60, False, 37*32)
                motsen_group.add(l)
            if col == "m":
                l = MovingLaser(x+12,y, "right", 4*32)
                movelaser_group.add(l)
            if col == "o":
                l = MovingLaser(x+12,y, "left",4*32)
                movelaser_group.add(l)
            if col == "e":
                l = HotMotSen(x,y,60, 60, False, 12*32)
                motsen_group.add(l)
            if col == "v":
                l = MovingLaser(x+12, y, "right", 5*32)
                movelaser_group.add(l)
            if col == "i":
                l = MovingLaser(x+12,y, "right", 15*32)
                movelaser_group.add(l)
            if col == "t":
                l = MovingLaser(x+12,y, "right", 35*12)
                movelaser_group.add(l)
            if col == "b":
                l = MovingLaser(x+12, y, "left", 35*12)
                movelaser_group.add(l)
            if col == "P":
                p = Platform("Sprites/BlackBlock.png",x,y)
                platform_group.add(p)
            x += 32
        y += 32
        x = 0

    trig4 = Trigger(94*32,19*32)
    triggerdoor4 = TriggerDoor(95*32, 32*32)

    platform_group.add(triggerdoor4)

    #Set Up Camera
    total_width_app = len(mission04_level[0]) * 32
    total_height_app = len(mission04_level) * 32
    camera = Camera(total_width_app, total_height_app)


    while mission04_loop:
        clock.tick(fps)
        screen.fill((100, 100,100))

        # Quitting the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # Update

        movelaser_group.update(hero, mission04)
        hero_group.update(platform_group, mission04)
        camera.update(hero.rect)
        motsen_group.update(hero, mission04)
        secguard_group.update(hero, secguard_group, mission04)



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

        puzzletrigger2.update(hero, MazePuzzle3, mission04)
        puzzledoor2.update(puzzletrigger2)

        plat1.update(hero)
        plat2.update(hero)
        plat3.update(hero)
        plat4.update(hero)
        plat5.update(hero)
        plat6.update(hero)
        plat7.update(hero)

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
        screen.blit(trig5.image, camera.apply(trig5))

        pygame.display.flip()



if __name__ == "__main__":
    mission04()
