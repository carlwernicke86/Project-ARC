import pygame, os
from arc_intro import intro
from HubLocation import hub


fps = 60

WIN_W = 1600
WIN_H = 900

pygame.init()

#Screen Variables defined
pygame.display.set_caption("Project ARC")                                      #Defines the text on the top of the window
screen = pygame.display.set_mode((WIN_W, WIN_H), pygame.SRCALPHA)              #The screen

#Time Variables are defined below
clock = pygame.time.Clock()            #The clock which can be used to set fps
beg_time = pygame.time.get_ticks()     #The time the game first begins

def main():
    intro(screen, clock, fps)
    hub(screen, clock, fps)



main()