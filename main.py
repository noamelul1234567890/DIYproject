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
        w_1 = wall(141, 11, 0, 69)
        # wall_level_1 = [w_1]
    pleyer_image = pleyer_1_image_up
    go_left =  False
    go_down = False
    steps_down = [step1,step2]
    go_up = False
    go_rite = False

    while not finish:

        if go_down:

            flur_y -= 5
            wall1.wall_y -= 5
            wall2.wall_y -= 5
            wall3.wall_y -= 5
            wall4.wall_y -= 5
            pleyer_image = pleyer_1_image_dound
        if go_up:
            for i in range(2):
                pygame.time.wait(10)
                limit(flur_x, flur_y, walls)
                pleyer_image = steps_down[i]
                bild_level_1(flur_x,flur_y,walls,pleyer_image)
                pygame.display.flip()
                flur_y += 5
                wall1.wall_y += 5
                wall2.wall_y += 5
                wall3.wall_y += 5
                wall4.wall_y += 5
        if go_rite:
            pleyer_image = pleyer_1_image_left
            flur_x -= 5
            wall1.wall_x -= 5
            wall2.wall_x -= 5
            wall3.wall_x -= 5
            wall4.wall_x -= 5
        if go_left:
            pleyer_image = pleyer_1_image_rire
            flur_x += 5
            wall1.wall_x += 5
            wall2.wall_x += 5
            wall3.wall_x += 5
            wall4.wall_x += 5

        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()

            if event.type == pygame.QUIT:
                finish = True

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_DOWN:
                    go_down = True
                if event.key == pygame.K_UP:
                    go_up = True
                if event.key == pygame.K_RIGHT:
                    go_rite = True
                if event.key == pygame.K_LEFT:
                    go_left = True
            if event.type == pygame.KEYUP:
                go_left = False
                go_down = False
                go_up = False
                go_rite = False








                p = limit(flur_x, flur_y, walls)
                flur_x = p[0]
                flur_y = p[1]
                walls = p[2]



                pygame.display.flip()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if ((start_buttons_x_pos <= pos[0] <= start_buttons_x_pos + start_buttons_width) and (
                        start_buttons_y_pos <= pos[1] <= start_buttons_y_pos + start_buttons_height)):
                    Screen_mode = 'level 1'

        if Screen_mode == 'opening':
            restart_opening_windows()

        elif Screen_mode == 'level 1':
            bild_level_1(flur_x, flur_y, walls, pleyer_image)

        pygame.display.flip()
    pygame.quit()


main()
