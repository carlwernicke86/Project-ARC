import pygame, os, sys, math
from object_classes import *

os.environ["SDL_VIDE_CENTERED"] = '1'

TIMER = 0

#Time Variables are defined below
clock = pygame.time.Clock()            #The clock which can be used to set fps
beg_time = pygame.time.get_ticks()     #The time the game first begins
fps = 60

#Constants
WIN_W = 1600
WIN_H = 900

def tutorial(clock, fps, triggers = 0):
    pygame.init()

    #Basic settings
    tutorial_loop = True
    pygame.display.set_caption("Project ARC")
    screen = pygame.display.set_mode((WIN_W, WIN_H), pygame.SRCALPHA)

    #Group creation
    platform_group = pygame.sprite.Group() #Walls, floors, and stuff
    hero_group = pygame.sprite.Group() #The main character
    secguard_group = pygame.sprite.Group() #Security Guards
    motsen_group = pygame.sprite.Group() #Motion sensing lasers
    movelaser_group = pygame.sprite.Group() #Moving motion sensor lasers
    trigger_group = pygame.sprite.Group() #CAN ONLY TAKE ARGUMENT Hero
    ScrollText_group = pygame.sprite.Group()

    #Object creation
    hero = Hero(96, 288)
    hero_group.add(hero)
    sec1 = SecGuard("right", 128, 640, 288)
    trig1 = Trigger(1248, 224)
    #movelaser1 = MovingLaser(1056, 288, "left", 128)

    #Trigger creation (mostly for scroll text)





    if triggers <= 4:
        WinDocsTrig = GenericTrigger(1664, 200, 200)
        WinDocText = Scroll_Text("Collect the documents to complete the mission.", (0, 0, 0))
        trigger_group.add(WinDocsTrig)
        ScrollText_group.add(WinDocText)
    if triggers <= 3:
        DoorTextTrig = GenericTrigger(1376, 200, 200)
        DoorText = Scroll_Text("Activate the trigger in order to open the door.", (0, 0, 0))
        trigger_group.add( DoorTextTrig)
        ScrollText_group.add( DoorText)
    if triggers <= 2:
        LaserTextTrig = GenericTrigger(1152, 200, 200)
        LaserText = Scroll_Text("Avoid touching laser sensors! They will turn on and off periodically.", (0, 0, 0))
        trigger_group.add(LaserTextTrig)
        ScrollText_group.add(LaserText)
    if triggers <= 1:
        SecGuardTextTrig = GenericTrigger(224, 200, 200)
        SecGuardText = Scroll_Text("This is a security guard, avoid coming in contact with him and his flashlight!", (0, 0, 0))
        trigger_group.add(SecGuardTextTrig)
        ScrollText_group.add(SecGuardText)
    if triggers == 0:
        ScrollTextIntroTrig = GenericTrigger(96, 200, 200)
        ScrollTextIntro = Scroll_Text("Default movement keys are W for Jump, A for Left, D for Right. Press E to continue.", (0, 0, 0))
        trigger_group.add(ScrollTextIntroTrig)
        ScrollText_group.add(ScrollTextIntro)

    secguard_group.add(sec1)
    #movelaser_group.add(movelaser1)

    #Load tutorial level
    tutorial_level = [ #3 space gap is jumpable
        "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP",
        "P                                     P                    P",
        "P                                     P                    P",
        "P                                     P                    P",
        "P                                     P                    P",
        "P                     PPPPPP          P                    P",
        "P                                     P                    P",
        "P                                     P                    P",
        "P          PPPPPPPP                   PPPPP           PPPPPP",
        "P                                     LLLLL           O    P",
        "P                                                        D P",#288 y value
        "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP"
    ]   #01234567890123456789012345678901234567890123456789012345678
        #          1         2         3         4         5
         #Multiply by 32 to get x placement value

    #Build level
    x = y = 0
    platforms = []
    for row in tutorial_level:
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
                l = MotionSensor(x, y, 180, 180, False)
                motsen_group.add(l)
            x += 32
        y += 32
        x = 0

    #Set Up Camera
    total_width_app = len(tutorial_level[0]) * 32
    total_height_app = len(tutorial_level) * 32
    camera = Camera(total_width_app, total_height_app)

    fade_in_screen = pygame.Surface((WIN_W, WIN_H))
    fade_in_screen.set_alpha(255)

    full_fade = pygame.Surface([WIN_W, WIN_H])
    full_fade.fill(BLACK)
    fade_alpha = 0
    caught_timer = 0
    # Apartment, mostly eye candy and mechanism for 'desk' level selector
    while tutorial_loop:
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
        hero_group.update(platform_group, tutorial)
        camera.update(hero.rect)
        if hero.activate_caught == False:
            secguard_group.update(hero, secguard_group, tutorial)
            trig1.update(hero)
            platform_group.update(trig1)
            motsen_group.update(hero, tutorial)
            #movelaser_group.update(hero)
            trigger_group.update(hero)
            if triggers <= 4:
                WinDocText.update(screen, True, WinDocsTrig.active)
            if triggers <= 3:
                DoorText.update(screen, True, DoorTextTrig.active)
            if triggers <= 2:
                LaserText.update(screen, True, LaserTextTrig.active)
            if triggers <= 1:
                SecGuardText.update(screen, True, SecGuardTextTrig.active)
            if triggers == 0:
                ScrollTextIntro.update(screen, True, ScrollTextIntroTrig.active)

        
        if hero.dead == True:
            break

        # Put stuff on the screen yo
        for p in platform_group:
            screen.blit(p.image, camera.apply(p))
        for h in hero_group:
            screen.blit(h.image, camera.apply(h))
        for sg in secguard_group:
            screen.blit(sg.image, camera.apply(sg))
        for ms in motsen_group:
            if ms.active == True:
                screen.blit(ms.image, camera.apply(ms))
        #for ml in movelaser_group:
        #    screen.blit(ml.image, camera.apply(ml))
        screen.blit(trig1.image, camera.apply(trig1))

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
                tutorial_loop = False
        for ST in ScrollText_group:
            ST.Scroll(screen, TIMER)
            ST.TextBlit(screen, TIMER)
        #for t in trigger_group:
        #    screen.blit(t.image, camera.apply(t))

        pygame.display.flip()

    for t in trigger_group:
        if t.active == True:
            triggers += 1

    if hero.activate_caught == True:
        tutorial(clock, fps, triggers)

if __name__ == "__main__":
    tutorial(clock, fps)
