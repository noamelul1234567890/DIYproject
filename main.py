import pygame
# from pygame.examples.cursors import surf
from start_and_end import end_2

from classs import *
from game import *
from opening import *
import random
from קבועים import *
from move import *
Screen_mode = 'opening'
x = 0
y = 0


def main():
    global screen, Screen_mode, event, pos, color, color

    screen_size = (WINDOW_WIDTH, WINDOW_HEIGHT)
    screen = pygame.display.set_mode(screen_size)
    pygame.init()
    finish = False

    flur_y = -350
    flur_x = -250
    x_door = -94
    y_door = -240

    levels_screen_x = 0
    levels_screen_y = 0
    levels_screen_w = 600
    levels_screen_h = 600

    levels_2_x = -600
    levels_2_y = -600
    levels_2 =[levels_2_x,levels_2_y]

    # walls of level 1
    wall1 = wall(-200, -360, wall_w1, wall_h1)
    wall2 = wall(-210, -350, wall_w2, wall_h2)
    wall3 = wall(400, -360, wall_w3, wall_h3)
    wall4 = wall(-210, 241, wall_w4, wall_h4)
    walls = [wall1, wall2, wall3, wall4]
    #coins
    print_coin_1 = True
    print_coin_2 = True
    coin_1 = [250,60,30,30,coin,print_coin_1]
    coin_2 = [-100,-100,30,30,coin,print_coin_2]
    num_of_coin = 0
    coins = [ num_of_coin,coin_1,coin_2]

    koz_1 = [0,0,20,20,False]
    kosim = [koz_1]



    pleyer_image = pleyer_1_image_up
    go_up = False
    go_down = False
    go_rite = False
    go_left = False

    steps_up = [step1,step2]
    steps_rite = [step3,step4]
    steps_down = [step5,step6]
    steps_left = [step7,step8]

    wall_001 = line_wall(200,130,200,200)
    walls_level_1 = [wall_001]

    while not finish:


        pygame.time.wait(10)

        if Screen_mode == 'level 1':
            limit(flur_x,flur_y,walls,coins,walls_level_1,Screen_mode,
                  levels_2,x_door,y_door)




        if go_down:
            for i in range(len(steps_down)):
                pleyer_image = steps_down[i]
                pygame.time.wait(1)
                if Screen_mode == 'level 1':
                    bild_level_1(1000, 1000, walls, pleyer_image, coins)
                    limit(flur_x, flur_y, walls, coins,walls_level_1,
                          Screen_mode,levels_2,x_door,y_door)
                if Screen_mode == 'level 2':
                    bild_level_2(pleyer_image)


                all_y_up(walls, flur_y, coins,walls_level_1,Screen_mode,
                         levels_2,y_door)
                color = pygame.Surface.get_at(screen, (pos_x + pleyer_width // 2, pos_y + pleyer_height - 7))
                if color == (0,0,0,255):
                    all_y_down(walls, flur_y, coins, walls_level_1,
                               Screen_mode,levels_2,y_door)
                    break
                if color == (149, 94, 39, 255):
                    Screen_mode = 'levels'
                    break
                pygame.display.flip()

        if go_up:
            for i in range(len(steps_up)):
                pleyer_image = steps_up[i]
                pygame.time.wait(1)
                if Screen_mode == 'level 1':
                    bild_level_1(1000, 1000, walls, pleyer_image, coins)
                    limit(flur_x, flur_y, walls, coins,walls_level_1,
                          Screen_mode,levels_2,x_door,y_door)
                if Screen_mode == 'level 2':
                    bild_level_2(pleyer_image)
                all_y_down(walls, flur_y, coins,walls_level_1,Screen_mode,levels_2,y_door)
                color = pygame.Surface.get_at(screen, (pos_x + pleyer_width // 2, pos_y +7))
                if color == (0,0,0,255):
                    all_y_up(walls, flur_y, coins, walls_level_1,Screen_mode,levels_2,y_door)
                    break
                if color == (149, 94, 39, 255):
                    Screen_mode = 'levels'
                    break
                pygame.display.flip()
        if go_rite:
            for i in range(len(steps_rite)):
                pleyer_image = steps_rite[i]
                pygame.time.wait(1)
                if Screen_mode == 'level 1':
                    bild_level_1(1000, 1000, walls, pleyer_image, coins)
                    limit(flur_x, flur_y, walls, coins,walls_level_1,
                          Screen_mode,levels_2,x_door,y_door)
                if Screen_mode == 'level 2':
                    bild_level_2(pleyer_image)
                all_x_left(walls, flur_x, coins,walls_level_1,Screen_mode,
                           levels_2,x_door)

                color = pygame.Surface.get_at(screen, (pos_x + pleyer_width - 7, pos_y + pleyer_height // 2))
                if color == (0,0,0,255):
                    all_x_rite(walls, flur_y, coins, walls_level_1,Screen_mode,levels_2,x_door)
                    break
                if color == (149, 94, 39, 255):
                    Screen_mode = 'levels'
                    break
                pygame.display.flip()

        if go_left:
            for i in range(len(steps_left)):
                pleyer_image = steps_left[i]
                pygame.time.wait(1)
                if Screen_mode == 'level 1':
                    bild_level_1(1000, 1000, walls, pleyer_image,coins)
                    limit(flur_x, flur_y, walls, coins,walls_level_1,
                          Screen_mode,levels_2,x_door,y_door)
                if Screen_mode == 'level 2':
                    bild_level_2(pleyer_image)
                all_x_rite(walls, flur_x, coins,walls_level_1,Screen_mode,levels_2,x_door)
                color = pygame.Surface.get_at(screen, (pos_x + 7, pos_y + pleyer_height // 2))
                if color == (0, 0, 0, 255):
                    all_x_left(walls, flur_y, coins, walls_level_1,Screen_mode,levels_2,x_door)
                    break
                if color == (149, 94, 39, 255):
                    Screen_mode = 'levels'
                    break

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
                p = limit(flur_x, flur_y, walls,coins,walls_level_1,
                          Screen_mode,levels_2,x_door,y_door)
                flur_x = p[0]
                flur_y = p[1]
                walls = p[2]
                num_of_coin = p[3]




                pygame.display.flip()



            if event.type == pygame.MOUSEBUTTONDOWN:
                if ((start_buttons_x_pos <= pos[0] <= start_buttons_x_pos + start_buttons_width) and (
                        start_buttons_y_pos <= pos[1] <= start_buttons_y_pos + start_buttons_height)):
                    Screen_mode = 'levels'





        if Screen_mode == 'opening':
            restart_opening_windows()

        elif Screen_mode == 'levels':
            levels_screen(levels_screen_x,levels_screen_y,levels_screen_w,levels_screen_h)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if (30 <= pos[0] <= 90) and (30 <= pos[1] <= 90):
                    Screen_mode = 'level 1'

                if (30+90 <= pos[0] <= 90+90) and (30 <= pos[1] <= 90):
                    Screen_mode = 'level 2'

                if (30 <= pos[0] <= 130) and (400 <= pos[1] <= 460):
                    Screen_mode = 'opening'


        elif Screen_mode == 'level 1':
            bild_level_1(flur_x, flur_y, walls,pleyer_image,coins)
            color = pygame.Surface.get_at(screen,(100,100))

        elif Screen_mode == 'level 2':
            levels_screen(levels_screen_x,levels_screen_y,levels_screen_w,levels_screen_h)
            bild_level_2(pleyer_image)








        pygame.display.flip()
    pygame.quit()


main()
