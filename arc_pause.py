__author__ = 'cardg_000'
from other_objects import *



def pause(hero):

    screen = pygame.display.set_mode((WIN_W, WIN_H), pygame.SRCALPHA)

    pause = Regular_Text(80, BLACK, (screen.get_rect().centerx, screen.get_rect().centery/2), "Paused")
    paused_text_group = pygame.sprite.Group()
    paused_text_group.add(pause)

    while hero.pause == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    hero.pause = False

        screen.fill(WHITE)
        paused_text_group.draw(screen)


        pygame.display.flip()