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

def tutorial(clock, fps):
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
    ScrollTextIntroTrig = GenericTrigger(128, 322)

    #Text creation
    ScrollTextIntro = Scroll_Text("Welcome to Project ARC! Default movement keys are W for Jump, A for Left, D for Right.", (0,0,0))

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

    # Apartment, mostly eye candy and mechanism for 'desk' level selector
    while tutorial_loop:
        clock.tick(fps)
        screen.fill((255, 255, 255))
        # Quitting the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # Update
        hero_group.update(platform_group, tutorial)
        camera.update(hero.rect)
        secguard_group.update(hero, secguard_group, tutorial)
        trig1.update(hero)
        platform_group.update(trig1)
        motsen_group.update(hero, tutorial)
        #movelaser_group.update(hero)
        trigger_group.update(hero)
        ScrollTextIntro.update(screen, True, ScrollTextIntroTrig.active)

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
        for ST in ScrollText_group:
            ST.Scroll(screen, TIMER)
            ST.TextBlit(screen, TIMER)
        for t in trigger_group:
            screen.blit(t.image, camera.apply(t))

        pygame.display.flip()


if __name__ == "__main__":
    tutorial(clock, fps)
