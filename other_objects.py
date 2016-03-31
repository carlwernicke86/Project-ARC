import pygame
from KeyList import key_list

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
LIGHT_GREY = (200, 200, 200)
GREEN = (50, 200, 50)
BLUE = (50, 50, 200)
RED =(200, 50, 50)

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
    def __init__(self, size, color, box_color, position, text, font = None):
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

    def update(self, event, next_screen, end_event = None):
        self.gray = False
        mouse_pos = pygame.mouse.get_pos()
        if mouse_pos[0] > self.outline.left and mouse_pos[0] < self.outline.right and mouse_pos[1] > self.outline.top and mouse_pos[1] < self.outline.bottom:
            self.gray = True
        if event.type == pygame.MOUSEBUTTONDOWN and self.gray == True:
            print "hi"

    def TextBlit(self, screen):
        if self.gray == True:
            screen.blit(self.box, (self.box_x, self.box_y))
        screen.blit(self.image, (self.rect.x, self.rect.y))
        pygame.draw.rect(screen, BLACK, self.outline, 1)


class Option_Text(pygame.sprite.Sprite):
    def __init__(self, size, color, position, text, button, font = None):
        self.size = size
        self.color = color
        self.font = pygame.font.Font(font, size)
        self.image = self.font.render(self.text, 1, self.color)
        self.rect = self.image.get_rect()
        self.rect.center = position
        self.button = button
        self.back_rect = pygame.Rect(self.rect.top, self.rect.right + 5, self.rect.height + 3, 100)
        self.back = pygame.Surface([self.back_rect.width, self.back_rect.height])
        self.back.convert()
        self.back.fill(LIGHT_GREY)
        for k in key_list:
            if self.button == k[0]:
                self.button_text = k[1]
        self.button_text_image = self.font.Font(self.button_text, size)
        self.button_text_rect = self.button_text_image.get_rect()
        self.button_text_rect.x = self.back_rect.x + 3
        self.button_text_rect.y = self.rect.y
        self.selected = False

        def update(event, option_text_group):
            mouse_pos = pygame.mouse.get_pos()
            if event == pygame.MOUSEBUTTONDOWN and mouse_pos[0] > self.back_rect.left and mouse_pos[0] < self.back_rect.right and mouse_pos[1] > self.back_rect.top and mouse_pos[1] < self.back_rect.bottom:
                for o in option_text_group:
                    o.selected = False
                self.selected = True

            if self.selected == True:
                for k in key_list:
                    if event == k[0]:
                        self.button = k[0]
                        self.button_text = k[1]
                        self.button_text_image = self.font.Font(self.button_text, font)

        def TextBlit(screen):
            screen.blit(self.image, (self.rect.x, self.rect.y))
            screen.blit(self.back, (self.back_rect.x, self.back_rect.y))
            screen.blit(self.button_text_image, (self.button_text_rect.x, self.button_text_rect.y))

