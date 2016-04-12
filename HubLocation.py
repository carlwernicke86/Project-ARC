import pygame, os, sys, math
from object_classes import *
from other_objects import *

os.environ["SDL_VIDEO_CENTERED"] = '1'

TIMER = 0

#Constants
WIN_W = 1600
WIN_H = 900

def hub(screen, clock, fps):
    pygame.init()

    apartment = desk = True

    platform_group = pygame.sprite.Group()
    hero_group = pygame.sprite.Group()

    hero = Hero(128, 96)
    hero_group.add(hero)

    dummy_scroll = Scroll_Text("hi",BLACK)

    # Load apartment level
    apartment_level = [
        "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP",
        "P                   P          P     P          P          P",
        "P                                                          P",
        "P                                                          P", #| This represents the player height in relation to the level
        "P                                                    D     P", #|
        "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP",
    ]
    #80 P wide (60 * 32) and 6 P high (6 * 32)

    #Build level
    x = y = 0
    platforms = []
    for row in apartment_level:
        for col in row:
            if col == "P":
                p = Platform([176, 162, 150], x, y)
                platform_group.add(p)
            if col == "D":
                d = WinDocs(x, y)
                platform_group.add(d)
            x += 32
        y += 32
        x = 0

    #Set Up Camera
    total_width_app = len(apartment_level[0]) * 32
    total_height_app = len(apartment_level) * 32
    camera = Camera(total_width_app, total_height_app)

    #Apartment, mostly eye candy and mechanism for 'desk' level selector
    while apartment:
        clock.tick(fps)
        screen.fill((255,255,255))
        #Quitting the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                dummy_scroll.update(screen, event.key, pygame.K_RETURN)
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()


        #Update
        hero_group.update(platform_group)
        camera.update(hero.rect)
        dummy_scroll.TextBlit(screen, TIMER)

        #Put stuff on the screen yo
        for p in platform_group:
            screen.blit(p.image, camera.apply(p))
        for h in hero_group:
            screen.blit(h.image, camera.apply(h))

        pygame.display.flip()
