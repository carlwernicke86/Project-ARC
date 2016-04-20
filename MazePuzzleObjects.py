import pygame
from arc_pause import *
WIN_W = 1600
WIN_H = 900

class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([32, 32])
        self.image.convert()
        self.image.fill((226, 18, 18))
        self.rect = pygame.Rect(x, y, 32 ,32)

"""class Hacker(pygame.sprite.Sprite):
    def __init__(self, x, y, speed, facing):
        pygame.sprite.Sprite.__init__(self)
        self.facing = facing
        self.speed = speed

        self.image = pygame.Surface([32, 32])
        self.image.convert()
        self.image.fill((4, 74, 238))
        self.rect = pygame.Rect((x, y, 32, 32))

        self.pause = False

        self.move_l = False
        self.move_r = False
        self.move_u = False
        self.move_d = False

    def update(self, wall_group):
        key = pygame.key.get_pressed()
        if key[pygame.K_w] == True and not self.move_d:
            self.move_u = True
            self.move_r = False
            self.move_d = False
            self.move_l = False
            self.facing = "up"
        if key[pygame.K_a] == True and not self.move_r:
            self.move_l = True
            self.move_r = False
            self.move_d = False
            self.move_u = False
            self.facing = "left"
        if key[pygame.K_d] == True and not self.move_l:
            self.move_r = True
            self.move_d = False
            self.move_u = False
            self.move_l = False
            self.facing = "right"
        if key[pygame.K_s] == True and not self.move_u:
            self.move_d = True
            self.move_r = False
            self.move_u = False
            self.move_l = False
            self.facing = "down"

        if self.move_u:
            self.rect.y -= self.speed
        if self.move_d:
            self.rect.y += self.speed
        if self.move_l:
            self.rect.x -= self.speed
        if self.move_r:
            self.rect.x += self.speed
"""
class Hacker(pygame.sprite.Sprite):
    def __init__(self, x, y, speed, facing):
        pygame.sprite.Sprite.__init__(self)
        self.facing = facing
        self.speed = speed

        self.image = pygame.Surface([32, 32])
        self.image.convert()
        self.image.fill((4, 74, 238))
        self.rect = pygame.Rect((x, y, 32, 32))

        self.pause = False

    def update(self, wall_group):
        key = pygame.key.get_pressed()
        if key[pygame.K_w] == True and self.facing != "down":
            self.facing = "up"
        if key[pygame.K_a] == True and self.facing != "right":
            self.facing = "left"
        if key[pygame.K_d] == True and self.facing != "left":
            self.facing = "right"
        if key[pygame.K_s] == True and self.facing != "up":
            self.facing = "down"

        if self.facing == "up":
            self.rect.y -= self.speed
        if self.facing == "down":
            self.rect.y += self.speed
        if self.facing == "left":
            self.rect.x -= self.speed
        if self.facing == "right":
            self.rect.x += self.speed