import pygame
from SpriteSheetFunction import SpriteSheet
from arc_pause import *
from arc_lose import lose
from arc_win import win
from KeyList import key_list
from KeyList import key_decoder

#Constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
LIGHT_GREY = (200, 200, 200)
GREEN = (50, 200, 50)
BLUE = (50, 50, 200)
RED =(200, 50, 50)

WIN_W = 1600
WIN_H = 900

clock = pygame.time.Clock()
fps = 60

#Position is a tuple of (x, y)

#OBJECT CLASSES
#Placed at 128, 96 for apartment
class Hero(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.xvel = 0
        self.yvel = 0
        self.grounded = False
        self.side_speed = 3
        self.rect = pygame.Rect((x,y,24,64))
        self.pause = False

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
        
        self.hidden = False

        #Keys
        self.key_right = ""
        self.key_left = ""
        self.key_jump = ""
        self.key_interact = ""

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
        self.dead = False
        self.menu = False

    def update(self, platform_group, cur_level):
        ControlOptions = open('ControlOptions.txt', 'r')
        CtrlOp_jump = ControlOptions.readline()
        CtrlOp_left = ControlOptions.readline()
        CtrlOp_right = ControlOptions.readline()
        CtrlOp_intr = ControlOptions.readline()
        self.key_jump = [item for item in key_list if item[1] + "\n" == CtrlOp_jump]
        self.key_left = [item for item in key_list if item[1] + "\n" == CtrlOp_left]
        self.key_right = [item for item in key_list if item[1] + "\n" == CtrlOp_right]
        self.key_interact = [item for item in key_list if item[1] == CtrlOp_intr]
        self.key_jump = self.key_jump[0][0]
        self.key_left = self.key_left[0][0]
        self.key_right = self.key_right[0][0]
        self.key_interact = self.key_interact[0][0]

        key = pygame.key.get_pressed()
        if key[self.key_right] == True and key[self.key_left] == True:
            self.move_r = False
            self.move_l = False
        if key[self.key_right] == True and key[self.key_left] == False:
            self.move_r = True
            self.facing = "right"
            self.step_num_right += 1
            self.step_num_left = 0
        if key[self.key_left] == True and key[self.key_right] == False:
            self.move_l = True
            self.facing = "left"
            self.step_num_left += 1
            self.step_num_right = 0
        if key[self.key_jump]:
            self.move_u = True
        if key[pygame.K_s]:
            self.move_d = True
        if key[self.key_interact]:
            self.interact = True
        if key[pygame.K_p]:
            self.pause = True

        if not key[self.key_right]:
            self.move_r = False
            self.step_num_right = 0
        if not key[self.key_left]:
            self.move_l = False
            self.step_num_left = 0
        if not key[self.key_jump]:
            self.move_u = False
        if not key[pygame.K_s]:
            self.move_d = False
        if not key[self.key_interact]:
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
            
        if self.yvel > 0.7:
            self.moving = True

        if self.xvel != 0:
            self.moving = True
        else:
            self.moving = False

        if self.pause == True:
            pause(self)
            self.pause = False

        self.rect.left += self.xvel
        self.collide(self.xvel, 0, platform_group, cur_level)
        self.rect.top += self.yvel
        self.grounded = False
        self.collide(0, self.yvel, platform_group, cur_level)

        if self.step_num_left == 19:
            self.step_num_left = 0
        if self.step_num_right == 19:
            self.step_num_right = 0
        if self.facing == "right":
            self.image = self.walking_frames_r[self.step_num_right//3]
        if self.facing == "left":
            self.image = self.walking_frames_l[self.step_num_left//3]
            
        if self.hidden:
            print "HIDDEN"
            if self.move_r or self.move_l or self.move_u or self.move_d:
                self.hidden = False
            self.step_num_left = 0
            self.step_num_right = 0

    def collide(self, xvel, yvel, platform_group, cur_level):
        for p in platform_group:
            if pygame.sprite.collide_rect(self, p):
                if isinstance(p, WinDocs):
                    win(self, cur_level)
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
    def __init__(self, image_path, x, y): #image_path "Sprites/something.png"
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image.convert()
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

    def update(self, hero, secguard_group, cur_level):
        if pygame.sprite.spritecollideany(hero, secguard_group, collided = None) != None:
            lose(cur_level, hero)
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
        Platform.__init__(self, "Sprites/WinDocs.png", x, y)

class Trigger(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Sprites/trigger.png").convert_alpha()
        self.image.convert()
        self.y = y
        self.rect = pygame.Rect(x, y + 24, 32, 8)
        self.active = False

    def update(self, hero):
        if pygame.sprite.collide_rect(self, hero):
            self.active = True
        if self.active: #This is formatted like this in case we want timed triggers
            self.rect.y = self.y + 24 + 4
            self.image = pygame.image.load("Sprites/triggerpressed.png").convert_alpha()


class InvisibleWall(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([32, 64])
        self.image.convert()
        self.image.fill((255, 255, 255))
        self.image.set_colorkey((255,255,255))
        self.rect = pygame.Rect(x, y, 32, 64)

class TriggerDoor(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Sprites/triggerdoor.png").convert_alpha()
        self.image.convert()
        self.rect = pygame.Rect(x, y, 32, 64)
        self.movecount = 0

    def update(self, trigger):
        if trigger.active == True and self.movecount < 64:
            self.rect.y -= 1
            self.movecount += 1

class MotionSensor(pygame.sprite.Sprite): #This is misleading, you have to walk through these to trigger them
    def __init__(self, x, y, ontime, offtime, delayed): #Ontime is how long the laser is on, offtime is how long the laser is off
        pygame.sprite.Sprite.__init__(self) #delayed determines if the laser starts in the on or off position, usually it will be False
        self.image = pygame.image.load("Sprites/LaserVertical.png").convert_alpha()
        self.image.convert()
        self.rect = pygame.Rect(x, y, 8, 64)
        self.ontime = ontime
        self.offtime = offtime
        if delayed:
            self.active = False
        else:
            self.active = True
        self.ontimer = 0 #Counts how long the laser is on
        self.offtimer = 0 #Counts how long the laser is off

    def update(self, hero, cur_level):
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
            lose(cur_level, hero)
            
class HotMotSen(pygame.sprite.Sprite):
    def __init__(self, x, y, ontime, offtime, delayed, length):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([length, 8])
        self.image.convert()
        self.image.fill((247, 29, 29))
        self.rect = pygame.Rect(x, y, length, 8)
        self.ontime = ontime
        self.offtime = offtime
        if delayed:
            self.active = False
        else:
            self.active = True
        self.ontimer = 0
        self.offtimer = 0
        
    def update(self, hero, cur_level):
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
            lose(cur_level, hero)

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

    def update(self, hero, cur_level):
        if pygame.sprite.collide_rect(self, hero) and hero.moving == True:
            lose(cur_level, hero)
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
        Platform.__init__(self, "Sprites/Desk.png", x, y)

    def update(self, hero, missions):
        if hero.interact:
            if hero.rect.bottom == self.rect.bottom and abs(hero.rect.centerx - self.rect.centerx) < 40:
                missions(hero)
                
class HidingSpot(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([32, 64])
        self.image.convert()
        self.image.fill((86,250,53))
        self.rect = pygame.Rect(x, y, 32, 64)

    def update(self, hero):
        if hero.interact:
            if abs(hero.rect.centerx - self.rect.centerx) < 5 and hero.rect.centery == self.rect.centery:
                distance = hero.rect.centerx - self.rect.centerx
                if distance != 0:
                    hero.rect.centerx = self.rect.centerx

                    hero.hidden = True
                else: #If the distance is 0, perfectly lined up
                    hero.hidden = True

class PuzzleDoor(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([32, 64])
        self.image.convert()
        self.image.fill((255, 0, 255))
        self.rect = pygame.Rect(x, y, 32, 64)
        self.movecount = 0

    def update(self, PuzzleDoorTrigger):
        if PuzzleDoorTrigger.active == True and self.movecount < 64:
            self.rect.y -= 1
            self.movecount += 1

class PuzzleDoorTrigger(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([32, 64])
        self.image.convert()
        self.image.fill((255, 153, 255))
        self.rect = pygame.Rect(x, y, 32, 64)
        self.active = False

    def update(self, hero, puzzle_function, cur_level):
        if hero.interact:
            if hero.rect.bottom == self.rect.bottom and abs(hero.rect.centerx - self.rect.centerx) < 10:
                if puzzle_function() == "Fail":
                    lose(cur_level, hero)
                else:
                    self.active = True
                    
class HMovPlat(pygame.sprite.Sprite): #Horizontal Moving Platforms
    def __init__(self, x, y, length, facing, movetime, speed): #x, y, length are ints; facing is str; movetime, speed are ints
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([length, 32])
        self.image.convert()
        self.image.fill((169, 30, 210))
        self.rect = pygame.Rect(x, y, length, 32)
        self.movetime = movetime
        self.timer = 0
        self.direction = facing #must be "left" or "right"
        self.speed = speed

    def update(self, hero):
        if self.direction == "left":
            self.rect.x -= self.speed
            self.timer += 1
        if self.direction == "right":
            self.rect.x += self.speed
            self.timer += 1
        if self.direction == "right" and self.timer == self.movetime:
            self.direction = "left"
            self.timer = 0
        if self.direction == "left" and self.timer == self.movetime:
            self.direction = "right"
            self.timer = 0

        if hero.rect.x > self.rect.x and hero.rect.x < self.rect.right and hero.rect.y - self.rect.y == -64:
            if self.direction == "left":
                hero.rect.x -= self.speed
            if self.direction == "right":
                hero.rect.x += self.speed
                
class GenericTrigger(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([32, 32])
        self.image.convert()
        self.image.fill((124, 231, 34))
        self.rect = pygame.Rect(x, y, 32 , 32)
        self.active = False

    def update(self, hero):
        if pygame.sprite.collide_rect(self, hero):
            self.active = True #[TRIGGERED]

#ELEVATOR OBJECTS
class ElevatorFloor(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([128, 32])
        self.image.convert()
        self.image.fill((212, 184, 144))
        self.rect = pygame.Rect(x, y, 32, 64)
        self.climbing = True
        self.climbtime = 0
        self.falling = False
        self.fallspeed = 2
    def update(self, e):
        if self.climbing:
            if self.climbtime < 2048:
                self.rect.y -= 2
                self.climbtime += 2
            elif self.climbtime >= 2048:
                self.climbing = False
        if self.falling:
            self.rect.y += self.fallspeed
            if self.fallspeed < 100:
                self.fallspeed += 2
        if self.rect.y > 2464:
            self.kill()
        if e.activated:
            self.falling = True

class ElevatorRoof(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([128, 32])
        self.image.convert()
        self.image.fill((212, 184, 144))
        self.rect = pygame.Rect(x, y, 32, 64)
        self.climbing = True
        self.climbtime = 0
        self.falling = False
        self.fallspeed = 2
    def update(self, e):
        if self.climbing:
            if self.climbtime < 2048:
                self.rect.y -= 2
                self.climbtime += 2
            elif self.climbtime >= 2048:
                self.climbing = False
        if self.falling:
            self.rect.y += self.fallspeed
            if self.fallspeed < 100:
                self.fallspeed += 2
        if self.rect.y > 2464:
            self.kill()
        if e.activated:
            self.falling = True

class ElevatorWall(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([32, 160])
        self.image.convert()
        self.image.fill((212, 184, 144))
        self.rect = pygame.Rect(x, y, 32, 64)
        self.climbing = True
        self.climbtime = 0
        self.falling = False
        self.fallspeed = 2
    def update(self, e):
        if self.climbing:
            if self.climbtime < 2048:
                self.rect.y -= 2
                self.climbtime += 2
            elif self.climbtime >= 2048:
                self.climb = False
        if self.falling:
            self.rect.y += self.fallspeed
            if self.fallspeed < 100:
                self.fallspeed += 2
        if self.rect.y > 2464:
            self.kill()
        if e.activated:
            self.falling = True

class ElevatorDoorFrame(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([32, 32])
        self.image.convert()
        self.image.fill((212, 184, 144))
        self.rect = pygame.Rect(x, y, 32, 32)
        self.climbing = True
        self.climbtime = 0
        self.falling = False
        self.fallspeed = 2
    def update(self, e):
        if self.climbing:
            if self.climbtime < 2048:
                self.rect.y -= 2
                self.climbtime += 2
            elif self.climbtime >= 2048:
                self.climbing = False
        if self.falling:
            self.rect.y += self.fallspeed
            if self.fallspeed < 100:
                self.fallspeed += 2
        if self.rect.y > 2464:
            self.kill()
        if e.activated:
            self.falling = True

class ElevatorDoor(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([32, 64])
        self.image.convert()
        self.image.fill((100, 255, 166))
        self.rect = pygame.Rect(x, y, 32, 64)
        self.climbing = True
        self.climbtime = 0
        self.falling = False
        self.fallspeed = 2
        self.opentimer = 0
        self.closetimer = 0
        self.opennow = False
        self.opendelay = 0
    def update(self, invisTrig, e):
        if self.climbing:
            if self.climbtime < 2048:
                self.rect.y -= 2
                self.climbtime += 2
            elif self.climbtime >= 2048:
                self.climbing = False
        if self.climbing == False and self.opendelay <= 30:
            self.opendelay += 1
        if self.opendelay == 30:
            self.opennow = True
        if self.climbing == False and self.opentimer < 65 and self.opennow == True:
            self.rect.y -= 1
            self.opentimer += 1
        if invisTrig.active and self.closetimer < 65:
            self.rect.y += 1
            self.closetimer += 1
        if self.falling:
            self.rect.y += self.fallspeed
            if self.fallspeed < 100:
                self.fallspeed += 2
        if self.rect.y > 2464:
            self.kill()
        if e.activated:
            self.falling = True
#I HAVE NO IDEA WHY THE ELEVATOR WORKS, I JUST KNOW THAT IT DOES
#END ELEVATOR CODE

class Event_Mission03(pygame.sprite.Sprite):
    def __init__(self, x, y, x_range, y_range, id):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.image = pygame.Surface((32*x_range, 32*y_range)).convert()
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y - 96
        self.id = id
        self.activated = False

    def update(self, hero, event_list):

        collision = pygame.sprite.collide_rect(self, hero)

        if collision == True:
            event_list[self.id-1] = 1
            self.activated = True

        return event_list

