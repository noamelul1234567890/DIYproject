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

    line_1 = (80,197,348,197)
    liness = [line_1]




    if Screen_mode == 'level 1':
        w_1 = wall(141,11,0,69)
        # wall_level_1 = [w_1]
    pleyer_image = pleyer_1_image_up
    go_up = False
    go_down = False
    go_rite = False
    go_left = False
    steps_up = [step1,step2]
    steps_rite = [step3,step4]
    steps_down = [step5,step6]
    steps_left = [step7,step8]

    while not finish:
        pygame.time.wait(10)










        limit(flur_x,flur_y,walls)
        # lines(liness, walls, flur_y, flur_x)
        if go_down:
            for i in range(len(steps_down)):
                pleyer_image = steps_down[i]
                pygame.time.wait(50)
                bild_level_1(1000, 1000, walls, pleyer_image)
                flur_y -= 5
                wall1.wall_y -= 5
                wall2.wall_y -= 5
                wall3.wall_y -= 5
                wall4.wall_y -= 5
                pygame.display.flip()

        if go_up:
            for i in range(len(steps_up)):
                pleyer_image = steps_up[i]
                pygame.time.wait(50)
                bild_level_1(1000,1000,walls,pleyer_image)
                flur_y += 5
                wall1.wall_y += 5
                wall2.wall_y += 5
                wall3.wall_y += 5
                wall4.wall_y += 5
                pygame.display.flip()
        if go_rite:
            for i in range(len(steps_rite)):
                pleyer_image = steps_rite[i]
                pygame.time.wait(50)
                bild_level_1(1000, 1000, walls, pleyer_image)
                flur_y -= 5
                wall1.wall_x -= 5
                wall2.wall_x -= 5
                wall3.wall_x -= 5
                wall4.wall_x -= 5
                pygame.display.flip()

        if go_left:
            for i in range(len(steps_left)):
                pleyer_image = steps_left[i]
                pygame.time.wait(50)
                bild_level_1(1000, 1000, walls, pleyer_image)
                flur_y += 5
                wall1.wall_x += 5
                wall2.wall_x += 5
                wall3.wall_x += 5
                wall4.wall_x += 5
                pygame.display.flip()



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
