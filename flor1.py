import pygame

from classs import *

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.RESIZABLE)


def bild_level_1(x, y, walls):
    img = pygame.image.load(plur_image)
    img = pygame.transform.scale(img, (plur_w, plur_h))
    screen.blit(img, (x, y))
    # wall image
    img = pygame.image.load(wall_image)
    img = pygame.transform.scale(img, (wall_w1, wall_h1))
    screen.blit(img, (walls[0].wall_x, walls[0].wall_y))

    img = pygame.image.load(wall_image)
    img = pygame.transform.scale(img, (wall_w2, wall_h2))
    screen.blit(img, (walls[1].wall_x, walls[1].wall_y))

    rect = pygame.Surface((500, 500))
    rect.set_alpha(50)
    rect.fill((0, 0, 0))
    screen.blit(rect, (0, 0))

    # player
    square = pygame.Rect(pos_x, pos_y, pleyer_width, pleyer_height)
    pygame.draw.rect(screen, color, square)


def limit(flur_x, flur_y, walls):
    # wall1
    print((walls[0].wall_x < pos_x < walls[0].wall_x + wall_w1) and (walls[0].wall_y < pos_y < walls[0].wall_y + wall_h1))

    if (walls[0].wall_x < pos_x < walls[0].wall_x + wall_w1) and (walls[0].wall_y < pos_y < walls[0].wall_y + wall_h1):
        walls[0].wall_y -= 10
        flur_y -= 10
        flur_x -= 10
        walls[0].wall_x -= 10
        walls[1].wall_x -= 10
        walls[1].wall_y -= 10
    elif (walls[0].wall_x < pos_x + pleyer_width < walls[0].wall_x + wall_w1) and (
            walls[0].wall_y < pos_y + pleyer_height < walls[0].wall_y + wall_h1):
        walls[0].wall_x += 10
        walls[0].wall_y += 10
        flur_x += 10
        flur_y += 10
        walls[1].wall_x += 10
        walls[1].wall_y += 10
    elif (walls[0].wall_x < pos_x < walls[0].wall_x + wall_w1) and (
            walls[0].wall_y < pos_y + pleyer_height < walls[0].wall_y + wall_h1):
        walls[0].wall_x -= 10
        walls[0].wall_y += 10
        flur_x -= 10
        flur_y += 10
        walls[1].wall_x -= 10
        walls[1].wall_y += 10
    elif (walls[0].wall_x < pos_x + pleyer_width < walls[0].wall_x + wall_w1) and (
            walls[0].wall_y < pos_y < walls[0].wall_y + wall_h1):
        walls[0].wall_x += 10
        walls[0].wall_y += 10
        flur_x += 10
        flur_y += 10
        walls[1].wall_x += 10
        walls[1].wall_y += 10
    # wall2
    elif (walls[1].wall_x < pos_x < walls[1].wall_x + wall_w2) and (walls[1].wall_y < pos_y < walls[1].wall_y + wall_h2):
        walls[1].wall_y -= 10
        flur_y -= 10
        flur_x -= 10
        walls[1].wall_x -= 10
        walls[0].wall_x -= 10
        walls[0].wall_y -= 10
    elif (walls[1].wall_x < pos_x + pleyer_width < walls[1].wall_x + wall_w2) and (walls[1].wall_y < pos_y + pleyer_height < walls[1].wall_y + wall_h2):
        walls[1].wall_x += 10
        walls[1].wall_y += 10
        flur_x += 10
        flur_y += 10
        walls[0].wall_x += 10
        walls[0].wall_y += 10
    elif (walls[0].wall_x < pos_x < walls[0].wall_x + wall_w2) and (walls[1].wall_y < pos_y + pleyer_height < walls[1].wall_y + wall_h2):
        walls[0].wall_x -= 10
        walls[0].wall_y += 10
        flur_x -= 10
        flur_y += 10
        walls[1].wall_x -= 10
        walls[1].wall_y += 10
    elif (walls[0].wall_x < pos_x + pleyer_width < walls[0].wall_x + wall_w2) and (walls[1].wall_y < pos_y < walls[1].wall_y + wall_h2):
        walls[1].wall_x += 10
        walls[1].wall_y += 10
        flur_x += 10
        flur_y += 10
        walls[0].wall_x += 10
        walls[0].wall_y += 10

    p = [flur_x, flur_y, walls]
    return p

# if ((wall_x < pos_x < wall_x + wall_w) and (wall_y < pos_y < wall_y + wall_h)):
#     wall_y -= 10
#     y -= 10
#     x -= 10
#     wall_x -= 10
# elif ((wall_x < pos_x + pleyer_width < wall_x + wall_w) and (wall_y < pos_y + pleyer_height < wall_y + wall_h)):
#     wall_x += 10
#     wall_y += 10
#     x += 10
#     y += 10
# elif ((wall_x < pos_x < wall_x + wall_w) and (wall_y < pos_y + pleyer_height < wall_y + wall_h)):
#     wall_x += 10
#     wall_y += 10
#     x += 10
#     y += 10
# elif ((wall_x < pos_x + pleyer_width < wall_x + wall_w) and (wall_y < pos_y < wall_y + wall_h)):
#     wall_x += 10
#     wall_y += 10
#     x += 10
#     y += 10


# if ((new_line.falt_line_x_s < pos_x < new_line.falt_line_x_f) and (
#         new_line.falt_line_y_s < pos_y < new_line.falt_line_y_f)):
#     wall_y -= 10
#     y -= 10
#     x -= 10
#     wall_x -= 10
#     print(123)
# elif ((new_line.falt_line_x_s < pos_x + pleyer_width < new_line.falt_line_x_f) and (
#         new_line.falt_line_y_s < pos_y + pleyer_height < new_line.falt_line_y_f)):
#     wall_x += 10
#     wall_y += 10
#     x += 10
#     y += 10
# elif ((new_line.falt_line_x_s < pos_x < new_line.falt_line_x_f) and (
#         new_line.falt_line_y_s < pos_y + pleyer_height < new_line.falt_line_y_f)):
#     wall_x += 10
#     wall_y += 10
#     x += 10
#     y += 10
# elif ((new_line.falt_line_x_s < pos_x + pleyer_width < new_line.falt_line_x_f) and (
#         new_line.falt_line_y_s < pos_y < new_line.falt_line_y_f)):
#     wall_x += 10
#     wall_y += 10
#     x += 10
#     y += 10
