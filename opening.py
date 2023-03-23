
from קבועים import *
import pygame
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.RESIZABLE)



def restart_opening_windows():
    img = pygame.image.load(start_background)
    img = pygame.transform.scale(img,(start_background_width, start_background_height))
    screen.blit(img, (start_background_x_pos, start_background_y_pos))

    square = pygame.Rect(start_buttons_x_pos, start_buttons_y_pos, start_buttons_width, start_buttons_height)
    pygame.draw.rect(screen, COLOR, square)

    font = pygame.font.SysFont('Aharoni', start_text_size)
    text = font.render(start_text_m, True, color)
    screen.blit(text, [start_text_x_pos, start_text_y_pos])

    square = pygame.Rect(shop_buttons_x_pos, shop_buttons_y_pos, shop_buttons_width, shop_buttons_height)
    pygame.draw.rect(screen, COLOR, square)

    font = pygame.font.SysFont('Aharoni', start_text_size)
    text = font.render('shop', True, color)
    screen.blit(text, [shop_buttons_x_pos+5, shop_buttons_y_pos+5])
