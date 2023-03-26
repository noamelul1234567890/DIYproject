import pygame

from opening import screen


def bose_atak():
    atak = 'first'
    atak_1 = [0, 0, False]

    if atak == 'first':
        square = pygame.Rect(atak_1[0], atak_1[1], 100, 100)
        pygame.draw.rect(screen, (0, 0, 0), square)



