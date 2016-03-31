import pygame, sys
from other_objects import *





def intro(screen, clock, fps):

    #Regular Text Objects, images can be added later
    Title = Regular_Text(80, BLACK, (screen.get_rect().centerx, screen.get_rect().centery/2), "Project ARC")

    #Click Text Objects
    New_Game = Click_Button(40, BLACK, LIGHT_GREY, (screen.get_rect().centerx, screen.get_rect().centery/1.5), "New Game" )
    Options = Click_Button(40, BLACK, LIGHT_GREY, (screen.get_rect().centerx, New_Game.rect.y + 65), "Options")

    #Groups and adding things to groups
    regular_text_group = pygame.sprite.Group()
    regular_text_group.add(Title)

    click_text_group = pygame.sprite.Group()
    click_text_group.add(New_Game, Options)



    intro = True
    while intro:
        clock.tick(fps)

        for event in pygame.event.get():
            click_text_group.update(event, None)
            if event.type == pygame.QUIT: sys.exit()

        screen.fill(WHITE)
        regular_text_group.draw(screen)
        for i in click_text_group:
            i.TextBlit(screen)


        pygame.display.flip()