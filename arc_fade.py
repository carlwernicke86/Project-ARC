import pygame, sys
WIN_W = 1600
WIN_H = 900

def fade(screen):
    fade_frame = 0
    clock = pygame.time.Clock()
    fade_in_screen = pygame.Surface((WIN_W, WIN_H))
    fade_in_screen.set_alpha(0)

    while fade_frame < 255:
        clock.tick(60)

        #Fading
        fade_in_screen.fill((0, 0, 0))
        fade_in_screen.set_alpha(fade_frame)
        fade_frame += 1.5
        #Fading
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

        screen.fill((255, 255, 255))
        screen.blit(fade_in_screen, (0,0))
        pygame.display.flip()
        print fade_frame

