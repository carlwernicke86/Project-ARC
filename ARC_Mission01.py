import pygame, os, sys, math
from object_classes import *

TIMER = 0

#Time Variables are defined below
clock = pygame.time.Clock()            #The clock which can be used to set fps
beg_time = pygame.time.get_ticks()     #The time the game first begins
fps = 60

#Constants
WIN_W = 1600
WIN_H = 900

def mission01(intro_flag = False):
    pygame.init()
    
    pygame.mixer.music.stop()
    try:
        pygame.mixer.music.load("Sounds/InLimboSong.mp3")
        pygame.mixer.music.play(-1)
    except pygame.error:
        pass

    #Basic settings
    mission01_loop = True
    pygame.display.set_caption("Project ARC")
    screen = pygame.display.set_mode((WIN_W, WIN_H), pygame.SRCALPHA)
    
    level1 = Regular_Text(100, BLACK, (screen.get_rect().centerx, screen.get_rect().centery/2), "Level 1")
    press_continue = Regular_Text(50, (200, 200, 200), (screen.get_rect().centerx, screen.get_rect().centery), "- Press Any Button to Proceed -")

    #Group creation
    platform_group = pygame.sprite.Group()
    hero_group = pygame.sprite.Group()
    secguard_group = pygame.sprite.Group()
    motsen_group = pygame.sprite.Group()
    movelaser_group = pygame.sprite.Group()

    #Object creation
    hero = Hero(64, 160)
    sec1 = SecGuard("right", 256, 608, 160) #Farthest right is 1152 [36] (end of flashlight)
    sec2 = SecGuard("left", 352, 1504, 160) #Farthest right is 1856 [58]
    trig1 = Trigger(160,192)
    triggerdoor1 = TriggerDoor(192, 160) #Just triggerdoor1 is updated later, independent of the platform_group.
                                        # We can use this method for future objects that need collision but have different update arguments.
    trig2 = Trigger(1888, 192)
    hero_group.add(hero)
    secguard_group.add(sec1)
    secguard_group.add(sec2)
    platform_group.add(triggerdoor1)

    #Load the level
    mission01_level = [
        "I     PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP",
        "I     PPPPPPPPP                                                   P",
        "I     PPPPPPPPP                                                   P",
        "I     PPPPPPPPP  PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP   P",
        "I     PPPPPPPPP                                             P     P",
        "I      dddddddL                                             O     P",
        "I               P                                              D  P",
        "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP"
    ]   #0123456789012345678901234567890123456789012345678901234567890123456
        #          1         2         3         4         5         6

    #Build level
    x = y = 0
    platforms = []
    for row in mission01_level:
        for col in row:
            if col == "P":
                p = Platform("Sprites/BlackBlock.png", x, y)
                platform_group.add(p)
            if col == "D":
                d = WinDocs(x, y)
                platform_group.add(d)
            if col == "O":
                o = TriggerDoor(x, y)
                platform_group.add(o)
            if col == "L":
                l = MotionSensor(x, y, 370, 45, False)
                motsen_group.add(l)
            if col == "d":
                l2 = MotionSensor(x, y, 999999999999, 370 + 45 + 10, True)
                motsen_group.add(l2)
            if col == "I":
                i = InvisibleWall(x, y)
                platform_group.add(i)
            x += 32
        y += 32
        x = 0

    #Set Up Camera
    total_width_app = len(mission01_level[0]) * 32
    total_height_app = len(mission01_level) * 32
    camera = Camera(total_width_app, total_height_app)
    if intro_flag == False:

        pre_level_loop_in = True
        while pre_level_loop_in:
            clock.tick(60)
            for event in pygame.event.get():                    #Fading in Loop
                if event.type == pygame.QUIT: sys.exit()
                if event.type == pygame.KEYDOWN:
                    pre_level_loop_in = False

            screen.fill(BLACK)
            level1.fade_in(screen)
            if level1.red > 252:
                cur_time = pygame.time.get_ticks()
                press_continue.blink(screen, cur_time, beg_time)
            pygame.display.update()

        for i in range(150):
            clock.tick(60)                                      #Fading out Loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()

            screen.fill(BLACK)
            level1.fade_out(screen)

            pygame.display.update()

    fade_in_screen = pygame.Surface((WIN_W, WIN_H))

    fade_in_screen.set_alpha(255)
    if intro_flag == True:
        fade_in_screen.set_alpha(0)
        
    full_fade = pygame.Surface([WIN_W, WIN_H])
    full_fade.fill(BLACK)
    fade_alpha = 0
    caught_timer = 0
    while mission01_loop:
        clock.tick(fps)
        if hero.activate_caught == False:
            screen.fill((100, 100, 100))
        elif hero.activate_caught == True:
            screen.fill(WHITE)
            caught_timer += 1

        # Quitting the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # Update
        hero_group.update(platform_group, mission01)
        camera.update(hero.rect)
        if hero.activate_caught == False:
            secguard_group.update(hero, secguard_group, mission01)
            trig1.update(hero)
            triggerdoor1.update(trig1)
            #platform_group.update()
            motsen_group.update(hero, mission01)
            movelaser_group.update(hero, mission01)

        if hero.dead == True:
            break

        #Draw something
        for p in platform_group:
            screen.blit(p.image, camera.apply(p))
        for h in hero_group:
            screen.blit(h.image, camera.apply(h))
        for sg in secguard_group:
            screen.blit(sg.image, camera.apply(sg))
        for ms in motsen_group:
            if ms.active == True:
                screen.blit(ms.image, camera.apply(ms))
        screen.blit(trig1.image, camera.apply(trig1))
        screen.blit(trig2.image, camera.apply(trig2))

        screen.blit(fade_in_screen, (0, 0))
        if fade_in_screen.get_alpha() != 0:
            fade_in_screen.set_alpha(fade_in_screen.get_alpha() - 3)
        
        if hero.activate_caught == True:

            if caught_timer > 30:
                for sg in secguard_group:
                    if sg.rect.y < hero.rect.y + 64 and sg.rect.y > hero.rect.y- 64:
                        if sg.direction == "left":
                            if hero.rect.x < sg.rect.right:
                                sg.image = pygame.image.load("Sprites/security_guard_left.png").convert_alpha()
                                sg.exclamation.rect.x = sg.rect.x + sg.rect.width - sg.rect.width/8
                            elif hero.rect.x > sg.rect.right:
                                sg.image = pygame.image.load("Sprites/security_guard_right.png").convert_alpha()
                                sg.exclamation.rect.x = sg.rect.x + sg.rect.width/8
                            else:
                                sg.image = pygame.image.load("Sprites/security_guard_right.png").convert_alpha()
                                sg.exclamation.rect.x = sg.rect.x + sg.rect.width/8

                        elif sg.direction == "right":
                            if hero.rect.x < sg.rect.right + sg.rect.width:
                                sg.image = pygame.image.load("Sprites/security_guard_left.png").convert_alpha()
                                sg.exclamation.rect.x = sg.rect.x + sg.rect.width - sg.rect.width/8
                            elif hero.rect.x > sg.rect.right + sg.rect.width:
                                sg.image = pygame.image.load("Sprites/security_guard_right.png").convert_alpha()
                                sg.exclamation.rect.x = sg.rect.x + sg.rect.width/8
                            else:
                                sg.image = pygame.image.load("Sprites/security_guard_right.png").convert_alpha()
                                sg.exclamation.rect.x = sg.rect.x + sg.rect.width/8


                    sg.exclamation.rect.y = sg.rect.y - sg.rect.height/2
                    if caught_timer < 90:
                        screen.blit(sg.exclamation.image, (sg.exclamation.rect.x, sg.exclamation.rect.y))

            if caught_timer > 120:
                fade_alpha += 3
                full_fade.set_alpha(fade_alpha)
                screen.blit(full_fade,(0, 0))

            if caught_timer > 200:
                lose(mission01, hero)

        pygame.display.flip()

if __name__ == "__main__":
    mission01()
