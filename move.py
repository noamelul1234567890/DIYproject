
def all_x_rite(walls, flur_x, coins,walls_level_1,Screen_mode,levels_2,x_door):
    if Screen_mode == 'level 1':
        walls[1].wall_x += 3
        flur_x += 3
        x_door +=3
        walls[0].wall_x += 3
        walls[2].wall_x += 3
        walls[3].wall_x += 3
        coins[1][0] += 3
        coins[2][0] += 3
        walls_level_1[0].x_start +=3
        walls_level_1[0].x_end += 3
    elif Screen_mode == 'level 2':
        levels_2[0] += 3


def all_x_left(walls, flur_x, coins,walls_level_1,Screen_mode,levels_2,
               door_x):
    if Screen_mode == 'level 1':
        walls[1].wall_x -= 3
        flur_x -= 3
        door_x -= 3
        walls[0].wall_x -= 3
        walls[2].wall_x -= 3
        walls[3].wall_x -= 3
        coins[1][0] -= 3
        coins[2][0] -= 3
        walls_level_1[0].x_start -= 3
        walls_level_1[0].x_end -= 3
    elif Screen_mode == 'level 2':
        levels_2[0] -= 3


def all_y_up(walls, flur_y, coins,walls_level_1,Screen_mode,levels_2,y_door):
    if Screen_mode == 'level 1':
        walls[1].wall_y -= 3
        flur_y -= 3
        y_door -= 3
        walls[0].wall_y -= 3
        walls[2].wall_y -= 3
        walls[3].wall_y -= 3
        coins[1][1] -= 3
        coins[2][1] -= 3
        walls_level_1[0].y_start -= 3
        walls_level_1[0].y_end -= 3
    elif Screen_mode == 'level 2':
        levels_2[1] -= 3

def all_y_down(walls, flur_y, coins,walls_level_1,Screen_mode,levels_2,y_door):
    if Screen_mode == 'level 1':
        walls[1].wall_y += 3
        flur_y += 3
        y_door += 3
        walls[0].wall_y += 3
        walls[2].wall_y += 3
        walls[3].wall_y += 3
        coins[1][1] += 3
        coins[2][1] += 3
        walls_level_1[0].y_start += 3
        walls_level_1[0].y_end += 3
    elif Screen_mode == 'level 2':
        levels_2[1] += 3

