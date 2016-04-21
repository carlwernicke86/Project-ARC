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

    def update(self, wall_group, exit_group):
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

        for w in wall_group:
            if pygame.sprite.collide_rect(self, w):
                self.kill()
                print "GAME OVER"

        for e in exit_group:
            if pygame.sprite.collide_rect(self, e):
                self.kill()
                print "HACKED"

class ExitBlock(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([32, 32])
        self.image.convert()
        self.image.fill((18, 226, 18))
        self.rect = pygame.Rect(x, y, 32, 32)