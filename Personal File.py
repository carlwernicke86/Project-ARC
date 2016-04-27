__author__ = 'cardg_000'
import pygame

class Event(pygame.sprite.Sprite):
    def __init__(self, x, y, x_range, y_range, id):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.image = pygame.Surface((x_range*self.x, y_range*self.y)).convert()
        self.rect = self.image.get_rect
        self.rect.x = self.x
        self.id = id

    def update(self, hero, event_list):

         collision = pygame.sprite.spritecollide(self, hero, True)

         if collision == True:
             event_list[self.id-1] = 1