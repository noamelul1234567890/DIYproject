import pygame
from קבועים import *
def print_kotzim():
    screen_size = (WINDOW_WIDTH, WINDOW_HEIGHT)
    screen = pygame.display.set_mode(screen_size)
    koz_1 = [-250, -350, 20, 20, False]
    pos_kozim = [koz_1]
    img1 = pygame.image.load(koz_of)
    img1 = pygame.transform.scale(img1, (50,50))
    for i in range(len(pos_kozim)):
        screen.blit(img1, (pos_kozim[i][0],pos_kozim[i][1]))
def kotzim(event):
    y = False
    koz_1 = [-250,-350, 0, 20, 20, False]
    pos_kozim= [koz_1]
    pygame.time.set_timer(pygame.USEREVENT, 5000)
    if event.type == pygame.USEREVENT:
        img1 = pygame.image.load(koz_on)
        img1 = pygame.transform.scale(img1, (50, 50))
        for i in range(5):
            screen.blit(img1, (pos_kozim[i][0], pos_kozim[i][1]))
        y = True
    return y








