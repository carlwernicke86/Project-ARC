import pygame, os, sys, math

os.environ["SDL_VIDE_CENTERED"] = '1'

#Constants
WIN_W = 1600
WIN_H = 900

class Hero(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.side_speed = 3
        self.jump_speed = 4
        self.image = pygame.Surface((32, 64))
        self.image.convert()
        self.image.fill([108,80,55])
        self.rect = pygame.Rect((200,200,32,64))

    def update(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_d]:
            self.rect.x += self.side_speed
        if key[pygame.K_a]:
            self.rect.x -= self.side_speed

class Platform(pygame.sprite.Sprite):
    def __init__(self, color, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([32,32])
        self.image.convert()
        self.image.fill(color)
        self.rect = pygame.Rect(x,y,32,32)

def main():
    pygame.init()

    apartment = desk = True
    pygame.display.set_caption("Project ARC")
    screen = pygame.display.set_mode((WIN_W, WIN_H), pygame.SRCALPHA)

    #total_rect = pygame.rect.Rect(0,0, 60*32, 6*32)

    platform_group = pygame.sprite.Group()
    hero_group = pygame.sprite.Group()
    hero = Hero()
    hero_group.add(hero)

    # Load apartment level
    apartment_level = [
        "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP",
        "P                   P          P     P          P          P",
        "P                   P          P     P          P          P",
        "P                                                          P",
        "P                                                          P",
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
            x += 32
        y += 32
        x = 0

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
        hero_group.update()

        #Draw
        hero_group.draw(screen)
        platform_group.draw(screen)

        pygame.display.flip()


if __name__ == "__main__":
    main()