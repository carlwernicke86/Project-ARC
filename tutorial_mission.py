import pygame, os, sys, math
from object_classes import *

os.environ["SDL_VIDE_CENTERED"] = '1'

TIMER = 0

#Constants
WIN_W = 1600
WIN_H = 900

def main():
    pygame.init()

    #Basic settings
    intro = tutorial = True
    pygame.display.set_caption("Project ARC")
    screen = pygame.display.set_mode((WIN_W, WIN_H), pygame.SRCALPHA)

    #Group creation
    platform_group = pygame.sprite.Group()
    hero_group = pygame.sprite.Group()
    secguard_group = pygame.sprite.Group()
    trigger_group = pygame.sprite.Group()

    #Object creation
    hero = Hero(96, 288)
    hero_group.add(hero)
    sec1 = SecGuard("right", 128, 640, 288)
    trig1 = Trigger(32, 320)

    secguard_group.add(sec1)

    #Load tutorial level
    tutorial_level = [ #3 space gap is jumpable
        "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP",
        "P                                                          P",
        "P                                                          P",
        "P                                                          P",
        "P                                                          P",
        "P                     PPPPPP                               P",
        "P                                                          P",
        "P                                                          P",
        "P          PPPPPPPP                                   PPPPPP",
        "P                                                     O    P",
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
                p = Platform([61, 61, 61], x, y)
                platform_group.add(p)
            if col == "D":
                d = WinDocs(x, y)
                platform_group.add(d)
            if col == "O":
                o = TriggerDoor(x, y)
                platform_group.add(o)
            x += 32
        y += 32
        x = 0

    #Set Up Camera
    total_width_app = len(tutorial_level[0]) * 32
    total_height_app = len(tutorial_level) * 32
    camera = Camera(total_width_app, total_height_app)

    # Apartment, mostly eye candy and mechanism for 'desk' level selector
    while tutorial:
        screen.fill((255, 255, 255))
        # Quitting the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        # Update
        hero_group.update(platform_group)
        camera.update(hero.rect)
        secguard_group.update(hero, secguard_group)
        trig1.update(hero)
        platform_group.update(trig1)

        # Put stuff on the screen yo
        for p in platform_group:
            screen.blit(p.image, camera.apply(p))
        for h in hero_group:
            screen.blit(h.image, camera.apply(h))
        for sg in secguard_group:
            screen.blit(sg.image, camera.apply(sg))
        screen.blit(trig1.image, camera.apply(trig1))

        pygame.display.flip()


if __name__ == "__main__":
    main()