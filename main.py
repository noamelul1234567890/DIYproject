import pygame
from start_and_end import end_2
from classs import *
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

    flore_y = FLORE_Y
    flore_x = FLORE_X


    wall1 = wall(-250, -360, wall_w1, wall_h1)
    wall2 = wall(-260, -350, wall_w2, wall_h2)
    wall3 = wall(350, -360, wall_w3, wall_h3)
    wall4 = wall(-260, 250, wall_w4, wall_h4)
    walls = [wall1, wall2, wall3, wall4]

    if Screen_mode == 'level 1':
        w_1 = wall(141,11,0,69)
        # wall_level_1 = [w_1]
    if Screen_mode == 'level 2':
        w_1 = wall(141, 11, 0, 69)


    pleyer_image = pleyer_1_image_up



    while not finish:
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                finish = True
            if event.type == pygame.KEYUP:
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_DOWN:
                        pleyer_image = pleyer_1_image_dound
                        flore_y -= 10
                        wall1.wall_y -= 10
                        wall2.wall_y -= 10
                        wall3.wall_y -= 10
                        wall4.wall_y -= 10

                    if event.key == pygame.K_UP:
                        pleyer_image = pleyer_1_image_up
                        flore_y += 10
                        wall1.wall_y += 10
                        wall2.wall_y += 10
                        wall3.wall_y += 10
                        wall4.wall_y += 10

                    if event.key == pygame.K_RIGHT:
                        pleyer_image = pleyer_1_image_left
                        flore_x -= 10
                        wall1.wall_x -= 10
                        wall2.wall_x -= 10
                        wall3.wall_x -= 10
                        wall4.wall_x -= 10

                    if event.key == pygame.K_LEFT:
                        pleyer_image = pleyer_1_image_rire
                        flore_x += 10
                        wall1.wall_x += 10
                        wall2.wall_x += 10
                        wall3.wall_x += 10
                        wall4.wall_x += 10


                    wall_num = 1
                    p = limit(flore_x, flore_y, walls)
                    flore_x = p[0]
                    flore_y = p[1]
                    walls = p[2]

                    wall_num = 2
                    # p = limit(flur_x,flur_y,walls_x[2],walls_y[2])
                    # flur_x = p[0]
                    # flur_y = p[1]
                    # walls_x[2] = p[2]
                    # walls_y[2] = p[3]
                    the_end = end_2(flore_x,flore_y)
                    if the_end:
                        Screen_mode = 'level 2'
                        main()

                        pygame.display.flip()



            if event.type == pygame.MOUSEBUTTONDOWN:
                if ((start_buttons_x_pos <= pos[0] <= start_buttons_x_pos + start_buttons_width) and (
                        start_buttons_y_pos <= pos[1] <= start_buttons_y_pos + start_buttons_height)):
                    Screen_mode = 'level 1'

        if Screen_mode == 'opening':
            restart_opening_windows()

        elif Screen_mode == 'level 1':
            bild_level_1(flore_x, flore_y, walls,pleyer_image)


        pygame.display.flip()
    pygame.quit()


main()
