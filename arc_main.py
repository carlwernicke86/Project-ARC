import pygame, os

fps = 60

WIN_W = 1600
WIN_H = 900

pygame.init()

def main():

    #Screen Variables defined
    pygame.display.set_caption("Project ARC")       #Defines the text on the top of the window
    screen = pygame.display.set_mode()              #The screen

    #Time Variables are defined below
    clock = pygame.time.Clock((WIN_W, WIN_H), pygame.SRCALPHA)      #The clock which can be used to set fps
    beg_time = pygame.time.get_ticks()                              #The beginning time of the game's startup
