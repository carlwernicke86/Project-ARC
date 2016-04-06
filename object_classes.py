import pygame

#Constants
WIN_W = 1600
WIN_H = 900

#Placed at 128, 96 for apartment
class Hero(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.xvel = 0
        self.yvel = 0
        self.grounded = False
        self.side_speed = 3
        self.image = pygame.Surface((32, 64))
        self.image.convert()
        self.image.fill([108,80,55])
        self.rect = pygame.Rect((x,y,32,64))

        #Other stuff
        self.move_l = False
        self.move_r = False
        self.move_u = False
        self.move_d = False

    def update(self, platform_group):
        key = pygame.key.get_pressed()
        if key[pygame.K_d]:
            self.move_r = True
        if key[pygame.K_a]:
            self.move_l = True
        if key[pygame.K_w]:
            self.move_u = True
        if key[pygame.K_s]:
            self.move_d = True

        if not key[pygame.K_d]:
            self.move_r = False
        if not key[pygame.K_a]:
            self.move_l = False
        if not key[pygame.K_w]:
            self.move_u = False
        if not key[pygame.K_s]:
            self.move_d = False

        if self.move_u:
            if self.grounded:
                self.yvel -= 8
        if self.move_d:
            pass
        if self.move_l:
            self.xvel = -4
        if self.move_r:
            self.xvel = 4
        if not self.grounded:
            self.yvel += .35
            if self.yvel > 100:
                self.yvel = 100
        if not self.move_l and not self.move_r:
            self.xvel = 0

        self.rect.left += self.xvel
        self.collide(self.xvel, 0, platform_group)
        self.rect.top += self.yvel
        self.grounded = False
        self.collide(0, self.yvel, platform_group)

    def collide(self, xvel, yvel, platform_group):
        for p in platform_group:
            if pygame.sprite.collide_rect(self, p):
                if isinstance(p, WinDocs):
                    print "YOU WIN"
                if xvel > 0:
                    self.rect.right = p.rect.left
                if xvel < 0:
                    self.rect.left = p.rect.right
                if yvel > 0:
                    self.rect.bottom = p.rect.top
                    self.grounded = True
                    self.yvel = 0
                if yvel < 0:
                    self.rect.top = p.rect.bottom

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

class SecGuard(pygame.sprite.Sprite): #Includes flashlight, x dimension is 32 for guard + 96 for flashlight
    def __init__(self, direction, range, x, y): #The full distance a sec guard travels is the range in starting direction then range + 128 in the other direciton
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([128,64])
        self.image.convert()
        self.direction = direction
        self.y = y
        if self.direction == "left":
            self.image.fill((40, 106, 128))
        elif self.direction == "right":
            self.image.fill((150, 21, 49))
        self.range = range
        self.rect = pygame.Rect(x, y, 128, 64)
        self.steps = 0

    def update(self, hero, secguard_group):
        if pygame.sprite.spritecollideany(hero, secguard_group, collided = None) != None:
            print "GAME OVER"
        if self.direction == "left":
            self.rect.x -= 1
            self.steps += 1
        elif self.direction == "right":
            self.rect.x += 1
            self.steps += 1
        if self.direction == "left":
            self.image.fill((40, 106, 128))
        elif self.direction == "right":
            self.image.fill((150, 21, 49))
        if self.steps == self.range:
            self.steps = 0
            if self.direction == "left":
                self.rect = pygame.Rect(self.rect.x + 128, self.y, 128, 64)
                self.direction = "right"
            elif self.direction == "right":
                self.rect = pygame.Rect(self.rect.x - 128, self.y, 128, 64)
                self.direction = "left"

class WinDocs(Platform): #Touch these to win the level
    def __init__(self, x, y):
        Platform.__init__(self, (200, 200, 200), x, y)

class Trigger(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([32, 8])
        self.image.convert()
        self.image.fill((168, 30, 186))
        self.rect = pygame.Rect(x, y + 24, 32, 8)
        self.active = False

    def update(self, hero):
        if pygame.sprite.collide_rect(self, hero):
            self.active = True
        if self.active: #This is formatted like this in case we want timed triggers
            self.image.fill((243, 252, 63))

class TriggerDoor(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([32, 64])
        self.image.convert()
        self.image.fill((237, 147, 50))
        self.rect = pygame.Rect(x, y, 32, 64)
        self.movecount = 0

    def update(self, trigger):
        if trigger.active == True and self.movecount < 65:
            self.rect.y -= 1
            self.movecount += 1