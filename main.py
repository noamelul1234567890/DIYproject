import pygame
from classs import *
from flor1 import *
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

    flur_y = 0
    flur_x = 0

    wall1 = wall(0,-10,wall_w1,wall_h1)
    wall2 = wall(-10,0,wall_w2,wall_h2)
    wall3 = wall(600,-10,wall_w3,wall_h3)
    wall4 = wall(-10,600,wall_w4,wall_h4)



    walls = [wall1,wall2,wall3,wall4]







    # flat_line1 = wall(wall1_x, wall1_y, wall1_x + wall_w, wall1_y + wall_h)
    # lines_on_limit =[flat_line1]

    while not finish:

        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()

            if event.type == pygame.QUIT:
                finish = True

            if event.type == pygame.KEYUP:
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_DOWN:
                        flur_y -= 10
                        wall1.wall_y -= 10
                        wall2.wall_y -= 10
                        wall3.wall_y -= 10
                        wall4.wall_y -= 10
                    if event.key == pygame.K_UP:
                        flur_y += 10
                        wall1.wall_y += 10
                        wall2.wall_y += 10
                        wall3.wall_y += 10
                        wall4.wall_y += 10
                    if event.key == pygame.K_RIGHT:
                        flur_x -= 10
                        wall1.wall_x -= 10
                        wall2.wall_x -= 10
                        wall3.wall_x -= 10
                        wall4.wall_x -= 10
                    if event.key == pygame.K_LEFT:
                        flur_x += 10
                        wall1.wall_x += 10
                        wall2.wall_x += 10
                        wall3.wall_x += 10
                        wall4.wall_x += 10

                    wall_num = 1
                    p = limit(flur_x, flur_y, walls)
                    flur_x = p[0]
                    flur_y = p[1]
                    walls = p[2]


                    wall_num = 2
                    # p = limit(flur_x,flur_y,walls_x[2],walls_y[2])
                    # flur_x = p[0]
                    # flur_y = p[1]
                    # walls_x[2] = p[2]
                    # walls_y[2] = p[3]

                    pygame.display.flip()

                    # wall_x -= 10
                # if pos_x_p >= plur_w:
                #     x += 10
                #     wall_x += 10
                # if pos_y_p >= y:
                #     y += 10
                #     wall1_y += 10
                # if y <= plur_w:
                #     y += 10
                #     wall1_y += 10

            if event.type == pygame.MOUSEBUTTONDOWN:
                if ((start_buttons_x_pos <= pos[0] <= start_buttons_x_pos + start_buttons_width) and (
                        start_buttons_y_pos <= pos[1] <= start_buttons_y_pos + start_buttons_height)):
                    Screen_mode = 'game'

        if Screen_mode == 'opening':
            restart_opening_windows()

        elif Screen_mode == 'game':
            bild_level_1(flur_x, flur_y, walls)

        pygame.display.flip()
    pygame.quit()


main()
