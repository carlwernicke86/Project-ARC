import pygame, os
from arc_intro import intro
from HubLocation import hub
from other_objects import *


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
    ControlOptions = open('ControlOptions.txt', 'r')
    if ControlOptions.readline() == "W\n" and ControlOptions.readline() == "A\n" and ControlOptions.readline() == "D\n" and ControlOptions.readline() == "E":
        ControlOptions.close()
        ControlOptions = open('ControlOptions.txt', "w")
        ControlOptions.write("W"+"\n")
        ControlOptions.write("A"+"\n")
        ControlOptions.write("D"+"\n")
        ControlOptions.write("E")
    ControlOptions.close()


    TIMER = 0
    structure_loop = True
    while structure_loop:
        intro(screen, clock, fps, TIMER)
        structure_loop = hub(screen, clock, fps, TIMER)



main()