import random
import pygame
from pygame.locals import *
from pygame import mixer
from קבועים import *
def animals_move(animals):
    for i in range(len(animals)):
        if animals[i].alive == True:
            if animals[i].deraction == True:
                animals[i].x_pos += 5
                if animals[i].x_pos > animals[i].x_max:
                    animals[i].deraction = False
                    animals[i].image = hatalef_left
            if animals[i].deraction == False:
                animals[i].x_pos -= 5
                if animals[i].x_pos < animals[i].x_min:
                    animals[i].deraction = True
                    animals[i].image = hatalef_rite


def hitnagsot(animals):
    return1 = False
    for i in range(len(animals)):
        if (animals[i].x_pos < 210 + 50 // 2 < animals[i].x_pos + animals[i].WIDTH) and (
                animals[i].y_pos < 210 + 50 // 2 < animals[i].y_pos + animals[i].HEIGHT):
            if animals[i].deraction == False:
                animals[i].deraction = True
                animals[i].image = hatalef_rite

            elif animals[i].deraction == True:
                animals[i].deraction = False
                animals[i].image = hatalef_left



            return True
        else:
            return1 = False

    return return1



