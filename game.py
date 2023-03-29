from game import *
from opening import *
from move import *
from g import *
from screen_puse import *
from pygame.locals import *
from pygame import mixer

Screen_mode = 'opening'
x = 0
y = 0
live = 0
a = 0
font = pygame.font.SysFont('Aharoni', 40)
text1 = font.render(setting_text, True, WHITE)


def main():
    global screen, Screen_mode, event, pos, player_image, live, pos_x, pos_y, time

    screen_size = (WINDOW_WIDTH, WINDOW_HEIGHT)
    screen = pygame.display.set_mode(screen_size)
    pygame.init()
    finish = False

    atak = 'first'

    lives = 180

    flur_y = -350
    flur_x = -250

    levels_screen_x = 0
    levels_screen_y = 0
    levels_screen_w = 600
    levels_screen_h = 600

    levels_2_x = -270
    levels_2_y = -740
    levels_2 = [levels_2_x, levels_2_y]

    # walls of level 1
import time

from animals import *
from bose_atak import bose_atak
from classs import *

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.RESIZABLE)


def level_bose(deracsen, pleyer_image, x, y, atak, a, live,timer_start_bose):
    # baceraund
    img = pygame.image.load(flure)
    img = pygame.transform.scale(img,
                                 (500, 500))
    screen.blit(img, (0, 0))
    # the bose
    img = pygame.image.load(bose)
    img = pygame.transform.scale(img,
                                 (200, 100))
    screen.blit(img, (150, 50))

    if deracsen == 'go_rite':
        image = pygame.image.load(pleyer_image)
        pleyer_image = pygame.transform.rotate(image, -90)
    elif deracsen == 'go_left':
        image = pygame.image.load(pleyer_image)
        pleyer_image = pygame.transform.rotate(image, 90)
    elif deracsen == 'go_up':
        image = pygame.image.load(pleyer_image)
        pleyer_image = pygame.transform.rotate(image, 0)
    elif deracsen == 'go_down':
        image = pygame.image.load(pleyer_image)
        pleyer_image = pygame.transform.rotate(image, 180)
    else:
        image = pygame.image.load(pleyer_image)
        pleyer_image = pygame.transform.rotate(image, 180)

    pleyer_image = pygame.transform.scale(pleyer_image, (30, 30))
    screen.blit(pleyer_image, (x, y))



    square = pygame.Rect(0, 0, 1000, 50)
    pygame.draw.rect(screen, (100, 100, 100), square)

    square = pygame.Rect(130, 10, 200, 32)
    pygame.draw.rect(screen, (0, 100, 100), square)

    square = pygame.Rect(140, 13, 1 * live, 25)
    pygame.draw.rect(screen, (250, 00, 00), square)

    font = pygame.font.Font(None, 36)
    text = font.render("coins:  {}".format(0), True, (0, 0, 0))
    screen.blit(text, (10, 10))
    timea = pygame.time.get_ticks()
    font = pygame.font.Font(None, 36)
    text = font.render("time:  {}".format((timea - timer_start_bose) // 1000), True, (0, 0, 0))
    screen.blit(text, (400, 60))
    screen.blit(text1, (setting_x, setting_y))


def levels_screen(levels_screen_x, levels_screen_y, levels_screen_w, levels_screen_h):
    square = pygame.Rect(levels_screen_x, levels_screen_y, levels_screen_w, levels_screen_h)
    pygame.draw.rect(screen, (200, 200, 250), square)

    square = pygame.Rect(start_level1_buttons_x_pos + 90, start_level1_buttons_y_pos, start_level1_buttons_width,
                         start_level1_buttons_height)
    pygame.draw.rect(screen, (100, 100, 250), square)

    square = pygame.Rect(start_level1_buttons_x_pos, start_level1_buttons_y_pos, start_level1_buttons_width,
                         start_level1_buttons_height)
    pygame.draw.rect(screen, (100, 100, 250), square)

    font = pygame.font.SysFont(None, 100)
    text = font.render('1', True, color)
    screen.blit(text, [start_level1_buttons_x_pos + 10, start_level1_buttons_y_pos + 3])

    font = pygame.font.SysFont(None, 100)
    text = font.render('2', True, color)
    screen.blit(text, [start_level1_buttons_x_pos + 100, start_level1_buttons_y_pos + 3])

    img = pygame.image.load(bake_botom_image)
    img = pygame.transform.scale(img, (100, 60))
    screen.blit(img, (30, 400))

    square = pygame.Rect(370, 30, 100, 100)
    pygame.draw.rect(screen, (200, 00, 10), square)

    font = pygame.font.SysFont(None, 55)
    text = font.render('bose', True, (40, 0, 0))
    screen.blit(text, [375, 60])


def bild_level_2(pleyer_image, level_2, lives, coins, animals, deracsen, text1):
    screen.fill((0, 0, 0))
    img = pygame.image.load(level2_image)
    img = pygame.transform.scale(img, (1000, 1000))
    screen.blit(img, (level_2[0], level_2[1]))
    for i in range(len(animals)):
        img = pygame.image.load(animals[i].image)
        img = pygame.transform.scale(img, (animals[i].WIDTH, animals[i].HEIGHT))
        screen.blit(img, (animals[i].x_pos, animals[i].y_pos))

    if deracsen == 'go_rite':
        image = pygame.image.load(pleyer_image)
        pleyer_image = pygame.transform.rotate(image, -90)
    elif deracsen == 'go_left':
        image = pygame.image.load(pleyer_image)
        pleyer_image = pygame.transform.rotate(image, 90)
    elif deracsen == 'go_up':
        image = pygame.image.load(pleyer_image)
        pleyer_image = pygame.transform.rotate(image, 0)
    elif deracsen == 'go_down':
        image = pygame.image.load(pleyer_image)
        pleyer_image = pygame.transform.rotate(image, 180)
    else:
        image = pygame.image.load(pleyer_image)
        pleyer_image = pygame.transform.rotate(image, 180)

    pleyer_image = pygame.transform.scale(pleyer_image, (50, 50))
    screen.blit(pleyer_image, (pos_x, pos_y))

    animals_move(animals)

    # img = pygame.image.load(pleyer_image)
    # img = pygame.transform.scale(img, (pleyer_width, pleyer_height))
    # screen.blit(img, (pos_x, pos_y))
    zzel()
    print_score(lives, coins,)
    screen.blit(text1, (setting_x, setting_y))


def bild_level_1(x, y, walls, pleyer_image, coins, animals, lives, deracsen, text1,):

    img = pygame.image.load(plur_image)
    img = pygame.transform.scale(img, (plur_w, plur_h))
    screen.blit(img, (walls[0].wall_x, walls[0].wall_y))
    for i in range(len(animals)):
        img = pygame.image.load(animals[i].image)
        img = pygame.transform.scale(img, (animals[i].WIDTH, animals[i].HEIGHT))
        screen.blit(img, (animals[i].x_pos, animals[i].y_pos))

    for i in range(1, len(coins)):
        if coins[i][5]:
            img = pygame.image.load(coins[i][4])
            img = pygame.transform.scale(img, (coins[i][2], coins[i][3]))
            screen.blit(img, (coins[i][0], coins[i][1]))

    zzel()
    print_score(lives, coins,)

    rect = pygame.Surface((500, 500))
    rect.set_alpha(50)
    rect.fill((0, 0, 0))
    screen.blit(rect, (0, 0))

    # player
    if deracsen == 'go_rite':
        image = pygame.image.load(pleyer_image)
        pleyer_image = pygame.transform.rotate(image, -90)
    elif deracsen == 'go_left':
        image = pygame.image.load(pleyer_image)
        pleyer_image = pygame.transform.rotate(image, 90)
    elif deracsen == 'go_up':
        image = pygame.image.load(pleyer_image)
        pleyer_image = pygame.transform.rotate(image, 0)
    elif deracsen == 'go_down':
        image = pygame.image.load(pleyer_image)
        pleyer_image = pygame.transform.rotate(image, 180)
    else:
        image = pygame.image.load(pleyer_image)
        pleyer_image = pygame.transform.rotate(image, 180)

    pleyer_image = pygame.transform.scale(pleyer_image, (50, 50))
    screen.blit(pleyer_image, (pos_x, pos_y))
    screen.blit(text1, (setting_x, setting_y))

    animals_move(animals)


def shop(cions, speed_coin_sail):
    screen.fill((0, 0, 0))
    img = pygame.image.load(madaf)
    img = pygame.transform.scale(img, (600, 600))
    screen.blit(img, (-60, -60))

    font = pygame.font.Font(None, 36)
    text = font.render("coins:  {}".format(cions[0]), True, (250, 100, 0))
    screen.blit(text, (10, 10))

    img = pygame.image.load(bake_botom_image)
    img = pygame.transform.scale(img, (100, 60))
    screen.blit(img, (30, 400))
    if speed_coin_sail == False:
        img = pygame.image.load(coin_speed)
        img = pygame.transform.scale(img, (60, 60))
        screen.blit(img, (100, 100))

        font = pygame.font.Font(None, 36)
        text = font.render('2 coins', True, (0, 100, 0))
        screen.blit(text, (90, 150))


def limit(flur_x, flur_y, walls, coins, walls_level_1, Screen_mode, levels_2):
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

    p = [flur_x, flur_y, walls, coins[0]]
    return p


def print_score(lives, coins,):
    square = pygame.Rect(0, 0, 1000, 50)
    pygame.draw.rect(screen, (100, 100, 100), square)

    square = pygame.Rect(130, 10, 200, 32)
    pygame.draw.rect(screen, (0, 100, 100), square)

    square = pygame.Rect(140, 13, 1 * lives, 25)
    pygame.draw.rect(screen, (250, 00, 00), square)

    font = pygame.font.Font(None, 36)
    text = font.render("coins:  {}".format(coins[0]), True, (0, 0, 0))
    screen.blit(text, (10, 10))

    # font = pygame.font.Font(None, 36)
    # text = font.render("time:  {}".format(time//1000), True, (250, 0, 250))
    # screen.blit(text, (400, 60))


def zzel():
    alpa = 0
    for i in range(170, 1000, 10):
        surface1 = screen.convert_alpha()
        surface1.fill([0, 0, 0, 0])
        pygame.draw.circle(surface1, (0, 0, 0, alpa), (235, 240), i, 20)
        screen.blit(surface1, (0, 0))
        alpa += 13
        if alpa > 250:
            break


def shoot(animals, shoot_Valuable, deracsen):
    if deracsen == 'go_down':
        shoot_Valuable[3] += 10
    if deracsen == 'go_up':
        shoot_Valuable[3] -= 10
    if deracsen == 'go_rite':
        shoot_Valuable[2] += 10
    if deracsen == 'go_left':
        shoot_Valuable[2] -= 10

    pygame.time.wait(1)
    square = pygame.Rect(shoot_Valuable[0] + shoot_Valuable[2] / 2, shoot_Valuable[1] + shoot_Valuable[3] / 2,
                         shoot_Valuable[2], shoot_Valuable[3])
    pygame.draw.rect(screen, (210, 30, 30), square)


def win_game():
    # bakeruond
    square = pygame.Rect(0, 0, 1000, 1000)
    pygame.draw.rect(screen, (0, 0, 0), square)
    # bake to levels butom
    square = pygame.Rect(140, 210, 200, 60)
    pygame.draw.rect(screen, (250, 20, 0), square)

    font = pygame.font.SysFont(None, 100)
    text1 = font.render('levels', True, (0, 10, 10))
    screen.blit(text1, [140, 210])
    # print you win
    font = pygame.font.SysFont(None, 100)
    text = font.render('you win!!!', True, (250, 250, 0))
    screen.blit(text, [start_level1_buttons_x_pos + 50, start_level1_buttons_y_pos + 10])

def lose():
    # bakeruond
    square = pygame.Rect(0, 0, 1000, 1000)
    pygame.draw.rect(screen, (0, 0, 0), square)
    # bake to levels butom
    square = pygame.Rect(140, 270, 200, 60)
    pygame.draw.rect(screen, (250, 20, 0), square)

    font = pygame.font.SysFont(None, 100)
    text1 = font.render('levels', True, (0, 10, 10))
    screen.blit(text1, [140, 270])
    # print you win
    font = pygame.font.SysFont(None, 100)
    text = font.render('you lose!!!', True, (250, 250, 0))
    screen.blit(text, [start_level1_buttons_x_pos + 50, start_level1_buttons_y_pos + 10])
