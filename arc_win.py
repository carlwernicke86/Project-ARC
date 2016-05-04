import pygame, sys
from other_objects import *

WIN_W = 1600
WIN_H = 900

def win(hero, cur_level):
    level1 = False
    level2 = False
    level3 = False

    MissionSave = open('MissionSaveFile', 'r')
    readlvl1 = MissionSave.readline()
    readlvl2 = MissionSave.readline()
    readlvl3 = MissionSave.readline()
    if readlvl1 == "False" + "\n":
        level1 = False
    elif readlvl1 == "True" + "\n":
        level1 = True
    if readlvl2 == "False" + "\n":
        level2 = False
    elif readlvl1 == "True" + "\n":
        level2 = True
    if readlvl3 == "False":
        level3 = False
    elif readlvl3 == "True":
        level3 = True
    MissionSave.close()

    level = str(cur_level)
    level = level[10:19]
    if level == "mission01":
        level1 = True
    if level == "mission02":
        level2 = True
    if level == "mission03":
        level3 = True

    MissionSave = open('MissionSaveFile', 'w')
    MissionSave.write(str(level1) + "\n")
    MissionSave.write(str(level2) + "\n")
    MissionSave.write(str(level3))
    MissionSave.close()
    
    win = True
    screen = pygame.display.set_mode((WIN_W, WIN_H), pygame.SRCALPHA)
    mission_complete = Regular_Text(100, BLACK, (screen.get_rect().centerx, screen.get_rect().centery/2), "Mission Complete!")
    Continue = Click_Button(40, BLACK, GREEN, (screen.get_rect().centerx, screen.get_rect().centery), "Continue", False)

    regular_text_group = pygame.sprite.Group()
    regular_text_group.add(mission_complete)

    click_button_group = pygame.sprite.Group()
    click_button_group.add(Continue)

    while win:

        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            click_button_group.update(screen, event)
            win = Continue.stay


        screen.fill(WHITE)
        for c in click_button_group:
            c.TextBlit(screen)
        regular_text_group.update(screen)

        pygame.display.flip()


    hero.dead = True
    hero.menu = True
    return None
