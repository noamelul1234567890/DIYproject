from game import *
from opening import *
from move import *
from screen_puse import *

Screen_mode = 'opening'
x = 0
y = 0
live = 0
a = 0
font = pygame.font.SysFont('Aharoni', 40)
text1 = font.render(setting_text, True, WHITE)


def main():
    global screen, Screen_mode, event, pos, player_image, live, pos_x, pos_y, time, text1
    pygame.mixer.init()
    music1 = pygame.mixer.Sound(bg_sound)
    music2 = pygame.mixer.Sound(hitnagshut_sound)

    # Play both music files simultaneously
    # setup all the variables
    screen_size = (WINDOW_WIDTH, WINDOW_HEIGHT)
    screen = pygame.display.set_mode(screen_size)
    pygame.init()
    finish = False
    timer_start_bose = 0
    lives = 180
    fire_on = True
    flur_y = -350
    flur_x = -250
    x_fire = 140
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
    num_of_coin = 0
    coin_1 = [250, 60, 50, 50, coin, print_coin_1]
    coin_2 = [-100, -100, 50, 50, coin, print_coin_2]
    coin_3 = [0, 0, 50, 50, coin, True]
    coins_1 = [num_of_coin, coin_1, coin_2, coin_3]
    pleyer_image = step1
    go_up = False
    go_down = False
    go_rite = False
    go_left = False
    deracsen = go_up
    Screen_mode = 'opening'
    wall_001 = line_wall(200, 130, 200, 200)
    walls_level_1 = [wall_001]
    animal1 = animal(250, 0, 50, 50, 10, hatalef_left, True, 350, 200, True)
    animal2 = animal(-250, -200, 50, 50, 10, hatalef_left, True, 90, 0, True)
    animal3 = animal(100, 300, 50, 50, 10, hatalef_left, True, 5000, -1000, True)
    animal4 = animal(-250, -160, 50, 50, 10, hatalef_left, True, 150, 10, True)
    anemy = [animal1, animal2, animal3, animal4]
    animals_2 = [animal1, animal4]
    steps = [step1, step2, step3, step4, step5, step6, step7, step8, step9, step10]
    speed_cion_sail = False
    speed_a: int = 0
    shoott = False
    shoot_Valuable = [220, 220, 10, 10]
    x = 210
    y = 210
    atak = 'first'
    yui_1 = 50
    yui_2 = 50
    yui_3 = 50
    hand_1 = 0
    hand_2 = 0
    hand_3 = 0

    while not finish:
        timemer = pygame.time.get_ticks()

        # Load the music file
        screen.fill((0, 0, 0))

        if Screen_mode == 'level 1':
            limit(flur_x, flur_y, walls, coins_1, walls_level_1, Screen_mode, levels_2)
        if go_down:
            deracsen = 'go_down'
            for i in range(len(steps) - 5):
                pleyer_image = steps[i]
                if Screen_mode == 'level 1':
                    bild_level_1(1000, 1000, walls, pleyer_image, coins_1,
                                 anemy,
                                 lives, deracsen, text1, )
                    limit(flur_x, flur_y, walls, coins_1, walls_level_1,
                          Screen_mode, levels_2)
                if Screen_mode == 'level 2':
                    bild_level_2(pleyer_image, levels_2, lives, coins_1,
                                 animals_2,
                                 deracsen, text1)
                if Screen_mode == 'bose':
                    y += 0.5
                    if y > 475:
                        y -= 1
                all_y_up(walls, flur_y, coins_1, walls_level_1, Screen_mode,
                         levels_2, anemy, speed_a, shoot_Valuable)
                color = pygame.Surface.get_at(screen, (
                    pos_x + pleyer_width // 2, pos_y + pleyer_height - 7))
                if color == (0, 0, 0, 255):
                    all_y_down(walls, flur_y, coins_1, walls_level_1,
                               Screen_mode,
                               levels_2, anemy, speed_a,
                               shoot_Valuable)
                    break

                # d

                pygame.display.flip()

        if go_up:
            deracsen = 'go_up'
            for i in range(len(steps)):
                pleyer_image = steps[i]
                if Screen_mode == 'level 1':
                    bild_level_1(1000, 1000, walls, pleyer_image, coins_1,
                                 anemy,
                                 lives, deracsen, text1, )
                    limit(flur_x, flur_y, walls, coins_1, walls_level_1,
                          Screen_mode, levels_2)
                if Screen_mode == 'level 2':
                    bild_level_2(pleyer_image, levels_2, lives, coins_1,
                                 animals_2,
                                 deracsen, text1)

                if Screen_mode == 'bose':
                    y -= 0.5
                    if y < 50:
                        y += 1
                all_y_down(walls, flur_y, coins_1, walls_level_1, Screen_mode,
                           levels_2, anemy, speed_a, shoot_Valuable)
                color = pygame.Surface.get_at(screen, (
                    pos_x + pleyer_width // 2, pos_y + 7))
                if color == (0, 0, 0, 255):
                    all_y_up(walls, flur_y, coins_1, walls_level_1, Screen_mode,
                             levels_2, anemy, speed_a,
                             shoot_Valuable)
                    break
                color = pygame.Surface.get_at(screen,
                                              (
                                                  pos_x + pleyer_width // 2, pos_y))
                if color == (149, 94, 39, 255):
                    Screen_mode = 'win'

                pygame.display.flip()

        if go_rite:
            deracsen = 'go_rite'
            for i in range(len(steps)):
                pleyer_image = steps[i]
                if Screen_mode == 'level 1':
                    bild_level_1(1000, 1000, walls, pleyer_image, coins_1,
                                 anemy,
                                 lives, deracsen, text1, )
                    limit(flur_x, flur_y, walls, coins_1, walls_level_1,
                          Screen_mode, levels_2)
                if Screen_mode == 'level 2':
                    bild_level_2(pleyer_image, levels_2, lives, coins_1,
                                 animals_2,
                                 deracsen, text1)
                if Screen_mode == 'bose':
                    x += 0.5
                    if x > 475:
                        x -= 1
                all_x_left(walls, flur_x, coins_1, walls_level_1, Screen_mode,
                           levels_2, anemy, speed_a, shoot_Valuable)
                color = pygame.Surface.get_at(screen, (
                    pos_x + pleyer_width - 7, pos_y + pleyer_height // 2))
                if color == (0, 0, 0):
                    all_x_rite(walls, flur_y, coins_1, walls_level_1,
                               Screen_mode,
                               levels_2, anemy, speed_a,
                               shoot_Valuable)
                    break
                pygame.display.flip()

        if go_left:
            deracsen = 'go_left'
            for i in range(len(steps)):
                pleyer_image = steps[i]
                if Screen_mode == 'level 1':
                    bild_level_1(1000, 1000, walls, pleyer_image, coins_1,
                                 anemy,
                                 lives, deracsen, text1, )
                    limit(flur_x, flur_y, walls, coins_1, walls_level_1,
                          Screen_mode, levels_2)
                if Screen_mode == 'level 2':
                    bild_level_2(pleyer_image, levels_2, lives, coins_1,
                                 animals_2,
                                 deracsen, text1)
                if Screen_mode == 'bose':
                    x -= 0.5
                    if x < 0:
                        x += 1
                all_x_rite(walls, flur_x, coins_1, walls_level_1, Screen_mode,
                           levels_2, anemy, speed_a, shoot_Valuable)
                color = pygame.Surface.get_at(screen, (
                    pos_x + 7, pos_y + pleyer_height // 2))
                if color == (0, 0, 0, 255):
                    all_x_left(walls, flur_y, coins_1, walls_level_1,
                               Screen_mode,
                               levels_2, anemy, speed_a,
                               shoot_Valuable)
                    break

                pygame.display.flip()

        if hitnagsot(anemy):
            lives -= 10
            if lives == 0:
                Screen_mode = 'lose'

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
                        pos_x = x
                        pos_y = y

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
                p = limit(flur_x, flur_y, walls, coins_1, walls_level_1, Screen_mode, levels_2)
                flur_x = p[0]
                flur_y = p[1]
                walls = p[2]
                num_of_coin = p[3]
            if Screen_mode == 'level 1':
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if ((setting_x <= pos[0] <= setting_x + 150) and
                            (setting_y <= pos[1] <= setting_y + setting_hight)):
                        chack_if_exit_or_resume = display_pause_screen(Screen_mode)
                        if chack_if_exit_or_resume == True:
                            Screen_mode = 'levels'
                        elif chack_if_exit_or_resume == "level 1":
                            Screen_mode = 'level 1'

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()

                if Screen_mode == 'win' or Screen_mode == 'lose':
                    pos = pygame.mouse.get_pos()
                    print(pos)
                    if (140 < pos[0] < 340) and (210 < pos[1] < 270):
                        Screen_mode = 'levels'
                        pygame.mixer.music.load(level_2_sound)
                        # Set the volume

                        # Play the music
                        pygame.mixer.music.play()
                    if (140 < pos[0] < 340) and (280 < pos[1] < 340):
                        Screen_mode = 'levels'
                        pygame.mixer.music.load(bg_sound)
                        # Set the volume

                        # Play the music
                        pygame.mixer.music.play()

                if ((setting_x <= pos[0] <= setting_x + settin_width) and
                        (setting_y <= pos[1] <= setting_y + setting_hight)):
                    chack_if_exit_or_resume = display_pause_screen(Screen_mode)
                    if chack_if_exit_or_resume == True:
                        Screen_mode = 'levels'
                    elif chack_if_exit_or_resume == "level 1":
                        Screen_mode = 'level 1'
                if Screen_mode == 'shop':
                    if ((100 <= pos[0] <= 160) and (
                            100 <= pos[1] <= 160)):
                        if speed_cion_sail == False:
                            if num_of_coin >= 2:
                                speed_cion_sail = True
                                speed_a += 2
                                num_of_coin -= 2
                if Screen_mode == 'opening':
                    if ((start_buttons_x_pos <= pos[0] <= start_buttons_x_pos + start_buttons_width) and (
                            start_buttons_y_pos <= pos[1] <= start_buttons_y_pos + start_buttons_height)):
                        pygame.mixer.music.load(start_sound)
                        # Set the volume

                        # Play the music
                        pygame.mixer.music.play()
                        Screen_mode = 'levels'
                if ((shop_buttons_x_pos <= pos[0] <= shop_buttons_x_pos + shop_buttons_width) and (
                        shop_buttons_y_pos <= pos[1] <= shop_buttons_y_pos + shop_buttons_height)):
                    if Screen_mode == 'opening':
                        Screen_mode = 'shop'

        if Screen_mode == 'bose':
            if live < 0:
                Screen_mode = 'lose'

            level_bose(deracsen, pleyer_image, x, y, atak, a, live, timer_start_bose)
            atak_1 = [100, 300, True]

            if timer_start_bose + 1000 < timemer < timer_start_bose + 2000:
                font = pygame.font.SysFont(None, 40)
                text2 = font.render('you ur uglei', True, (0, 10, 10))
                screen.blit(text2, [30, 60])

            if timer_start_bose + 1800 < timemer < timer_start_bose + 3000:
                font = pygame.font.SysFont(None, 60)
                text2 = font.render('no', True, (0, 10, 10))
                screen.blit(text2, [150, 200])

            if timer_start_bose + 5000 < timemer < timer_start_bose + 7000:
                image = pygame.image.load(hegrof)
                p = pygame.transform.rotate(image, 180)
                p = pygame.transform.scale(p, (100, 100))
                screen.blit(p, (300, yui_1))
                if yui_1 < 130:
                    yui_1 += 1

                image = pygame.image.load(rto)
                p = pygame.transform.rotate(image, 180)
                p = pygame.transform.scale(p, (100, 100))
                screen.blit(p, (atak_1[0], atak_1[1]))
            elif timer_start_bose + 7000 < timemer < timer_start_bose + 8000:
                image = pygame.image.load(xx)
                p = pygame.transform.rotate(image, 180)
                p = pygame.transform.scale(p, (100, 100))
                screen.blit(p, (atak_1[0], atak_1[1]))
                if atak_1[0] < x + 5 < atak_1[1] + 100 and atak_1[1] < y + 5 < \
                        atak_1[1] + 100 and atak_1[2]:
                    live -= 1
                    atak_1[2] = False

            if timer_start_bose + 7000 < timemer < timer_start_bose + 10000:
                image = pygame.image.load(hegrof)
                p = pygame.transform.rotate(image, 180)
                p = pygame.transform.scale(p, (100, 100))
                screen.blit(p, (300, yui_1))
                if yui_1 < 130:
                    yui_1 += 1
                image = pygame.image.load(rto)
                p = pygame.transform.rotate(image, 180)
                p = pygame.transform.scale(p, (100, 100))
                screen.blit(p, (150, 140))
            elif timer_start_bose + 10000 < timemer < timer_start_bose + 11000:
                image = pygame.image.load(xx)
                p = pygame.transform.rotate(image, 180)
                p = pygame.transform.scale(p, (100, 100))
                screen.blit(p, (150, 140))
                if 150 < x + 5 < 150 + 100 and 140 < y + 5 < 140 + 100 and atak_1[2]:
                    live -= 1
                    atak_1[2] = False

            if timer_start_bose + 10000 < timemer < timer_start_bose + 14000:
                image = pygame.image.load(hegrof)
                p = pygame.transform.rotate(image, 180)
                p = pygame.transform.scale(p, (100, 100))
                screen.blit(p, (300, yui_2))
                if yui_2 < 130:
                    yui_2 += 1
                image = pygame.image.load(rto)
                p = pygame.transform.rotate(image, 180)
                p = pygame.transform.scale(p, (100, 100))
                screen.blit(p, (atak_1[0] + 200, atak_1[1] - 100))

            elif timer_start_bose + 14000 < timemer < timer_start_bose + 15000:
                image = pygame.image.load(xx)
                p = pygame.transform.rotate(image, 180)
                p = pygame.transform.scale(p, (100, 100))
                screen.blit(p, (atak_1[0] + 200, atak_1[1] - 100))
                if atak_1[0] + 200 < x + 5 < atak_1[1] + 400 and atak_1[
                    1] - 100 < y + 5 < atak_1[1] and atak_1[2]:
                    live -= 1
                    atak_1[2] = False

            if timer_start_bose + timemer > 15000 and timer_start_bose + timemer < 18000:
                image = pygame.image.load(hegrof)
                p = pygame.transform.rotate(image, 180)
                p = pygame.transform.scale(p, (100, 100))
                screen.blit(p, (300, yui_3))
                if yui_3 < 130:
                    yui_3 += 2

                image = pygame.image.load(rto)
                p = pygame.transform.rotate(image, 180)
                p = pygame.transform.scale(p, (100, 100))
                screen.blit(p, (atak_1[0] + 100, atak_1[1] - 50))
            elif timer_start_bose + 18000 < timemer < timer_start_bose + 19000:
                image = pygame.image.load(xx)
                p = pygame.transform.rotate(image, 180)
                p = pygame.transform.scale(p, (100, 100))
                screen.blit(p, (atak_1[0] + 100, atak_1[1] - 50))
                if atak_1[0] + 200 < x + 5 < atak_1[1] + 400 and atak_1[
                    1] < y + 5 < atak_1[1] + 50 and atak_1[2]:
                    live -= 1
                    atak_1[2] = False
            # atak 2
            if timer_start_bose + 20000 < timemer < timer_start_bose + 21000:
                square = pygame.Rect(300, 80, hand_1, 20)
                pygame.draw.rect(screen, (0, 10, 10), square)
                hand_1 += 10

                square = pygame.Rect(100, 50, 20, 500)
                pygame.draw.rect(screen, (250, 0, 0), square)
            if timer_start_bose + 21000 < timemer < timer_start_bose + 22500:

                square = pygame.Rect(300, 80, hand_1, 20)
                pygame.draw.rect(screen, (0, 10, 10), square)
                hand_1 += 10

                square = pygame.Rect(100, 50, 20, 500)
                pygame.draw.rect(screen, (0, 10, 10), square)
                if 100 < y + 5 < 20 and 100 < x + 5 < 120:
                    live -= 1

            if timer_start_bose + 20500 < timemer < timer_start_bose + 21500:
                square = pygame.Rect(300, 90, hand_2, 20)
                pygame.draw.rect(screen, (20, 10, 20), square)
                hand_2 += 10
                square = pygame.Rect(0, 150, 500, 20)
                pygame.draw.rect(screen, (250, 0, 0), square)
            if timer_start_bose + 21500 < timemer < timer_start_bose + 23000:
                square = pygame.Rect(300, 90, hand_2, 20)
                pygame.draw.rect(screen, (0, 10, 10), square)
                hand_2 += 10
                square = pygame.Rect(0, 150, 500, 20)
                pygame.draw.rect(screen, (0, 10, 10), square)
                if 0 < x + 5 < 500 and 150 < y + 5 < 170:
                    live -= 1

            if timer_start_bose + 21500 < timemer < timer_start_bose + 22500:
                square = pygame.Rect(300, 110, hand_3, 20)
                pygame.draw.rect(screen, (0, 10, 10), square)
                hand_3 += 10
                square = pygame.Rect(350, 50, 20, 500)
                pygame.draw.rect(screen, (250, 0, 0), square)
            if timer_start_bose + 22500 < timemer < timer_start_bose + 23500:
                square = pygame.Rect(300, 110, hand_3, 20)
                pygame.draw.rect(screen, (0, 10, 10), square)
                hand_3 += 10
                square = pygame.Rect(350, 50, 20, 500)
                pygame.draw.rect(screen, (0, 10, 10), square)
                if 350 < x + 5 < 370 and 50 < y + 5 < 500:
                    live -= 1

            # atak 3

            if timer_start_bose + 3000 < timemer < timer_start_bose + 15000:
                rains = []
                times = []
                for i in range(100):
                    xxx = random.randint(0, 480)
                    yyy = random.randint(50, 480)
                    time = random.randint(1000, 2000)
                    rains.append([xxx, yyy])
                    times.append(time)

                time_10 = pygame.time.get_ticks()
                for i in range(100):
                    if times[i] < time_10 < times[i] + 1000:
                        square = pygame.Rect(rains[i][0], rains[i][1], 20, 20)
                        pygame.draw.rect(screen, (250, 0, 0), square)

                for i in range(100):
                    if time_10 + 1000 > times[i] and time_10 < times[i] + 2000:
                        square = pygame.Rect(rains[i][0], rains[i][1], 20, 20)
                        pygame.draw.rect(screen, (0, 10, 10), square)

            if timemer > timer_start_bose + 36000:
                Screen_mode = 'win'

            if timer_start_bose + 30000 < timemer < timer_start_bose + 35000:
                font = pygame.font.SysFont(None, 40)
                text2 = font.render('how you do it?', True, (0, 10, 10))
                screen.blit(text2, [30, 60])

            if timer_start_bose + 31000 < timemer < timer_start_bose + 35000:
                font = pygame.font.SysFont(None, 60)
                text2 = font.render('i play fortinit', True, (0, 10, 10))
                screen.blit(text2, [150, 200])

            if timer_start_bose + 25000 < timemer < timer_start_bose + 30000:
                if fire_on:
                    x_fire += 2
                    if x_fire > 400:
                        fire_on = False
                else:
                    x_fire -= 2
                image = pygame.image.load(fire)
                p = pygame.transform.rotate(image, 180)
                p = pygame.transform.scale(p, (100, 100))
                screen.blit(p, (200, x_fire))
                if x_fire < y + 5 < x_fire + 100 and 200 < x + 5 < 300:
                    live -= 1

            if timer_start_bose + 28000 < timemer < timer_start_bose + 35000:
                image = pygame.image.load(firefire)
                p = pygame.transform.rotate(image, 0)
                p = pygame.transform.scale(p, (200, 200))
                screen.blit(p, (150, -30))

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
                    coin_1 = [250, 80, 30, 30, coin, print_coin_1]
                    coin_2 = [-100, -100, 30, 30, coin, print_coin_2]
                    coin_3 = [350, 80, 30, 30, coin, True]
                    coins_1 = [num_of_coin, coin_1, coin_2, coin_3]
                    animal1 = animal(250, 0, 50, 50, 10, hatalef_left, True, 350, 200, True)
                    animal2 = animal(-250, -200, 50, 50, 10, hatalef_left, True, 90, 0, True)
                    animal3 = animal(0, 0, 50, 50, 10, hatalef_left, True, 10, 0, True)
                    animal4 = animal(-250, -160, 50, 50, 10, hatalef_left, True, 150, 10, True)

                    anemy = [animal1, animal2, animal3, animal4]
                    flur_y = -350
                    flur_x = -250

                    Screen_mode = 'level 1'
                    pygame.time.wait(5)
                    if Screen_mode == 'level 1':
                        pygame.mixer.music.stop()
                        # Load the music file
                        pygame.mixer.music.load(bg_sound)

                        # Set the volume
                        pygame.mixer.music.set_volume(0.5)

                        # Play the music
                        pygame.mixer.music.play()

                if Screen_mode == 'levels':
                    if (30 + 90 <= pos[0] <= 90 + 90) and (30 <= pos[1] <= 90):
                        Screen_mode = 'level 2'
                        lives = 200
                        animal1 = animal(250, 0, 50, 50, 10, hatalef_left, True, 350, 200, True)
                        if Screen_mode == 'level 2':
                            pygame.mixer.music.load(level_2_sound)
                            # Set the volume
                            # Play the music
                            pygame.mixer.music.play()

                if Screen_mode == 'levels':
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load(start_sound)
                    # Set the volume

                    # Play the music
                    pygame.mixer.music.play()
                    if (30 <= pos[0] <= 130) and (400 <= pos[1] <= 460):
                        Screen_mode = 'opening'

                if (370 <= pos[0] <= 470) and (30 <= pos[1] <= 130):
                    Screen_mode = 'bose'
                    timer_start_bose = timemer

                    # Set the volume
                    pygame.mixer.music.load(boss_sound)

                    # Play the music
                    pygame.mixer.music.play()
                    live = 180

        if Screen_mode == 'win':
            win_game()



        elif Screen_mode == 'level 1':
            time = pygame.time.get_ticks()
            bild_level_1(flur_x, flur_y, walls, pleyer_image, coins_1, anemy, lives, deracsen, text1, )

        elif Screen_mode == 'level 2':

            levels_screen(levels_screen_x, levels_screen_y, levels_screen_w, levels_screen_h)
            bild_level_2(pleyer_image, levels_2, lives, coins_1, animals_2,
                         deracsen, text1)
            wall1 = wall(-200, -360, wall_w1, wall_h1)
            wall2 = wall(-210, -350, wall_w2, wall_h2)
            wall3 = wall(400, -360, wall_w3, wall_h3)
            wall4 = wall(-210, 241, wall_w4, wall_h4)
            walls = [wall1, wall2, wall3, wall4]
            lives = 180
            coin_1 = [250, 60, 30, 30, coin, print_coin_1]
            coin_2 = [-100, -100, 30, 30, coin, print_coin_2]
            coin_3 = [280, 60, 80, 80, coin, print_coin_1]
            coins_1 = [num_of_coin, coin_1, coin_2, coin_3]
            animal1 = animal(250, 0, 50, 50, 10, hatalef_left, True, 0, 200, True)
            animal2 = animal(-250, -200, 50, 50, 10, hatalef_left, True, 90, 0, True)
            animal3 = animal(0, 0, 50, 50, 10, hatalef_left, True, 10, 0, True)
            anemy = [animal1, animal2, animal3]



        elif Screen_mode == 'shop':
            shop(coins_1, speed_cion_sail)
            if (30 <= pos[0] <= 130) and (400 <= pos[1] <= 460):
                Screen_mode = 'opening'
        elif Screen_mode == 'lose':
            lose()
        if shoott:
            x = 220
            y = 220
            square = pygame.Rect(shoot_Valuable[0] + 20, shoot_Valuable[1] + shoot_Valuable[3], shoot_Valuable[2],
                                 shoot_Valuable[3])
            pygame.draw.rect(screen, (210, 30, 30), square)
            color = pygame.Surface.get_at(screen, (x, y))
            if color == (0, 0, 0, 255):
                shoot_Valuable[0] = x
                shoot_Valuable[1] = y
            if deracsen == 'go_down':
                shoot_Valuable[1] += 10
                if shoot_Valuable[1] > 500:
                    shoott = False
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

        pygame.display.flip()
    pygame.quit()


main()
