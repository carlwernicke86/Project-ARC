import pygame, sys
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
     def __init__(self, size, color, box_color, position, text, next_screen, object = None, object2 = None, font = None):
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
         self.object2 = object2
         self.went_to_screen = False


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
            elif self.object2 != None:
                self.went_to_screen = True
                self.next_screen(self.object, self.object2)
            elif self.object != None:
                self.went_to_screen = True
                self.next_screen(self.object)
            else:
                self.went_to_screen = True
                self.next_screen()
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

        for k in key_list:
            if k[0] == self.button:
                self.button_text = k[1]
        self.button_text_image = self.font.render(self.button_text, 1, self.color)

        return self.button_text

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
