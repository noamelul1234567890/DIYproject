import pygame

from classs import *

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.RESIZABLE)


def bild_level_1(x, y, walls,pleyer_image,):
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

    rect = pygame.Surface((500, 500))
    rect.set_alpha(50)
    rect.fill((0, 0, 0))
    screen.blit(rect, (0, 0))



    # player


    img = pygame.image.load(pleyer_image)
    img = pygame.transform.scale(img,
                                 (pleyer_width, pleyer_height))
    screen.blit(img, (pos_x, pos_y))



def limit(flur_x, flur_y, walls):
    # wall1
    pygame.time.wait(20)

    if (walls[0].wall_x < pos_x < walls[0].wall_x + wall_w1) and (walls[0].wall_y < pos_y < walls[0].wall_y + wall_h1):
        walls[0].wall_y -= 5
        flur_y -= 5
        walls[1].wall_y -= 5
        walls[2].wall_y -= 5
        walls[3].wall_y -= 5
    elif (walls[0].wall_x < pos_x + pleyer_width < walls[0].wall_x + wall_w1) and (walls[0].wall_y < pos_y + pleyer_height < walls[0].wall_y + wall_h1):
        walls[0].wall_y += 5
        flur_y += 5
        walls[1].wall_y += 5
        walls[2].wall_y += 5
        walls[3].wall_y += 5
    elif (walls[0].wall_x < pos_x < walls[0].wall_x + wall_w1) and (walls[0].wall_y < pos_y + pleyer_height < walls[0].wall_y + wall_h1):
        walls[0].wall_y += 5
        flur_y += 5
        walls[1].wall_y += 5
        walls[2].wall_y += 5
        walls[3].wall_y += 5
    elif (walls[0].wall_x < pos_x + pleyer_width < walls[0].wall_x + wall_w1) and (walls[0].wall_y < pos_y < walls[0].wall_y + wall_h1):
        walls[0].wall_y += 5
        flur_y += 5
        walls[1].wall_y += 5
        walls[2].wall_y += 5
        walls[3].wall_y += 5
    # wall2
    elif (walls[1].wall_x < pos_x < walls[1].wall_x + wall_w2) and (walls[1].wall_y < pos_y < walls[1].wall_y + wall_h2):
        flur_x -= 5
        walls[1].wall_x -= 5
        walls[0].wall_x -= 5
        walls[2].wall_x -= 5
        walls[3].wall_x -= 5
    elif (walls[1].wall_x < pos_x + pleyer_width < walls[1].wall_x + wall_w2) and (walls[1].wall_y < pos_y + pleyer_height < walls[1].wall_y + wall_h2):
        wall_x_p(walls,flur_x)
    elif (walls[1].wall_x < pos_x < walls[1].wall_x + wall_w2) and (walls[1].wall_y < pos_y + pleyer_height < walls[1].wall_y + wall_h2):
        walls[0].wall_x -= 5
        flur_x -= 5
        walls[1].wall_x -= 5
        walls[2].wall_x -= 5
        walls[3].wall_x -= 5
    elif (walls[0].wall_x < pos_x + pleyer_width < walls[0].wall_x + wall_w2) and (walls[1].wall_y < pos_y < walls[1].wall_y + wall_h2):
        wall_x_p(walls, flur_x)

#wall3
    if (walls[2].wall_x < pos_x < walls[2].wall_x + wall_w3) and (walls[2].wall_y < pos_y < walls[2].wall_y + wall_h3):
        wall_x_p(walls,flur_x)
    elif (walls[2].wall_x < pos_x + pleyer_width < walls[2].wall_x + wall_w3) and (walls[2].wall_y < pos_y + pleyer_height < walls[2].wall_y + wall_h3):
        wall_x_p(walls, flur_x)
    elif (walls[2].wall_x < pos_x < walls[2].wall_x + wall_w3) and (walls[2].wall_y < pos_y + pleyer_height < walls[2].wall_y + wall_h3):
        wall_x_p(walls,flur_x)
    elif (walls[2].wall_x < pos_x + pleyer_width < walls[2].wall_x + wall_w3) and (walls[2].wall_y < pos_y < walls[2].wall_y + wall_h3):
        wall_x_p(walls,flur_x)

#wall4
        # wall2
    elif (walls[3].wall_x < pos_x < walls[3].wall_x + wall_w4) and (walls[3].wall_y < pos_y < walls[3].wall_y + wall_h4):

        walls[0].wall_y += 5
        flur_y += 5
        walls[1].wall_y += 5
        walls[2].wall_y += 5
        walls[3].wall_y += 5
    elif (walls[3].wall_x < pos_x + pleyer_width < walls[3].wall_x + wall_w4) and (walls[3].wall_y < pos_y + pleyer_height < walls[3].wall_y + wall_h4):
        walls[0].wall_y += 5
        flur_y += 5
        walls[1].wall_y += 5
        walls[2].wall_y += 5
        walls[3].wall_y += 5
    elif (walls[3].wall_x < pos_x < walls[3].wall_x + wall_w4) and (walls[3].wall_y < pos_y + pleyer_height < walls[3].wall_y + wall_h4):
        walls[0].wall_y += 5
        flur_y += 5
        walls[1].wall_y += 5
        walls[2].wall_y += 5
        walls[3].wall_y += 5
    elif (walls[3].wall_x < pos_x + pleyer_width < walls[3].wall_x + wall_w4) and (walls[3].wall_y < pos_y < walls[3].wall_y + wall_h4):
        walls[0].wall_y += 5
        flur_y += 5
        walls[1].wall_y += 5
        walls[2].wall_y += 5
        walls[3].wall_y += 5



    p = [flur_x, flur_y, walls]
    return p

def wall_x_p(walls,flur_x):
    walls[1].wall_x += 5
    flur_x += 5
    walls[0].wall_x += 5
    walls[2].wall_x += 5
    walls[3].wall_x += 5


def walls_in_level_1(walls_level_1):
    if (walls_level_1[0].wall_x < pos_x < walls_level_1[0].wall_x + wall_w1) and (walls_level_1[0].wall_y < pos_y < walls_level_1[0].wall_y + wall_h1):
        # walls_level_1[0].wall_y -= 5
        print(1)

# def lines(lines,walls,flur_y,flur_x):
#     if (lines[0].x_start < pos_x < lines[0].x_end) and (lines[0].y_start < pos_y < lines[0].y_end):
#         lines[0].y_start -= 5
#         walls[0].wall_y -= 5
#         flur_y -= 5
#         walls[1].wall_y -= 5
#         walls[2].wall_y -= 5
#         walls[3].wall_y -= 5
