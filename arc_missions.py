import sys
from other_objects import *
from arc_missionList import mission_list

screen = pygame.display.set_mode((WIN_W, WIN_H), pygame.SRCALPHA)

def mission_screen(m, hero):                                                               #mission_goto initiates the level for the mission
    display_mission = Mission(screen, m[0], m[1],m[2], m[3], m[4], m[5])                     #Gives the displayed mission the properties it holds (screen, employer, building, difficulty, requirements, reward, mission_goto)
    exit = Click_Button(40, BLACK, LIGHT_GREY, (100, screen.get_rect().bottom - 100), "Missions", False)
    click_button_group = pygame.sprite.Group()
    click_button_group.add(exit)
    mission_screen_loop = True
    while mission_screen_loop:

        screen.fill(WHITE)
        for event in pygame.event.get():
            click_button_group.update(screen, event)
            display_mission.update(screen, event)
            if exit.stay == False or display_mission.decline.stay == False:
                mission_screen_loop = False


            if event.type == pygame.QUIT: sys.exit()

        hero.menu = display_mission.accept.went_to_screen
        if hero.menu == True:
            break

        display_mission.TextBlit(screen)
        exit.TextBlit(screen)

        pygame.display.update()


def missions(hero):

    exit = Click_Button(40, BLACK, WHITE, (screen.get_rect().centerx, screen.get_rect().bottom - 100), "Back", False)
    click_button_group = pygame.sprite.Group()
    click_button_group.add(exit)
    MissionSave = open('MissionSaveFile.rtf', 'r')
    lvl1 = MissionSave.readline()
    lvl2 = MissionSave.readline()
    lvl3 = MissionSave.readline()
    if lvl1 == "False" + "\n":
        lvl1comp = False
    elif lvl1 == "True" + "\n":
        lvl1comp = True
    if lvl2 == "False" + "\n":
        lvl2comp = False
    elif lvl1 == "True" + "\n":
        lvl2comp = True
    if lvl3 == "False":
        lvl3comp = False
    elif lvl3 == "True":
        lvl3comp = True
    MissionSave.close()

    for m in range(len(mission_list)):                                                                           #The last argument here is the argument that needs to be passed into the button's next_screen method
        if m == 0:
            button = Click_Button(40, BLACK, LIGHT_GREY, (screen.get_rect().centerx, 50 + (50 * m)), "Mission " + str(m + 1), mission_screen, mission_list[m], hero)
        if m == 1:
            if lvl1comp == True:
                button = Click_Button(40, BLACK, LIGHT_GREY, (screen.get_rect().centerx, 50 + (50 * m)), "Mission " + str(m + 1), mission_screen, mission_list[m], hero)
        if m == 2:
            if lvl1comp == True and lvl2comp == True:
                button = Click_Button(40, BLACK, LIGHT_GREY, (screen.get_rect().centerx, 50 + (50 * m)), "Mission " + str(m + 1), mission_screen, mission_list[m], hero)
        if m == 3:
            if lvl1comp == True and lvl2comp == True and lvl3comp == True:
                button = Click_Button(40, BLACK, LIGHT_GREY, (screen.get_rect().centerx, 50 + (50 * m)), "Mission " + str(m + 1), mission_screen, mission_list[m], hero)
        click_button_group.add(button)

    mission_loop = True
    while mission_loop:

        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            click_button_group.update(screen, event)
            mission_loop = exit.stay

        if hero.menu == True:
            break

        screen.fill(WHITE)
        for c in click_button_group:
            c.TextBlit(screen)


        pygame.display.update()
