
from game import *
from opening import *
from move import *
from g import *
from screen_puse import *
Screen_mode = 'opening'
x = 0
y = 0
font = pygame.font.SysFont('Aharoni', 40)
text1 = font.render(setting_text, True,WHITE)

def main():
    global screen, Screen_mode, event, pos, player_image

    screen_size = (WINDOW_WIDTH, WINDOW_HEIGHT)
    screen = pygame.display.set_mode(screen_size)
    pygame.init()
    finish = False

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
    wall1 = wall(-200, -360, wall_w1, wall_h1)
    wall2 = wall(-210, -350, wall_w2, wall_h2)
    wall3 = wall(400, -360, wall_w3, wall_h3)
    wall4 = wall(-210, 241, wall_w4, wall_h4)
    walls = [wall1, wall2, wall3, wall4]
    # coins
    print_coin_1 = True
    print_coin_2 = True

    coin_1 = [250, 60, 50, 50, coin, print_coin_1]
    coin_2 = [-100, -100, 50, 50, coin, print_coin_2]

    num_of_coin = 0
    coins_1 = [num_of_coin, coin_1, coin_2]

    koz_1 = [0, 0, 20, 20, False]
    kosim = [koz_1]

    pleyer_image = step1
    go_up = False
    go_down = False
    go_rite = False
    go_left = False
    deracsen = go_up

    wall_001 = line_wall(200, 130, 200, 200)
    walls_level_1 = [wall_001]

    animal1 = animal(250, 0, 50, 50, 10, hatalef_left, True, 350, 200,True)
    animal2 = animal(-250, -200, 50, 50, 10, hatalef_left, True, 90, 0,True)
    animal3 = animal(0, 0, 50, 50, 20, hatalef_left, True, 10, 0,True)
    anemy = [animal1, animal2, animal3]

    animals_2 = [animal1]
    steps = [step1,step2,step3,step4,step5,step6,step7,step8,step9,step10]

    speed_cion_sail = False
    speed_a = 0
    shoott = False
    shoot_Valuable = [220, 220, 10, 10]
    x = 210
    y = 210
    while not finish:

        pygame.time.wait(5)

        if Screen_mode == 'level 1':
            limit(flur_x, flur_y, walls, coins_1, walls_level_1, Screen_mode, levels_2)

        if go_down:
            deracsen = 'go_down'
            for i in range(len(steps) - 5):
                pleyer_image = steps[i]
                if Screen_mode == 'level 1':
                    bild_level_1(1000, 1000, walls, pleyer_image, coins_1, anemy, lives,deracsen,text1)
                    limit(flur_x, flur_y, walls, coins_1, walls_level_1, Screen_mode, levels_2)
                if Screen_mode == 'level 2':
                    bild_level_2(pleyer_image,levels_2,lives,coins_1,animals_2,deracsen)
                if Screen_mode == 'bose':
                    y += 0.2
                    if y > 475:
                        y -= 1
                all_y_up(walls, flur_y, coins_1, walls_level_1, Screen_mode, levels_2, anemy,speed_a,shoot_Valuable)
                color = pygame.Surface.get_at(screen, (pos_x + pleyer_width // 2, pos_y + pleyer_height - 7))
                if color == (0, 0, 0, 255):
                    all_y_down(walls, flur_y, coins_1, walls_level_1, Screen_mode, levels_2, anemy,speed_a,shoot_Valuable)
                    break

                #d


                pygame.display.flip()

        if go_up:
            deracsen = 'go_up'
            for i in range(len(steps)):
                pleyer_image = steps[i]
                if Screen_mode == 'level 1':
                    bild_level_1(1000, 1000, walls, pleyer_image, coins_1, anemy, lives,deracsen,text1)
                    limit(flur_x, flur_y, walls, coins_1, walls_level_1, Screen_mode, levels_2)
                if Screen_mode == 'level 2':
                    bild_level_2(pleyer_image,levels_2,lives,coins_1,animals_2,deracsen)

                if Screen_mode == 'bose':
                    y -= 0.2
                    if y < 0:
                        y += 1
                all_y_down(walls, flur_y, coins_1, walls_level_1, Screen_mode, levels_2, anemy,speed_a,shoot_Valuable)
                color = pygame.Surface.get_at(screen, (pos_x + pleyer_width // 2, pos_y + 7))
                if color == (0, 0, 0, 255):
                    all_y_up(walls, flur_y, coins_1, walls_level_1, Screen_mode, levels_2, anemy,speed_a,shoot_Valuable)
                    break
                color = pygame.Surface.get_at(screen, (pos_x + pleyer_width // 2, pos_y))
                if color == (149,94,39,255):
                    Screen_mode = 'win'

                pygame.display.flip()

        if go_rite:
            deracsen = 'go_rite'
            for i in range(len(steps)):
                pleyer_image = steps[i]
                if Screen_mode == 'level 1':
                    bild_level_1(1000, 1000, walls, pleyer_image, coins_1, anemy, lives,deracsen,text1)
                    limit(flur_x, flur_y, walls, coins_1, walls_level_1, Screen_mode, levels_2)
                if Screen_mode == 'level 2':
                    bild_level_2(pleyer_image,levels_2,lives,coins_1,animals_2,deracsen)
                if Screen_mode == 'bose':
                    x += 0.2
                    if x > 475:
                        x -= 1
                all_x_left(walls, flur_x, coins_1, walls_level_1, Screen_mode, levels_2, anemy,speed_a,shoot_Valuable)
                color = pygame.Surface.get_at(screen, (pos_x + pleyer_width - 7, pos_y + pleyer_height // 2))
                if color == (0, 0, 0, 255):
                    all_x_rite(walls, flur_y, coins_1, walls_level_1, Screen_mode, levels_2, anemy,speed_a,shoot_Valuable)
                    break
                pygame.display.flip()

        if go_left:
            deracsen = 'go_left'
            for i in range(len(steps)):
                pleyer_image = steps[i]
                if Screen_mode == 'level 1':
                    bild_level_1(1000, 1000, walls, pleyer_image, coins_1, anemy, lives,deracsen,text1)
                    limit(flur_x, flur_y, walls, coins_1, walls_level_1, Screen_mode, levels_2)
                if Screen_mode == 'level 2':
                    bild_level_2(pleyer_image,levels_2,lives,coins_1,animals_2,deracsen)
                if Screen_mode == 'bose':
                    x -= 0.2
                    if x < 0:
                        x += 1
                all_x_rite(walls, flur_x, coins_1, walls_level_1, Screen_mode, levels_2, anemy,speed_a,shoot_Valuable)
                color = pygame.Surface.get_at(screen, (pos_x + 7, pos_y + pleyer_height // 2))
                if color == (0, 0, 0, 255):
                    all_x_left(walls, flur_y, coins_1, walls_level_1, Screen_mode, levels_2, anemy,speed_a,shoot_Valuable)
                    break

                pygame.display.flip()


        if hitnagsot(anemy):
            lives -= 10
            if lives == 0:
                Screen_mode = 'levels'

        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()

            if event.type == pygame.QUIT:
                finish = True
            if event.type == pygame.KEYUP:
                go_up = False
                go_down = False
                go_rite = False
                go_left = False
                if event.key == pygame.K_x:
                    if Screen_mode == 'bose':
                        shoott = True

                    elif Screen_mode == 'level 1':
                        shoott = True
                        shoot_Valuable = [210, 210, 10, 10]

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
                p = limit(flur_x, flur_y, walls, coins_1, walls_level_1, Screen_mode, levels_2)
                flur_x = p[0]
                flur_y = p[1]
                walls = p[2]
                num_of_coin = p[3]
            if Screen_mode== 'level 1':
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if ((setting_x <= pos[0] <= setting_x + 150) and
                            (setting_y <= pos[1] <= setting_y + setting_hight)):
                        chack_if_exit_or_resume = display_pause_screen()
                        if chack_if_exit_or_resume == True:
                            Screen_mode = 'levels'
                        elif chack_if_exit_or_resume == "level 1":
                            Screen_mode = 'level 1'

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if ((setting_x <= pos[0] <= setting_x + settin_width) and
                        (setting_y <= pos[1] <= setting_y + setting_hight)):
                    chack_if_exit_or_resume = display_pause_screen()
                    if chack_if_exit_or_resume == True:
                        Screen_mode = 'levels'
                    elif chack_if_exit_or_resume == "level 1":
                        Screen_mode = 'level 1'
                if Screen_mode == 'shop':
                    if ((100 <= pos[0] <= 160) and (
                            100 <= pos[1] <= 160)):
                        if speed_cion_sail == False:
                            if num_of_coin >= 2:
                                speed_cion_sail =True
                                speed_a += 3
                                num_of_coin -= 2
                if Screen_mode == 'opening':
                    if ((start_buttons_x_pos <= pos[0] <= start_buttons_x_pos + start_buttons_width) and (
                            start_buttons_y_pos <= pos[1] <= start_buttons_y_pos + start_buttons_height)):
                        Screen_mode = 'levels'
                if ((shop_buttons_x_pos <= pos[0] <= shop_buttons_x_pos + shop_buttons_width) and (
                        shop_buttons_y_pos <= pos[1] <= shop_buttons_y_pos + shop_buttons_height)):
                    if Screen_mode == 'opening':
                        Screen_mode = 'shop'

        if Screen_mode == 'bose':
            level_bose(deracsen,pleyer_image,x,y)
            if shoott:
                x = 210
                y = 210
                square = pygame.Rect(shoot_Valuable[0] + 20, shoot_Valuable[1] + shoot_Valuable[3], shoot_Valuable[2],
                                     shoot_Valuable[3])
                pygame.draw.rect(screen, (210, 30, 30), square)
                color = pygame.Surface.get_at(screen, (x, y))
                if color == (0, 0, 0, 255):
                    shoot_Valuable[0] = x
                    shoot_Valuable[1] = y
                if deracsen == 'go_down':
                    shoot_Valuable[1] += 10
                if deracsen == 'go_up':
                    shoot_Valuable[1] -= 10
                if deracsen == 'go_rite':
                    shoot_Valuable[0] += 10
                if deracsen == 'go_left':
                    shoot_Valuable[0] -= 10

                for i in range(len(anemy)):
                    if (anemy[i].x_pos < shoot_Valuable[0] < anemy[i].x_pos + anemy[i].WIDTH) and (
                            anemy[i].y_pos < shoot_Valuable[1] < anemy[i].y_pos + anemy[i].HEIGHT):
                        shoott = False
                        anemy[i].alive = False


        if Screen_mode == 'opening':
            restart_opening_windows()

        elif Screen_mode == 'levels':
            levels_screen(levels_screen_x, levels_screen_y, levels_screen_w, levels_screen_h)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if (30 <= pos[0] <= 90) and (30 <= pos[1] <= 90):
                    wall1 = wall(-200, -360, wall_w1, wall_h1)
                    wall2 = wall(-210, -350, wall_w2, wall_h2)
                    wall3 = wall(400, -360, wall_w3, wall_h3)
                    wall4 = wall(-210, 241, wall_w4, wall_h4)
                    walls = [wall1, wall2, wall3, wall4]
                    lives = 180
                    coin_1 = [250, 60, 30, 30, coin, print_coin_1]
                    coin_2 = [-100, -100, 30, 30, coin, print_coin_2]
                    coins_1 = [num_of_coin, coin_1, coin_2]
                    animal1 = animal(250, 0, 50, 50, 10, hatalef_left, True, 350, 200,True)
                    animal2 = animal(-250, -200, 50, 50, 10, hatalef_left, True, 90, 0,True)
                    animal3 = animal(0, 0, 50, 50, 10, hatalef_left, True, 10, 0,True)
                    anemy = [animal1, animal2, animal3]
                    flur_y = -350
                    flur_x = -250
                    Screen_mode = 'level 1'


                if Screen_mode == 'levels':
                    if (30 + 90 <= pos[0] <= 90 + 90) and (30 <= pos[1] <= 90):
                        Screen_mode = 'level 2'
                        lives = 200
                        animal1 = animal(250, 0, 50, 50, 10, hatalef_left, True, 350, 200,True)

                if Screen_mode == 'levels':
                    if (30 <= pos[0] <= 130) and (400 <= pos[1] <= 460):
                        Screen_mode = 'opening'

        if Screen_mode == 'win':
            win_game()
            if (140< pos[0] <140+200) and (
                    210 < pos[2] < 60):
                pass


        elif Screen_mode == 'level 1':
            bild_level_1(flur_x, flur_y, walls, pleyer_image, coins_1, anemy, lives,deracsen,text1)

        elif Screen_mode == 'level 2':
            levels_screen(levels_screen_x, levels_screen_y, levels_screen_w, levels_screen_h)
            bild_level_2(pleyer_image,levels_2,lives,coins_1,animals_2,deracsen)
            wall1 = wall(-200, -360, wall_w1, wall_h1)
            wall2 = wall(-210, -350, wall_w2, wall_h2)
            wall3 = wall(400, -360, wall_w3, wall_h3)
            wall4 = wall(-210, 241, wall_w4, wall_h4)
            walls = [wall1, wall2, wall3, wall4]
            lives = 180
            coin_1 = [250, 60, 30, 30, coin, print_coin_1]
            coin_2 = [-100, -100, 30, 30, coin, print_coin_2]
            coins_1 = [num_of_coin, coin_1, coin_2]
            animal1 = animal(250, 0, 50, 50, 10, hatalef_left, True, 0, 200, True)
            animal2 = animal(-250, -200, 50, 50, 10, hatalef_left, True, 90, 0, True)
            animal3 = animal(0, 0, 50, 50, 10, hatalef_left, True, 10, 0, True)
            anemy = [animal1, animal2, animal3]

        elif Screen_mode == 'shop':
            shop(coins_1,speed_cion_sail)
            if (30 <= pos[0] <= 130) and (400 <= pos[1] <= 460):
                Screen_mode = 'opening'





        if shoott:
            x =210
            y = 210
            square = pygame.Rect(shoot_Valuable[0] +20, shoot_Valuable[1] + shoot_Valuable[3] , shoot_Valuable[2], shoot_Valuable[3])
            pygame.draw.rect(screen, (210, 30, 30), square)
            color = pygame.Surface.get_at(screen, (x, y))
            if color == (0, 0, 0, 255):
                shoot_Valuable[0] = x
                shoot_Valuable[1] = y
            if deracsen == 'go_down':
                shoot_Valuable[1] += 10
            if deracsen == 'go_up':
                shoot_Valuable[1] -= 10
            if deracsen == 'go_rite':
                shoot_Valuable[0] += 10
            if deracsen == 'go_left':
                shoot_Valuable[0] -= 10

            for i in range(len(anemy)):
                if (anemy[i].x_pos < shoot_Valuable[0] < anemy[i].x_pos + anemy[i].WIDTH) and (anemy[i].y_pos < shoot_Valuable[1] < anemy[i].y_pos + anemy[i].HEIGHT):
                    shoott = False
                    anemy[i].alive = False



        pygame.display.flip()
    pygame.quit()


main()
