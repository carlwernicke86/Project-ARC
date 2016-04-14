import pygame
from arc_missions import missions
from SpriteSheetFunction import SpriteSheet

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
        self.rect = pygame.Rect((x,y,24,64))

        #Other stuff
        self.move_l = False
        self.move_r = False
        self.move_u = False
        self.move_d = False
        self.moving = False #For motion triggered sensors

        self.facing = "right"
        self.step_num_right = 0
        self.step_num_left = 0

        self.interact = False

        #Sprite sheet loading
        right_sprite_sheet = SpriteSheet("Sprites/player_sprite_right.png")
        left_sprite_sheet = SpriteSheet("Sprites/player_sprite_left.png")
        self.walking_frames_r = []
        self.walking_frames_l = []
        #Loading into a list
        #RIGHT SIDE
        image = right_sprite_sheet.get_image(0, 0, 24, 64)
        self.walking_frames_r.append(image)
        image = right_sprite_sheet.get_image(32, 0, 24, 64)
        self.walking_frames_r.append(image)
        image = right_sprite_sheet.get_image(64, 0, 24, 64)
        self.walking_frames_r.append(image)
        image = right_sprite_sheet.get_image(96, 0, 24, 64)
        self.walking_frames_r.append(image)
        image = right_sprite_sheet.get_image(128, 0, 24, 64)
        self.walking_frames_r.append(image)
        image = right_sprite_sheet.get_image(160, 0, 24, 64)
        self.walking_frames_r.append(image)
        image = right_sprite_sheet.get_image(192, 0, 24, 64)
        self.walking_frames_r.append(image)
        image = right_sprite_sheet.get_image(224, 0, 24, 64)
        self.walking_frames_r.append(image)
        #LEFT SIDE
        image = left_sprite_sheet.get_image(0, 0, 24, 64)
        self.walking_frames_l.append(image)
        image = left_sprite_sheet.get_image(32, 0, 24, 64)
        self.walking_frames_l.append(image)
        image = left_sprite_sheet.get_image(64, 0, 24, 64)
        self.walking_frames_l.append(image)
        image = left_sprite_sheet.get_image(96, 0, 24, 64)
        self.walking_frames_l.append(image)
        image = left_sprite_sheet.get_image(128, 0, 24, 64)
        self.walking_frames_l.append(image)
        image = left_sprite_sheet.get_image(192, 0, 24, 64)
        self.walking_frames_l.append(image)
        image = left_sprite_sheet.get_image(224, 0, 24, 64)
        self.walking_frames_l.append(image)

        self.image = self.walking_frames_r[0]
        self.image.convert()


    def update(self, platform_group):
        key = pygame.key.get_pressed()
        if key[pygame.K_d] == True and key[pygame.K_a] == True:
            self.move_r = False
            self.move_l = False
        if key[pygame.K_d] == True and key[pygame.K_a] == False:
            self.move_r = True
            self.facing = "right"
            self.step_num_right += 1
            self.step_num_left = 0
        if key[pygame.K_a] == True and key[pygame.K_d] == False:
            self.move_l = True
            self.facing = "left"
            self.step_num_left += 1
            self.step_num_right = 0
        if key[pygame.K_w]:
            self.move_u = True
        if key[pygame.K_s]:
            self.move_d = True
        if key[pygame.K_e]:
            self.interact = True

        if not key[pygame.K_d]:
            self.move_r = False
            self.step_num_right = 0
        if not key[pygame.K_a]:
            self.move_l = False
            self.step_num_left = 0
        if not key[pygame.K_w]:
            self.move_u = False
        if not key[pygame.K_s]:
            self.move_d = False
        if not key[pygame.K_e]:
            self.interact = False

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

        if self.xvel != 0:
            self.moving = True
        else:
            self.moving = False

        self.rect.left += self.xvel
        self.collide(self.xvel, 0, platform_group)
        self.rect.top += self.yvel
        self.grounded = False
        self.collide(0, self.yvel, platform_group)

        if self.step_num_left == 19:
            self.step_num_left = 0
        if self.step_num_right == 19:
            self.step_num_right = 0
        if self.facing == "right":
            self.image = self.walking_frames_r[self.step_num_right//3]
        if self.facing == "left":
            self.image = self.walking_frames_l[self.step_num_left//3]

    def collide(self, xvel, yvel, platform_group):
        for p in platform_group:
            if pygame.sprite.collide_rect(self, p):
                if isinstance(p, WinDocs):
                    x = 1
                if xvel > 0:
                    self.rect.right = p.rect.left
                if xvel < 0:
                    self.rect.left = p.rect.right
                if yvel > 0:
                    self.rect.bottom = p.rect.top
                    self.grounded = True
                    self.yvel = 0
                if yvel < 0:
                    self.yvel = 0
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
    def __init__(self, direction, range, x, y): #The full distance a sec guard travels is the range in starting direction then range + 128 in the other direction
        pygame.sprite.Sprite.__init__(self)
        self.direction = direction
        self.y = y
        if self.direction == "left":
            self.image = pygame.image.load("Sprites/security_guard_left.png").convert_alpha()
        elif self.direction == "right":
            self.image = pygame.image.load("Sprites/security_guard_right.png").convert_alpha()
        self.image.convert()
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
        if self.steps == self.range:
            self.steps = 0
            if self.direction == "left":
                self.rect = pygame.Rect(self.rect.x + 128, self.y, 128, 64)
                self.direction = "right"
            elif self.direction == "right":
                self.rect = pygame.Rect(self.rect.x - 128, self.y, 128, 64)
                self.direction = "left"
        if self.direction == "left":
            self.image = pygame.image.load("Sprites/security_guard_left.png").convert_alpha()
        elif self.direction == "right":
            self.image = pygame.image.load("Sprites/security_guard_right.png").convert_alpha()

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
        if trigger.active == True and self.movecount < 64:
            self.rect.y -= 1
            self.movecount += 1

class MotionSensor(pygame.sprite.Sprite): #This is misleading, you have to walk through these to trigger them
    def __init__(self, x, y, ontime, offtime): #Ontime is how long the laser is on, offtime is how long the laser is off
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([8, 64])
        self.image.convert()
        self.image.fill((247, 29, 29))
        self.rect = pygame.Rect(x, y, 8, 64)
        self.ontime = ontime
        self.offtime = offtime
        self.active = True
        self.ontimer = 0 #Counts how long the laser is on
        self.offtimer = 0 #Counts how long the laser is off

    def update(self, hero):
        if self.active == True:
            self.ontimer += 1
        elif self.active == False:
            self.offtimer += 1
        if self.ontimer == self.ontime:
            self.ontimer = 0
            self.active = False
        if self.offtimer == self.offtime:
            self.offtimer = 0
            self.active = True
        if pygame.sprite.collide_rect(self, hero) and self.active == True:
            print "CAUGHT"

class MovingLaser(pygame.sprite.Sprite): #Only triggers if you are moving as the laser passes over you
    def __init__(self, x, y, direction, distance):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([8, 64])
        self.image.convert()
        self.image.fill((29, 134, 226))
        self.rect = pygame.Rect(x, y, 8, 64)
        self.direction = direction
        self.distance = distance
        self.moved = 0 #Measures how much the laser has moved
        self.speed = 2

    def update(self, hero):
        if pygame.sprite.collide_rect(self, hero) and hero.moving == True:
            print "YOU GOT CAUGHT"
        if self.direction == "left":
            self.rect.x -= self.speed
            self.moved += self.speed
        if self.direction == "right":
            self.rect.x += self.speed
            self.moved += self.speed
        if self.direction == "left" and self.moved == self.distance:
            self.moved = 0
            self.direction = "right"
        if self.direction == "right" and self.moved == self.distance:
            self.moved = 0
            self.direction = "left"

class LaunchDesk(Platform):
    def __init__(self, x, y):
        Platform.__init__(self, (154, 90, 7), x, y)

    def update(self, hero, screen):
        if hero.interact:
            if hero.rect.bottom == self.rect.bottom and abs(hero.rect.centerx - self.rect.centerx) < 40:\
                missions(screen)