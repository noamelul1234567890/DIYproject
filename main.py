import pygame
from opening import *
import random
from קבועים import *

Screen_mode = 'opening'


def main():
    global screen
    screen_size = (WINDOW_WIDTH, WINDOW_HEIGHT)
    screen = pygame.display.set_mode(screen_size)
    pygame.init()
    finish = False

    while not finish:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finish = True

        if Screen_mode == 'opening':
            restart_opening_windows()












        pygame.display.flip()
    pygame.quit()
main()
