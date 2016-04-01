from other_objects import *
import pygame, sys

def options(screen):
    #These are all the options buttons
    jump = Option_Text(100, BLACK, (screen.get_rect().centerx/2, screen.get_rect().centery/2), "Jump:", pygame.K_SPACE)
    right = Option_Text(100, BLACK, (jump.rect.centerx, jump.rect.centery + 125), "Right:", pygame.K_d)
    left = Option_Text(100, BLACK, (jump.rect.centerx, jump.rect.centery + 250), "Left: ", pygame.K_a)

    right.rect.right = jump.rect.right
    left.rect.right = jump.rect.right
    option_text_group = pygame.sprite.Group()
    option_text_group.add(jump, right, left)

    #This is the escape button
    exit = Click_Button(40, BLACK, LIGHT_GREY, (screen.get_rect().centerx, screen.get_rect().bottom - 100), "Main Menu")
    click_button_group = pygame.sprite.Group()
    click_button_group.add(exit)

    options = True
    while options:
        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            option_text_group.update(event, option_text_group,mouse_pos)
            click_button_group.update(screen, event, options)
            if event.type == pygame.QUIT: sys.exit()



        screen.fill(WHITE)
        for o in option_text_group:
            o.TextBlit(screen)
        for c in click_button_group:
            c.TextBlit(screen)

        pygame.display.flip()