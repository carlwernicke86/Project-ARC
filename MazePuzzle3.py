import pygame, sys
from MazePuzzleObjects import *

WIN_W = 1600
WIN_H = 900

TIMER = 0

#Time Variables are defined below
clock = pygame.time.Clock()            #The clock which can be used to set fps
beg_time = pygame.time.get_ticks()     #The time the game first begins
fps = 60

def MazePuzzle3():
    pygame.init()

    mpuzzle3 = True
    pygame.display.set_caption("Project ARC")
    screen = pygame.display.set_mode((WIN_W, WIN_H), pygame.SRCALPHA)

    #Group creation
    wall_group = pygame.sprite.Group() #Just the walls and boundaries of the puzzle
    exit_group = pygame.sprite.Group() #Touch these to wim
    #Object creation
    hacker = Hacker(1472, 832, 5, "up")

    #The actual level
    maze3_level = [
        "WEEEEEWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",#1
        "W     WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
        "W                                                W",
        "W                                                W",
        "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW W  W   W  W",#5
        "W                                                W",
        "W                                                W",
        "W        W     WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
        "W  WWWWWWW                W                      W",
        "W        W                W                      W",#10
        "W        W    W   W       W    WWWWWWWWWWWWW     W",
        "WWW  WWWWW        W       W    W                 W",
        "W        W      WWW       W    W                 W",
        "W        W   W  W         W    W      WWWWWWWWWWWW",
        "W        W      W         W    W      W          W",#15
        "WW  WWWWWW      W         W    W      W          W",
        "W        W           WWWWWW    W      W     W    W",
        "W        W           W         W            W    W",
        "W        W           W         W            W    W",
        "W WWWWW  WWWWWWWW    W   WWWWWWWWWWWWWWWWWWWW    W",#20
        "W        W      W    W   W     W                 W",
        "W               W    W   W     W                 W",
        "W               W        W     W     WWWWWWWWWWWWW",
        "W        WWW  WWW        W           W           W",
        "W        W      WWWWWWWWWW           W           W",#25a
        "W        W                     W           W  H  W",
        "W        W                     W           W     W",
        "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
        "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
    ]   #01234567890123456789012345678901234567890123456789
        #0         1         2         3         4

    #Build level
    x = y= 0
    for row in maze3_level: #H only denotes where the hero starts, does not actually spawn anything
        for row in maze3_level:
            for col in row:
                if col == "W":
                    w = Wall(x, y)
                    wall_group.add(w)
                if col == "E":
                    e = ExitBlock(x, y)
                    exit_group.add(e)
                x += 32
            y += 32
            x = 0

    while mpuzzle3:
        clock.tick(fps)
        screen.fill((255, 255, 255))

        #Quit the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        hacker.update(wall_group, exit_group)

        for w in wall_group:
            screen.blit(w.image, (w.rect.x, w.rect.y))
        for e in exit_group:
            screen.blit(e.image, (e.rect.x, e.rect.y))
        screen.blit(hacker.image, (hacker.rect.x, hacker.rect.y))

        if hacker.deactivated:
            break
        if hacker.fail:
            return "Fail"

        pygame.display.flip()
