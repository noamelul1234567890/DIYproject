import time
from קבועים import *
import pygame
import threading


from opening import screen

# atak = 'first'
from קבועים import rto, xx
atak_1 = [100, 300, True]
atak_2 = [200,200,True]


def bose_atak(atak,a,x,y,live ):

    time = pygame.time.get_ticks()

    if time > 5000 and time < 7000:
        image = pygame.image.load(rto)
        p = pygame.transform.rotate(image, 180)
        p = pygame.transform.scale(p, (100, 100))
        screen.blit(p, (atak_1[0], atak_1[1]))

    if time > 7000 and time < 8000:
        image = pygame.image.load(xx)
        p = pygame.transform.rotate(image, 180)
        p = pygame.transform.scale(p, (100, 100))
        screen.blit(p, (atak_1[0], atak_1[1]))
        if atak_1[0] < x+5 < atak_1[1] + 100 and atak_1[1] < y+5 < atak_1[1] + 100 and atak_1[2]:
            live -= 100
            print(1)
            atak_1[2] = False




