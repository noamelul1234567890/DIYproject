import pygame
from pygame import Color

from move import *
from classs import *

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.RESIZABLE)


def bild_level_1(x, y, walls, pleyer_image, coins):
    img = pygame.image.load(plur_image)
    img = pygame.transform.scale(img, (plur_w, plur_h))
    screen.blit(img, (walls[0].wall_x, walls[0].wall_y))
    # wall image
    img = pygame.image.load(wall_image)
    img = pygame.transform.scale(img, (wall_w1, wall_h1))
    screen.blit(img, (walls[0].wall_x, walls[0].wall_y))

    img = pygame.image.load(wall_image)
    img = pygame.transform.scale(img, (wall_w2, wall_h2))
    screen.blit(img, (walls[1].wall_x, walls[1].wall_y))

    img = pygame.image.load(wall_image)
    img = pygame.transform.scale(img, (wall_w3, wall_h3))
    screen.blit(img, (walls[2].wall_x, walls[2].wall_y))

    img = pygame.image.load(wall_image)
    img = pygame.transform.scale(img, (wall_w4, wall_h4))
    screen.blit(img, (walls[3].wall_x, walls[3].wall_y))
    for i in range(1,len(coins)):
        if coins[i][5]:
            img = pygame.image.load(coins[i][4])
            img = pygame.transform.scale(img, (coins[i][2], coins[i][3]))
            screen.blit(img, (coins[i][0], coins[i][1]))

    print_score()

    font = pygame.font.Font(None, 36)
    text = font.render("coins:  {}".format(coins[0]), True, (0, 0, 0))
    screen.blit(text, (10, 10))

    rect = pygame.Surface((500, 500))
    rect.set_alpha(50)
    rect.fill((0, 0, 0))
    screen.blit(rect, (0, 0))

    # player

    img = pygame.image.load(pleyer_image)
    img = pygame.transform.scale(img,(pleyer_width, pleyer_height))
    screen.blit(img, (pos_x, pos_y))


def limit(flur_x, flur_y, walls, coins,walls_level_1):
    # wall1
    pygame.time.wait(20)
    # walls_in_level_1(walls_level_1,flur_x, flur_y, walls,coins)
    if (walls[0].wall_x < pos_x < walls[0].wall_x + wall_w1) and (walls[0].wall_y < pos_y < walls[0].wall_y + wall_h1):
        all_y_up(walls, flur_y, coins,walls_level_1)
    elif (walls[0].wall_x < pos_x + pleyer_width < walls[0].wall_x + wall_w1) and (
            walls[0].wall_y < pos_y + pleyer_height < walls[0].wall_y + wall_h1):
        all_y_down(walls, flur_y, coins,walls_level_1)
    elif (walls[0].wall_x < pos_x < walls[0].wall_x + wall_w1) and (
            walls[0].wall_y < pos_y + pleyer_height < walls[0].wall_y + wall_h1):
        all_y_down(walls, flur_y, coins,walls_level_1)
    elif (walls[0].wall_x < pos_x + pleyer_width < walls[0].wall_x + wall_w1) and (
            walls[0].wall_y < pos_y < walls[0].wall_y + wall_h1):
        all_y_down(walls, flur_y, coins,walls_level_1)

    # wall2
    elif (walls[1].wall_x < pos_x < walls[1].wall_x + wall_w2) and (
            walls[1].wall_y < pos_y < walls[1].wall_y + wall_h2):
        all_x_left(walls, flur_x, coins,walls_level_1)
    elif (walls[1].wall_x < pos_x + pleyer_width < walls[1].wall_x + wall_w2) and (
            walls[1].wall_y < pos_y + pleyer_height < walls[1].wall_y + wall_h2):
        all_x_rite(walls, flur_x, coins,walls_level_1)
    elif (walls[1].wall_x < pos_x < walls[1].wall_x + wall_w2) and (
            walls[1].wall_y < pos_y + pleyer_height < walls[1].wall_y + wall_h2):
        all_x_left(walls, flur_x, coins,walls_level_1)
    elif (walls[0].wall_x < pos_x + pleyer_width < walls[0].wall_x + wall_w2) and (
            walls[1].wall_y < pos_y < walls[1].wall_y + wall_h2):
        all_x_rite(walls, flur_x, coins,walls_level_1)

    # wall3
    elif (walls[2].wall_x < pos_x < walls[2].wall_x + wall_w3) and (walls[2].wall_y < pos_y < walls[2].wall_y + wall_h3):
        all_x_rite(walls, flur_x, coins,walls_level_1)
    elif (walls[2].wall_x < pos_x + pleyer_width < walls[2].wall_x + wall_w3) and (
            walls[2].wall_y < pos_y + pleyer_height < walls[2].wall_y + wall_h3):
        all_x_rite(walls, flur_x, coins,walls_level_1)
    elif (walls[2].wall_x < pos_x < walls[2].wall_x + wall_w3) and (
            walls[2].wall_y < pos_y + pleyer_height < walls[2].wall_y + wall_h3):
        all_x_rite(walls, flur_x, coins,walls_level_1)
    elif (walls[2].wall_x < pos_x + pleyer_width < walls[2].wall_x + wall_w3) and (
            walls[2].wall_y < pos_y < walls[2].wall_y + wall_h3):
        all_x_rite(walls, flur_x, coins,walls_level_1)

    # wall4
    # wall2
    elif (walls[3].wall_x < pos_x < walls[3].wall_x + wall_w4) and (
            walls[3].wall_y < pos_y < walls[3].wall_y + wall_h4):

        all_y_down(walls, flur_y, coins,walls_level_1)
    elif (walls[3].wall_x < pos_x + pleyer_width < walls[3].wall_x + wall_w4) and (
            walls[3].wall_y < pos_y + pleyer_height < walls[3].wall_y + wall_h4):
        all_y_down(walls, flur_y, coins,walls_level_1)
    elif (walls[3].wall_x < pos_x < walls[3].wall_x + wall_w4) and (
            walls[3].wall_y < pos_y + pleyer_height < walls[3].wall_y + wall_h4):
        all_y_down(walls, flur_y, coins,walls_level_1)
    elif (walls[3].wall_x < pos_x + pleyer_width < walls[3].wall_x + wall_w4) and (
            walls[3].wall_y < pos_y < walls[3].wall_y + wall_h4):
        all_y_down(walls, flur_y, coins,walls_level_1)

    # coin_1

    if (coins[1][0] < pos_x + pleyer_width // 2 < coins[1][0] + coins[1][2]) and (
            coins[1][1] < pos_x + pleyer_height // 2 < coins[1][1] + coins[1][3]):
        if coins[1][5]:
            coins[1][5] = False
            coins[0] += 1
    if (coins[2][0] < pos_x + pleyer_width // 2 < coins[2][0] + coins[2][2]) and (
                coins[2][1] < pos_x + pleyer_height // 2 < coins[2][1] + coins[2][3]):
        if coins[2][5]:
            coins[2][5] = False
            coins[0] += 1

    p = [flur_x, flur_y, walls,coins[0]]
    return p


# def walls_in_level_1(walls_level_1,flur_x, flur_y, walls,coins):
#
#
#         print(1)
#         all_x_left(walls, flur_x, coins,walls_level_1)
#         all_y_up(walls, flur_y, coins,walls_level_1)







def print_score():
    square = pygame.Rect(0, 0,1000, 50)
    pygame.draw.rect(screen, (100,100,100), square)




