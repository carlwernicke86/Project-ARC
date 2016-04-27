import pygame, sys
from other_objects import *

WIN_W = 1600
WIN_H = 900

def win(hero, cur_level):
    win = True
    screen = pygame.display.set_mode((WIN_W, WIN_H), pygame.SRCALPHA)
    mission_complete = Regular_Text(100, BLACK, (screen.get_rect().centerx, screen.get_rect().centery/2), "Mission Complete!")

    regular_text_group = pygame.sprite.Group()
    regular_text_group.add(mission_complete)

    while win:

        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

        screen.fill(WHITE)
        regular_text_group.update(screen)

        pygame.display.flip()

    return None