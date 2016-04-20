import pygame
from MazePuzzleObjects import *

WIN_W = 1600
WIN_H = 900

TIMER = 0

#Time Variables are defined below
clock = pygame.time.Clock()            #The clock which can be used to set fps
beg_time = pygame.time.get_ticks()     #The time the game first begins
fps = 60

def MazePuzzle1(clock, fps):
    pygame.init()