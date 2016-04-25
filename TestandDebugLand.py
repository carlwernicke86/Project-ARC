import pygame, os, sys, math
from object_classes import *
from MazePuzzle1 import *

os.environ["SDL_VIDE_CENTERED"] = '1'

TIMER = 0

#Time Variables are defined below
clock = pygame.time.Clock()            #The clock which can be used to set fps
beg_time = pygame.time.get_ticks()     #The time the game first begins
fps = 60

#Constants
WIN_W = 1600
WIN_H = 900

def main(clock, fps):
    pygame.init()

    #Basic settings
    debugland = True
    pygame.display.set_caption("Project ARC")
    screen = pygame.display.set_mode((WIN_W, WIN_H), pygame.SRCALPHA)

    #Group creation
    platform_group = pygame.sprite.Group() #Walls, floors, and stuff
    hero_group = pygame.sprite.Group() #The main character
    secguard_group = pygame.sprite.Group() #Security Guards
    motsen_group = pygame.sprite.Group() #Motion sensing lasers
    movelaser_group = pygame.sprite.Group() #Moving motion sensor lasers
    hidingspot_group = pygame.sprite.Group() #Potted plants, places the hero can hide
    puzzletrigger_group = pygame.sprite.Group() #Triggers puzzles that are required to open puzzle doors

    #Object creation
    hero = Hero(96, 288)
    hero_group.add(hero)
    puzzletrigger = PuzzleDoorTrigger(960, 224) #Original x value at 896, y 288
    puzzletrigger_group.add(puzzletrigger)
    puzzledoor = PuzzleDoor(960, 288)
    platform_group.add(puzzledoor)

    #Load tutorial level
    test_level = [ #3 space gap is jumpable
        "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP", #0
        "P                                                          P", #1
        "P                                                          P", #2
        "P                                                          P", #3
        "P                                                          P", #4
        "P                                                          P", #5
        "P                                                          P", #6
        "P                                                          P", #7
        "P                                                          P", #8
        "P          H                                               P", #9
        "P                            P                             P", #10
        "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP"  #11
    ]   #012345678901234567890123456789012345678901234567890123456789
        #          1         2         3         4         5
         #Multiply by 32 to get x placement value

    #Build level
    x = y = 0
    platforms = []
    for row in test_level:
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
                l = MotionSensor(x, y, 180, 180, False)
                motsen_group.add(l)
            if col == "H":
                h = HidingSpot(x, y)
                hidingspot_group.add(h)
            x += 32
        y += 32
        x = 0

    #Set Up Camera
    total_width_app = len(test_level[0]) * 32
    total_height_app = len(test_level) * 32
    camera = Camera(total_width_app, total_height_app)

    # Apartment, mostly eye candy and mechanism for 'desk' level selector
    while debugland:
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
        motsen_group.update(hero)
        #movelaser_group.update(hero)
        hidingspot_group.update(hero)
        puzzletrigger.update(hero, MazePuzzle1)
        puzzledoor.update(puzzletrigger)

        # Put stuff on the screen yo
        for hs in hidingspot_group:
            screen.blit(hs.image, camera.apply(hs))
        for p in platform_group:
            screen.blit(p.image, camera.apply(p))
        for pt in puzzletrigger_group:
            screen.blit(pt.image, camera.apply(pt))
        for h in hero_group:
            screen.blit(h.image, camera.apply(h))
        for sg in secguard_group:
            screen.blit(sg.image, camera.apply(sg))
        for ms in motsen_group:
            if ms.active == True:
                screen.blit(ms.image, camera.apply(ms))

        pygame.display.flip()


if __name__ == "__main__":
    main(clock, fps)
