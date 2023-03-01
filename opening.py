
from קבועים import *
import pygame
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.RESIZABLE)



def restart_opening_windows():
    img = pygame.image.load(start_background)
    img = pygame.transform.scale(img,(start_background_width, start_background_height))
    screen.blit(img, (start_background_x_pos, start_background_y_pos))

    square = pygame.Rect(x_pos, y_pos,
                         width, height)
    pygame.draw.rect(screen, color, square)
