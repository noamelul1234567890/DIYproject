import pygame

from game import *
from opening import *
import random
from קבועים import *

Screen_mode = 'opening'
x = 0
y = 0

def main():
    global screen, Screen_mode
    screen_size = (WINDOW_WIDTH, WINDOW_HEIGHT)
    screen = pygame.display.set_mode(screen_size)
    pygame.init()
    finish = False
    y = 0
    x = 0
    wall_x = 100
    wall_y = 0




    while not finish:

        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()

            if event.type == pygame.QUIT:
                finish = True

            if event.type == pygame.KEYUP:
                go_in_rezef = False
                while go_in_rezef:
                    if event.type == pygame.KEYUP:
                        if event.key == pygame.K_DOWN:
                            y -= 10
                            wall_y -= 10
                        if event.key == pygame.K_UP:
                            y += 10
                            wall_y += 10
                        if event.key == pygame.K_RIGHT:
                            x -= 10
                            wall_x -= 10
                        if event.key == pygame.K_LEFT:
                            x += 10
                            wall_x += 10

                        p = get_limit(x,y,wall_x,wall_y)
                        x = p[0]
                        y = p[1]
                        wall_x = p[2]
                        wall_y = p[3]
                        pygame.display.flip()






                    # wall_x -= 10
                # if pos_x_p >= plur_w:
                #     x += 10
                #     wall_x += 10
                # if pos_y_p >= y:
                #     y += 10
                #     wall_y += 10
                # if y <= plur_w:
                #     y += 10
                #     wall_y += 10




            if event.type == pygame.MOUSEBUTTONDOWN:
                if ((start_buttons_x_pos <= pos[0] <= start_buttons_x_pos + start_buttons_width) and (
                        start_buttons_y_pos <= pos[1] <= start_buttons_y_pos + start_buttons_height)):
                    Screen_mode = 'game'



        if Screen_mode == 'opening':
            restart_opening_windows()

        elif Screen_mode == 'game':
            game(x, y,wall_x,wall_y)

        pygame.display.flip()
    pygame.quit()
main()
