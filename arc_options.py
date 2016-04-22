from other_objects import *
import pygame, sys

def options(screen):
    ControlOptions = open('ControlOptions.txt', 'r')
    jump_button = ControlOptions.readline()
    left_button = ControlOptions.readline()
    right_button = ControlOptions.readline()
    interact_button = ControlOptions.readline()
    ControlOptions.close()

    jump_button = jump_button[0:len(jump_button) - 1]
    left_button = left_button[0:len(left_button) - 1]
    right_button = right_button[0:len(right_button) - 1]
    interact_button = interact_button[0]


    for k in key_list:
        if jump_button == k[1]:
            jump_button = k[0]
        if left_button == k[1]:
            left_button = k[0]
        if right_button == k[1]:
            right_button = k[0]
        if interact_button == k[1]:
            interact_button = k[0]

    #These are all the options buttons
    jump = Option_Text(100, BLACK, (screen.get_rect().centerx, screen.get_rect().centery/2 - 150), "Jump:", jump_button)
    right = Option_Text(100, BLACK, (screen.get_rect().centerx, jump.rect.y + 125), "Right:", right_button)
    left = Option_Text(100, BLACK, (screen.get_rect().centerx, jump.rect.y + 250), "Left: ", left_button)
    interact = Option_Text(100, BLACK, (screen.get_rect().centerx, jump.rect.y + 375), "Interact: ", interact_button)
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
            ControlOptions = open('ControlOptions.txt', 'w')
            ControlOptions.write(jump_button+"\n")
            ControlOptions.write(left_button+"\n")
            ControlOptions.write(right_button+"\n")
            ControlOptions.write(interact_button)
            ControlOptions.close()

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
