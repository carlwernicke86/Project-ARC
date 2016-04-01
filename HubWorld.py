import pygame, os, sys, math

os.environ["SDL_VIDE_CENTERED"] = '1'

TIMER = 0

#Constants
WIN_W = 1600
WIN_H = 900

class SpeculativeRect(pygame.sprite.Sprite):
    def __init__(self, hero):
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect((hero.side_speed + hero.rect.x, hero.jump_y + hero.rect.y, 32 + hero.side_speed * 2, 64 + hero.jump_y * 2))

class Hero(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.side_speed = 3
        self.image = pygame.Surface((32, 64))
        self.image.convert()
        self.image.fill([108,80,55])
        self.rect = pygame.Rect((128,96,32,64))
        #Jump stuff
        self.jump_height = 64
        self.jump_x = 1
        self.jump_y = 8
        self.jump_timer = 0
        self.jump_start = self.rect.y
        self.jump_end = self.rect.y - self.jump_height
        self.jumping = False
        #Other stuff
        self.move_l = False
        self.move_r = False
        self.move_u = False
        self.move_d = False
        self.canmove_l = True
        self.canmove_r = True
        self.canmove_u = True
        self.canmove_d = True

    def update(self, platform_group, SpecRect):
        self.jump_timer += 1
        SpecRect.rect.centerx = self.rect.centerx
        SpecRect.rect.centery = self.rect.centery
        key = pygame.key.get_pressed()
        if key[pygame.K_d]:
            """self.move_r = True
            if self.canmove_r == True:
                self.rect.x += self.side_speed"""
            self.rect.x += self.side_speed
        if key[pygame.K_a]:
            """self.move_l = True
            if self.canmove_l == True:
                self.rect.x -= self.side_speed"""
            self.rect.x -= self.side_speed
        if key[pygame.K_s]:
            """self.move_d = True
            if self.canmove_d == True:
                self.rect.y += self.jump_y"""
            self.rect.y += self.jump_y
        if key[pygame.K_w]:
            """if self.jump_timer % ((self.jump_height/self.jump_y) * 2) == 0 and self.canmove_u == True:
                self.jumping = True
            if self.rect.y == self.jump_end:
                self.jumping = False
                self.move_u = False
                self.jump_end = self.rect.y - self.jump_height
            if self.jumping == True:
                self.move_u = True
                self.rect.y -= self.jump_y"""
            self.rect.y -= self.jump_y

        for event in pygame.event.get():
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_d:
                    self.move_r = False
                if event.key == pygame.K_a:
                    self.move_l = False
                if event.key == pygame.K_s:
                    self.move_l = False
                #print "start", self.jump_start
                #print "end", self.jump_end
                #print "y", self.rect.y

        for p in platform_group:
            if pygame.sprite.collide_rect(SpecRect, p):
                print "COLLIDING"
                self.side_speed = abs(self.rect.centerx - p.rect.centerx)
                print "SELF CENTERX", self.rect.centerx
                print "PLATFORM CENTERX", p.rect.centerx
                print "Side speed", self.side_speed
                self.jump_y = abs(self.rect.centery - p.rect.centery)
                print "Jump speed", self.jump_y
        """
        for p in platform_group:
            if p.rect.top == self.rect.bottom:
                self.move_d = False
            else:
                self.move_d = True
            if p.rect.bottom == self.rect.top:
                self.move_u = False
            else:
                self.move_u = True
            if p.rect.left == self.rect.right:
                self.move_r = False
            else:
                self.move_r = True
            if p.rect.right == self.rect.left:
                self.move_l = False
            else:
                self.move_l = True
        if self.move_d == False:
            print "Cant move down"
        if self.move_l == False:
            print "Cant move left"
        else:
            self.moving = True
        """
        """if pygame.sprite.spritecollideany(self, platform_group, collided = None) != None:
            print "COLLISION"
            if self.move_r == True:
                self.canmove_r = False
            else:
                self.canmove_r = True
            if self.move_l == True:
                self.canmove_l = False
            else:
                self.canmove_l = True
            if self.move_d == True:
                self.canmove_d = False
            else:
                self.canmove_d = True
            if self.move_u == True:
                self.canmove_u = False
            else:
                self.canmove_u = True
        else:
            self.canmove_r = True
            self.canmove_l = True
            self.canmove_d = True
            self.canmove_u = True"""

class Platform(pygame.sprite.Sprite):
    def __init__(self, color, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([32,32])
        self.image.convert()
        self.image.fill(color)
        self.rect = pygame.Rect(x,y,32,32)

class Camera(object):
    def __init__(self, total_width, total_height):

        self.state = pygame.Rect(0, 0, total_width, total_height)

    def apply(self, target):
        return target.rect.move(self.state.topleft)

    def update(self, target_rect):
        x = -target_rect.x + WIN_W/2
        y = -target_rect.y + WIN_H/2
        #Stop at left edge
        if x > 0:
            x = 0
        #Stop at right edge
        elif x < -(self.state.width - WIN_W):
            x = -(self.state.width - WIN_W)
        #Stop at top
        if y > 0:
            y = 0
        #Stop at bottom
        elif y < -(self.state.height):
            y = -(self.state.height)
        self.state = pygame.Rect(x, y, self.state.width, self.state.height)

def main():
    pygame.init()

    apartment = desk = True
    pygame.display.set_caption("Project ARC")
    screen = pygame.display.set_mode((WIN_W, WIN_H), pygame.SRCALPHA)

    #total_rect = pygame.rect.Rect(0,0, 60*32, 6*32)

    platform_group = pygame.sprite.Group()
    hero_group = pygame.sprite.Group()
    hero = Hero()
    SpecRect = SpeculativeRect(hero)
    hero_group.add(hero)


    # Load apartment level
    apartment_level = [
        "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP",
        "P                   P          P     P          P          P",
        "P                                                          P",
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
        hero_group.update(platform_group, SpecRect)
        camera.update(hero.rect)

        #Put stuff on the screen yo
        for p in platform_group:
            screen.blit(p.image, camera.apply(p))
        for h in hero_group:
            screen.blit(h.image, camera.apply(h))

        pygame.display.flip()


if __name__ == "__main__":
    main()