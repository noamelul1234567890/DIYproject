from קבועים import *
import pygame

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.RESIZABLE)


def game(x, y, wall_x, wall_y):
    img = pygame.image.load(plur_image)
    img = pygame.transform.scale(img, (plur_w, plur_h))
    screen.blit(img, (x, y))
    # wall image
    img = pygame.image.load(wall_image)
    img = pygame.transform.scale(img, (wall_w, wall_h))
    screen.blit(img, (wall_x, wall_y))

    rect = pygame.Surface((500, 500))
    rect.set_alpha(50)
    rect.fill((0, 0, 0))
    screen.blit(rect, (0, 0))

    # pleyer
    square = pygame.Rect(pos_x, pos_y, pleyer_width, pleyer_height)
    pygame.draw.rect(screen, color, square)


def limit(x, y, wall_x, wall_y):
    print(x , "  ", y)
    print(wall_x , "  ", wall_y)
    if x > pos_x:
        x -= 10
        wall_x -= 10
    if pleyer_width + pos_x > x + plur_w:
        x += 10
        wall_x += 10

    if (wall_x <= pos_x <= wall_x + wall_w) and (wall_y < pos_y < wall_y + wall_h):
        x -= 10
        wall_x -= 10

    if y > pos_y:
        y -= 10
        wall_y -= 10
    if pleyer_height + pos_y > y + plur_h:
        y += 10
        wall_y += 10
        print(2)

    if (wall_y < pos_y < wall_y + wall_h) and (wall_x <= pos_x <= wall_x + wall_w):
        y -= 10
        print(1)
        wall_y -= 10



        # if wall_y < pos_y:
        #     y -= 10
        #     wall_y -= 10

    # if wall_y > pos_y > wall_y + wall_h:
    #     y -= 10
    #     wall_y -= 10
    # elif wall_x < pos_x < wall_x:
    #     x -= 10
    #     wall_x -= 10

    return [x, y, wall_x, wall_y]
