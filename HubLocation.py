import pygame, os, sys, math
from object_classes import *

os.environ["SDL_VIDE_CENTERED"] = '1'

TIMER = 0

#Constants
WIN_W = 1600
WIN_H = 900

def main():
    pygame.init()

    apartment = desk = True
    pygame.display.set_caption("Project ARC")
    screen = pygame.display.set_mode((WIN_W, WIN_H), pygame.SRCALPHA)

    platform_group = pygame.sprite.Group()
    hero_group = pygame.sprite.Group()
    secguard_group = pygame.sprite.Group()

    sec1 = SecGuard("left", 96, 384, 96)
    secguard_group.add(sec1)
    hero = Hero(128, 96)
    hero_group.add(hero)


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
        screen.fill((255,255,255))
        #Quitting the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        #Update
        hero_group.update(platform_group)
        camera.update(hero.rect)
        secguard_group.update(hero, secguard_group)

        #Put stuff on the screen yo
        for p in platform_group:
            screen.blit(p.image, camera.apply(p))
        for h in hero_group:
            screen.blit(h.image, camera.apply(h))
        for sg in secguard_group:
            screen.blit(sg.image, camera.apply(sg))

        pygame.display.flip()


if __name__ == "__main__":
    main()