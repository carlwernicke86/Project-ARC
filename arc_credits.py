import pygame, sys
from other_objects import *

def credits():

    screen = pygame.display.set_mode((WIN_W, WIN_H), pygame.SRCALPHA)
    clock = pygame.time.Clock()

    credits = True

    pr = Regular_Text(80, YELLOW, (screen.get_rect().centerx/2, 100), "Programmers:")
    art = Regular_Text(80, YELLOW, (screen.get_rect().centerx*1.5, 100), "Artists:")

    al = Regular_Text(50, YELLOW, (screen.get_rect().centerx/2, 200), "Andy Lee - Object/Structure Design")
    cw = Regular_Text(50, YELLOW, (screen.get_rect().centerx/2, 300), "Carl Wernicke - Structure/Interface Design")
    rk = Regular_Text(50, YELLOW, (screen.get_rect().centerx/2, 400), "Rohit Kaushik - Level Design")
    vw = Regular_Text(50, YELLOW, (screen.get_rect().centerx*1.5, 200), "Valerie Wang")
    al1 = Regular_Text(50, YELLOW, (screen.get_rect().centerx*1.5, 300), "Lillian Murtonen")
    al2 = Regular_Text(50, YELLOW, (screen.get_rect().centerx*1.5, 400), "Tiffany Chu")
    al3 = Regular_Text(50, YELLOW, (screen.get_rect().centerx*1.5, 500), "Ryu-yan Cheng")

    regular_text_group = pygame.sprite.Group()
    regular_text_group.add(al, cw, rk, vw, al1, al2, al3, pr, art)

    exit = Click_Button(40, BLACK, LIGHT_GREY, (100, 800), "Back", False, None, None, None, WHITE)

    while credits:
        clock.tick(60)
        screen.fill((100, 100, 100))

        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            exit.update(screen, event)
            credits = exit.stay
            
        regular_text_group.update(screen)

        exit.TextBlit(screen)
        pygame.display.update()


