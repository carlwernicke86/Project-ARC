import pygame, sys
from other_objects import *
from arc_options import options

def intro(screen, clock, fps, TIMER):
    TIMER += 1

    #Regular Text Objects, images can be added later
    Title = Regular_Text(80, ORANGE, (screen.get_rect().centerx, screen.get_rect().centery/2), "Project ARC")

    #Click Text Objects
    Continue = Click_Button(40, ORANGE, LIGHT_GREY, (screen.get_rect().centerx, screen.get_rect().centery/1.5), "Continue", False, None, None, None, WHITE)
    New_Game = Click_Button(40, ORANGE, LIGHT_GREY, (screen.get_rect().centerx, Continue.rect.y + 65), "Play", False, None, None, None, WHITE)
    Options = Click_Button(40, ORANGE, LIGHT_GREY, (screen.get_rect().centerx, New_Game.rect.y + 65), "Options", options, None, None, None, WHITE)
    
    #Groups and adding things to groups
    regular_text_group = pygame.sprite.Group()
    regular_text_group.add(Title)

    click_button_group = pygame.sprite.Group()
    click_button_group.add(New_Game, Options)

    bg = pygame.image.load("Sprites/MainBack.png")

    pygame.mixer.music.stop()
    try:
        pygame.mixer.music.load("Sounds/YourCellarSong.mp3")
        pygame.mixer.music.play(-1)
    except pygame.error:
        pass

    intro = True
    while intro:
        clock.tick(fps)

        for event in pygame.event.get():
            click_button_group.update(screen, event)
            intro = New_Game.stay
            if event.type == pygame.QUIT: sys.exit()

        screen.blit(bg, (0, 0))
        regular_text_group.draw(screen)
        for i in click_button_group:
            i.TextBlit(screen)


        pygame.display.flip()

