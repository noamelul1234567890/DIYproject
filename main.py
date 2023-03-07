import pygame
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

    flur_y = -350
    flur_x = -250

    wall1 = wall(-250, -360, wall_w1, wall_h1)
    wall2 = wall(-260, -350, wall_w2, wall_h2)
    wall3 = wall(350, -360, wall_w3, wall_h3)
    wall4 = wall(-260, 250, wall_w4, wall_h4)
    walls = [wall1, wall2, wall3, wall4]

    if Screen_mode == 'level 1':
        w_1 = wall(141,11,0,69)
        # wall_level_1 = [w_1]
    pleyer_image = pleyer_1_image_up
    go_up = False
    go_down = False
    go_rite = False
    go_left = False
    steps = [step1,step2]

    while not finish:
        limit(flur_x,flur_y,walls)
        if go_down:
            pleyer_image = pleyer_1_image_dound
            flur_y -= 10
            wall1.wall_y -= 10
            wall2.wall_y -= 10
            wall3.wall_y -= 10
            wall4.wall_y -= 10
        if go_up:
            pleyer_image = pleyer_1_image_up
            # for i in range(len(steps)):
            #     pleyer_image = steps[i]
            #     bild_level_1(1000,1000,walls,pleyer_image)
            #     pygame.time.wait(10)
            flur_y += 10
            wall1.wall_y += 10
            wall2.wall_y += 10
            wall3.wall_y += 10
            wall4.wall_y += 10
            # pygame.display.flip()
        if go_rite:
            pleyer_image = pleyer_1_image_left
            flur_x -= 10
            wall1.wall_x -= 10
            wall2.wall_x -= 10
            wall3.wall_x -= 10
            wall4.wall_x -= 10
        if go_left:
            pleyer_image = pleyer_1_image_rire
            flur_x += 10
            wall1.wall_x += 10
            wall2.wall_x += 10
            wall3.wall_x += 10
            wall4.wall_x += 10

        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()


            if event.type == pygame.QUIT:
                finish = True
            if event.type == pygame.KEYUP:

                go_up = False
                go_down = False
                go_rite = False
                go_left = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    go_down = True
                if event.key == pygame.K_UP:
                    go_up = True
                if event.key == pygame.K_RIGHT:
                    go_rite = True
                if event.key == pygame.K_LEFT:
                    go_left = True







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



            if event.type == pygame.MOUSEBUTTONDOWN:
                if ((start_buttons_x_pos <= pos[0] <= start_buttons_x_pos + start_buttons_width) and (
                        start_buttons_y_pos <= pos[1] <= start_buttons_y_pos + start_buttons_height)):
                    Screen_mode = 'level 1'

        if Screen_mode == 'opening':
            restart_opening_windows()

        elif Screen_mode == 'level 1':
            bild_level_1(flur_x, flur_y, walls,pleyer_image)

        pygame.display.flip()
    pygame.quit()


main()
