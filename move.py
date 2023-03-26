

from קבועים import *

def all_x_rite(walls, flur_x, coins, walls_level_1, Screen_mode, levels_2, anemy,speed_a,shoot_Valuable):
    if Screen_mode == 'level 1':
        walls[1].wall_x += 3
        flur_x += 3
        # x_door +=3
        walls[0].wall_x += 3
        walls[2].wall_x += 3
        walls[3].wall_x += 3
        coins[1][0] += 3
        coins[2][0] += 3
        walls_level_1[0].x_start +=3
        walls_level_1[0].x_end += 3
    elif Screen_mode == 'level 2':
        levels_2[0] += 3

        for i in range(len(anemy)):
            anemy[i].x_pos += speed+speed_a
            anemy[i].x_max += speed+speed_a
            anemy[i].x_min += speed+speed_a
    if Screen_mode == 'level 2':
        levels_2[0] += speed


def all_x_left(walls, flur_x, coins,walls_level_1,Screen_mode,levels_2,animals,speed_a,shoot_Valuable):
    if Screen_mode == 'level 1':
        shoot_Valuable[0] -= speed + speed_a
        walls[1].wall_x -= speed+speed_a
        flur_x -= speed+speed_a
        walls[0].wall_x -= speed+speed_a
        walls[2].wall_x -= speed+speed_a
        walls[3].wall_x -= speed+speed_a
        coins[1][0] -= speed+speed_a
        coins[2][0] -= speed+speed_a
        walls_level_1[0].x_start -= speed+speed_a
        walls_level_1[0].x_end -= speed+speed_a
        for i in range(len(animals)):
            animals[i].x_pos -= speed + speed_a
            animals[i].x_max -= speed + speed_a
            animals[i].x_min -= speed + speed_a
    if Screen_mode == 'level 2':
        levels_2[0] -= speed+speed_a

def all_y_up(walls, flur_y, coins,walls_level_1,Screen_mode,levels_2,animals,speed_a,shoot_Valuable):
    if Screen_mode == 'level 1':
        shoot_Valuable[1] -= speed + speed_a
        walls[1].wall_y -= speed+speed_a
        flur_y -= speed+speed_a
        walls[0].wall_y -= speed+speed_a
        walls[2].wall_y -= speed+speed_a
        walls[3].wall_y -= speed+speed_a
        coins[1][1] -= speed+speed_a
        coins[2][1] -= speed+speed_a

        walls_level_1[0].y_start -= speed+speed_a
        walls_level_1[0].y_end -= speed+speed_a
        animals[0].y_pos -= speed+speed_a
        animals[1].y_pos -= speed+speed_a
        animals[2].y_pos -= speed+speed_a
    if Screen_mode == 'level 2':
        levels_2[1] -= speed+speed_a

def all_y_down(walls, flur_y, coins,walls_level_1,Screen_mode,levels_2,animals,speed_a,shoot_Valuable):
    if Screen_mode == 'level 1':
        shoot_Valuable[1] += speed + speed_a
        walls[1].wall_y += speed+speed_a
        flur_y += speed+speed_a
        walls[0].wall_y += speed+speed_a
        walls[2].wall_y += speed+speed_a
        walls[3].wall_y += speed+speed_a
        coins[1][1] += speed+speed_a
        coins[2][1] += speed+speed_a

        walls_level_1[0].y_start += speed+speed_a
        walls_level_1[0].y_end += speed+speed_a
        animals[0].y_pos += speed+speed_a
        animals[1].y_pos += speed+speed_a
        animals[2].y_pos += speed+speed_a
    if Screen_mode == 'level 2':
        levels_2[1] += speed+speed_a

