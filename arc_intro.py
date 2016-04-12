import pygame, sys
from other_objects import *
from arc_options import options
from arc_missions import missions

def intro(screen, clock, fps, TIMER):
    TIMER += 1

    #Regular Text Objects, images can be added later
    Title = Regular_Text(80, BLACK, (screen.get_rect().centerx, screen.get_rect().centery/2), "Project ARC")

    #Click Text Objects
    New_Game = Click_Button(40, BLACK, LIGHT_GREY, (screen.get_rect().centerx, screen.get_rect().centery/1.5), "New Game", False)
    Options = Click_Button(40, BLACK, LIGHT_GREY, (screen.get_rect().centerx, New_Game.rect.y + 65), "Options", options)
    Mission_Button = Click_Button(40, BLACK, LIGHT_GREY, (screen.get_rect().centerx, Options.rect.y + 65), "Missions", missions)

    #Groups and adding things to groups
    regular_text_group = pygame.sprite.Group()
    regular_text_group.add(Title)

    click_button_group = pygame.sprite.Group()
    click_button_group.add(New_Game, Options, Mission_Button)



    intro = True
    while intro:
        clock.tick(fps)

        for event in pygame.event.get():
            click_button_group.update(screen, event)
            intro = New_Game.stay
            if event.type == pygame.QUIT: sys.exit()

        screen.fill(WHITE)
        regular_text_group.draw(screen)
        for i in click_button_group:
            i.TextBlit(screen)


        pygame.display.flip()