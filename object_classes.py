import pygame
from SpriteSheetFunction import SpriteSheet
from arc_pause import *
from arc_lose import lose
from KeyList import key_list

#Constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
LIGHT_GREY = (200, 200, 200)
GREEN = (50, 200, 50)
BLUE = (50, 50, 200)
RED =(200, 50, 50)

WIN_W = 1600
WIN_H = 900

#OTHER OBJECTS
#Position is a tuple of (x, y)
#So far we only have menuing text objects and buttons
class Regular_Text(pygame.sprite.Sprite):
    def __init__(self, size, color, position, text, font = None):
        pygame.sprite.Sprite.__init__(self)
        self.size = size
        self.color = color
        self.text = text
        self.font  = pygame.font.Font(font, size)
        self.image = self.font.render(self.text, 1, self.color)
        self.rect = self.image.get_rect()
        self.rect.center = position

    def update(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

class Click_Button(pygame.sprite.Sprite):
    def __init__(self, size, color, box_color, position, text, next_screen, object = None,font = None):
        pygame.sprite.Sprite.__init__(self)
        self.size = size
        self.color = color
        self.text = text
        self.font = pygame.font.Font(font, size)
        self.image = self.font.render(self.text, 1, self.color)
        self.rect = self.image.get_rect()
        self.rect.center = position
        self.outline = pygame.Rect(self.rect.x - 6, self.rect.y - 6, self.rect.width + 12, self.rect.height + 12)
        self.box = pygame.Surface((self.rect.width + 10, self.rect.height + 10))
        self.box.convert()
        self.box.fill((box_color))
        self.box_x = self.outline.x + 1
        self.box_y = self.outline.y + 1
        self.gray = False
        self.next_screen = next_screen
        self.stay = True
        self.object = object


    def update(self, screen, event):
        self.gray = False
        mouse_pos = pygame.mouse.get_pos()
        if mouse_pos[0] > self.outline.left and mouse_pos[0] < self.outline.right and mouse_pos[1] > self.outline.top and mouse_pos[1] < self.outline.bottom:
            self.gray = True
        if event.type == pygame.MOUSEBUTTONUP and self.gray == True:
            if self.next_screen == False or self.next_screen == True:
                self.stay = self.next_screen
            elif self.next_screen == None:
                return None
            elif self.object != None:
                self.next_screen(self.object, screen)
            else:
                self.next_screen(screen)
            self.gray = False


    def TextBlit(self, screen):
        if self.gray == True:
            screen.blit(self.box, (self.box_x, self.box_y))
        screen.blit(self.image, (self.rect.x, self.rect.y))
        pygame.draw.rect(screen, BLACK, self.outline, 1)


class Option_Text(pygame.sprite.Sprite):
    def __init__(self, size, color, position, text, button, font = None):
        pygame.sprite.Sprite.__init__(self)
        self.size = size
        self.color = color
        self.font = pygame.font.Font(font, size)
        self.text = text
        self.image = self.font.render(self.text, 1, self.color)
        self.rect = self.image.get_rect()
        self.rect.topright = position
        self.button = button
        self.back_rect = pygame.Rect(self.rect.right + 5, self.rect.top, self.rect.height + 3, 4 * self.size)
        self.back = pygame.Surface([self.back_rect.height, self.back_rect.width])
        self.back.convert()
        self.back.fill(LIGHT_GREY)
        for k in key_list:
            if self.button == k[0]:
                self.button_text = k[1]
        self.button_text_image = self.font.render(self.button_text, 1, self.color)
        self.button_text_rect = self.button_text_image.get_rect()
        self.button_text_rect.x = self.back_rect.x + 3
        self.button_text_rect.y = self.rect.y
        self.selected = False
        self.back_outline = pygame.Rect(self.back_rect.x - 1, self.back_rect.top - 4, self.back_rect.height + 2, self.back_rect.width + 2)

    def update(self, event, option_text_group, mouse_pos):
        if event.type == pygame.MOUSEBUTTONDOWN and mouse_pos[0] > self.back_outline.left and mouse_pos[0] < self.back_outline.right and mouse_pos[1] > self.back_outline.top and mouse_pos[1] < self.back_outline.bottom:
            for o in option_text_group:
                o.selected = False
            self.selected = True

        if self.selected == True:
             for k in key_list:
                 if event.type == pygame.KEYDOWN and event.key == k[0]:
                    self.button = k[0]
                    self.button_text = k[1]
                    self.button_text_image = self.font.render(self.button_text, 1, self.color)
                    
        return self.button

    def TextBlit(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
        screen.blit(self.back, (self.back_rect.x, self.back_rect.y - 3))
        screen.blit(self.button_text_image, (self.button_text_rect.x, self.button_text_rect.y))
        if self.selected == True:
            pygame.draw.rect(screen, BLACK, self.back_outline, 1)


class Mission():
    def __init__(self, screen, employer, building, difficulty, requirements, reward, mission_goto):
        self.employer = employer
        self.employer_text = Regular_Text(40, BLACK, (screen.get_rect().centerx, 100), ("Employer: " + str(employer)))
        self.building = building
        self.building_text = Regular_Text(40, BLACK, ((screen.get_rect().centerx), 200), ("Location: " + str(building)))
        self.difficulty = Regular_Text(40, BLACK, ((screen.get_rect().centerx), 300), ("Difficulty: " + str(difficulty)))
        self.requirements = requirements
        self.requirements_text = Regular_Text(40, BLACK, (screen.get_rect().centerx, 400), ("Requirements: "))
        self.reward = reward
        self.reward_text = Regular_Text(40, BLACK, ((screen.get_rect().centerx), 500), ("Reward: " + str(reward)))
        self.accept = Click_Button(40, GREEN, LIGHT_GREY, (screen.get_rect().centerx - 100, 600), "Accept", mission_goto)
        self.decline = Click_Button(40, RED, LIGHT_GREY, (screen.get_rect().centerx + 100, 600), "Decline", False)

    def update(self, screen, event):
        self.accept.update(screen, event)
        self.decline.update(screen, event)

    def TextBlit(self, screen):
        screen.blit(self.employer_text.image, (self.employer_text.rect.x, self.employer_text.rect.y))
        screen.blit(self.building_text.image, (self.building_text.rect.x, self.building_text.rect.y))
        screen.blit(self.difficulty.image, (self.difficulty.rect.x, self.difficulty.rect.y))
        screen.blit(self.reward_text.image, (self.reward_text.rect.x, self.reward_text.rect.y))
        screen.blit(self.requirements_text.image, (self.requirements_text.rect.x, self.requirements_text.rect.y))
        self.accept.TextBlit(screen)
        self.decline.TextBlit(screen)
        for r in range(len(self.requirements)):
            screen.blit(Regular_Text(40, BLACK, (0, 0), str(self.requirements[r])).image, (self.requirements_text.rect.right + 10, self.requirements_text.rect.y + (60 * r)))


class Scroll_Text(pygame.sprite.Sprite):
    def __init__(self, text, color, font = None, go = False):
        pygame.sprite.Sprite.__init__(self)
        self.text = text
        self.color = color
        self.font = pygame.font.Font(font, 40)
        self.image = self.font.render("", 1, self.color)
        self.timer = 0
        self.rect = pygame.Rect(150, WIN_H - 150, 1300, 140)
        self.go = go
        self.cur_text = ""

    def Scroll(self, screen, TIMER):
        self.go = Scroll = True
        self.cur_text = ""
        self.image = self.font.render(self.cur_text, 1, self.color)
        while Scroll:
            TIMER += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_t:
                        if self.cur_text == self.text:
                            Scroll = False
                        elif self.cur_text != self.text:
                            self.cur_text = self.text


            if self.go == True and TIMER%20 == 0:
                self.cur_text = self.text[0:len(self.cur_text) + 1]
                self.image = self.font.render(self.cur_text, 1, self.color)

            pygame.draw.rect(screen, BLACK, self.rect, 1)
            screen.blit(self.image, (self.rect.left + 20, self.rect.top + 20))
            pygame.display.update()



    def update(self, screen, cur_event, activate_event):
        if cur_event == activate_event:
            self.go = True


    def TextBlit(self, screen, TIMER):
        if self.go == True and TIMER%1 == 0:
            self.cur_text = self.text[0:len(self.cur_text) + 1]
            self.image = self.font.render(self.cur_text, 1, self.color)

        pygame.draw.rect(screen, BLACK, self.rect, 1)
        screen.blit(self.image, (self.rect.left + 20, self.rect.top + 20))

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
        if key[pygame.K_p]:
            self.pause = True

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

        if self.pause == True:
            pause(self)
            self.pause = False

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
            
        if self.hidden:
            print "HIDDEN"
            if self.move_r or self.move_l or self.move_u or self.move_d:
                self.hidden = False
            self.step_num_left = 0
            self.step_num_right = 0

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
            lose()
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
    def __init__(self, x, y, ontime, offtime, delayed): #Ontime is how long the laser is on, offtime is how long the laser is off
        pygame.sprite.Sprite.__init__(self) #delayed determines if the laser starts in the on or off position, usually it will be False
        self.image = pygame.Surface([8, 64])
        self.image.convert()
        self.image.fill((247, 29, 29))
        self.rect = pygame.Rect(x, y, 8, 64)
        self.ontime = ontime
        self.offtime = offtime
        if delayed:
            self.active = False
        else:
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
            lose()

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

    def update(self, hero, screen, missions):
        if hero.interact:
            if hero.rect.bottom == self.rect.bottom and abs(hero.rect.centerx - self.rect.centerx) < 40:
                missions(screen)
                
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
