import pygame, sys
from other_objects import *

WIN_W = 1600
WIN_H = 900
def lose(cur_level):
    screen = pygame.display.set_mode((WIN_W, WIN_H), pygame.SRCALPHA)
    clock = pygame.time.Clock()

    lose = True
    game_over = Regular_Text(100, BLACK, (screen.get_rect().centerx, screen.get_rect().centery/2), "GAME OVER")
    retry = Click_Button(40, BLACK, LIGHT_GREY, (screen.get_rect().centerx/2, screen.get_rect().centery), "Retry", False)
    apartment = Click_Button(40, BLACK, LIGHT_GREY, (screen.get_rect().centerx, screen.get_rect().centery), "Back to Apartment", False)
    exit = Click_Button(40, BLACK, LIGHT_GREY, (screen.get_rect().centerx * 1.5, screen.get_rect().centery), "Main Menu", False)

    regular_button_group = pygame.sprite.Group()
    regular_button_group.add(game_over)
    click_button_group = pygame.sprite.Group()
    click_button_group.add(retry, apartment, exit)


    while lose:
        clock.tick(60)
        screen.fill(WHITE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            for c in click_button_group:
                c.update(screen, event)
                
            lose = retry.stay

        for c in click_button_group:
            c.TextBlit(screen)
        for r in regular_button_group:
            r.update(screen)

        pygame.display.flip()
        
    if retry.stay == False:
        cur_level()


