from other_objects import *
import pygame, sys

screen = pygame.display.set_mode((WIN_W, WIN_H), pygame.SRCALPHA)
def options():
    ControlOptions = open('ControlOptions.txt', 'r')
    jump_button = ControlOptions.readline()
    left_button = ControlOptions.readline()
    right_button = ControlOptions.readline()
    interact_button = ControlOptions.readline()
    ControlOptions.close()

    jump_button = jump_button[0:len(jump_button) - 1]
    left_button = left_button[0:len(left_button) - 1]
    right_button = right_button[0:len(right_button) - 1]
    interact_button = interact_button


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
    

    option_text_group = pygame.sprite.Group()
    option_text_group.add(jump, right, left, interact)

    #This is the escape button
    exit = Click_Button(40, BLACK, LIGHT_GREY, (screen.get_rect().centerx, screen.get_rect().bottom - 100), "Main Menu", False)
    click_button_group = pygame.sprite.Group()
    click_button_group.add(exit)

    jump_button = jump.button
    left_button = left.button
    right_button = right.button
    interact_button = interact.button
    
    bg = pygame.image.load("Sprites/MainBack.png")
    
    option = True
    while option:
        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            old_jump = jump.button
            jump_button = jump.update(event, option_text_group,mouse_pos)
            old_left = left.button
            left_button = left.update(event, option_text_group,mouse_pos)
            old_right = right.button
            right_button = right.update(event, option_text_group,mouse_pos)
            old_interact = interact.button
            interact_button = interact.update(event, option_text_group,mouse_pos)


            if jump.button == left.button:
                if left.selected == True:
                    jump.button = old_left
                elif jump.selected == True:
                    left.button = old_jump
            elif jump.button == right.button:
                if jump.selected == True:
                    right.button = old_jump
                elif right.selected == True:
                    jump.button = old_right
            elif jump.button == interact.button:
                if jump.selected == True:
                    interact.button = old_jump
                elif interact.selected == True:
                    jump.button = old_interact

            if left.button == right.button:
                if left.selected == True:
                    right.button = old_left
                elif right.selected == True:
                    left.button = old_right
            elif left.button == interact.button:
                if left.selected == True:
                    interact.button = old_left
                elif interact.selected == True:
                    left.button = old_interact

            if right.button == interact.button:
                if right.selected == True:
                    interact.button = old_right
                elif interact.selected == True:
                    right.button = old_interact


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

        screen.blit(bg, (0, 0))
        for o in option_text_group:
            o.TextBlit(screen)
        for c in click_button_group:
            c.TextBlit(screen)

        pygame.display.flip()
