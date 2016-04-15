from other_objects import *
import pygame, sys

def options(screen):
    #These are all the options buttons
    jump = Option_Text(100, BLACK, (screen.get_rect().centerx, screen.get_rect().centery/2 - 150), "Jump:", pygame.K_w)
    right = Option_Text(100, BLACK, (screen.get_rect().centerx, jump.rect.y + 125), "Right:", pygame.K_d)
    left = Option_Text(100, BLACK, (screen.get_rect().centerx, jump.rect.y + 250), "Left: ", pygame.K_a)
    interact = Option_Text(100, BLACK, (screen.get_rect().centerx, jump.rect.y + 375), "Interact: ", pygame.K_e)

    option_text_group = pygame.sprite.Group()
    option_text_group.add(jump, right, left, interact)

    #This is the escape button
    exit = Click_Button(40, BLACK, LIGHT_GREY, (screen.get_rect().centerx, screen.get_rect().bottom - 100), "Main Menu", False)
    click_button_group = pygame.sprite.Group()
    click_button_group.add(exit)

    option = True
    while option:
        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            jump_button = jump.update(event, option_text_group,mouse_pos)
            left_button = left.update(event, option_text_group,mouse_pos)
            right_button = right.update(event, option_text_group,mouse_pos)
            interact_button = interact.update(event, option_text_group,mouse_pos)

            click_button_group.update(screen, event)
            option = exit.stay
            if event.type == pygame.QUIT: sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    option = False

        screen.fill(WHITE)
        for o in option_text_group:
            o.TextBlit(screen)
        for c in click_button_group:
            c.TextBlit(screen)

        pygame.display.flip()
