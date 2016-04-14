import pygame

class SpriteSheet():
    #Grabs images out of the sprite sheet
    def __init__(self, file_name):
        self.sprite_sheet = pygame.image.load(file_name).convert()

    def get_image(self, x, y, width, height):
        #Grabs a single image out of the sprite sheet, pass in x, y of sprite and width, height

        #Creates a new blank image
        image = pygame.Surface([width, height]).convert()

        #Copy sprite from large sheet onto smaller image
        image.blit(self.sprite_sheet, (0,0), (x,y,width,height))

        #set_colorkey makes anything with that RGB value transparent
        image.set_colorkey((0,0,0))

        return image