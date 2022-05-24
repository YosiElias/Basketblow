import sys
from typing import Tuple, Any

import pygame_menu
from pyfirmata import Arduino, util

import pygame.constants
from pygame import *
import ball
from const import *
import time
import math

from game import Game

global difficulty
difficulty = 2

def set_difficulty(selected: Tuple, value: Any) -> None:
    """
    Set the difficulty of the game.
    """
    print(f'Set difficulty to {selected[0]} ({value})')
    difficulty = int(value)


def creat_menu():
    # -------------------------------------------------------------------------
    # Init menu
    # -------------------------------------------------------------------------
    ABOUT = ["This is game of Basket-Blow",
             "",
             'Created By Aviva, Dina, Yagel and Yossi']
    COLOR_BACKGROUND = [128, 0, 128]
    HELP = ['Press ESC to enable/disable Menu',
            'Choose your game and click on it',
            'Now the window will close and the game will start']
    # Write help message on console
    for m in HELP:
        print(m)


    # Main timer and game clock
    first_font = pygame_menu.font.get_font(pygame_menu.font.FONT_NEVIS, 100)
    frame = 0

    # -------------------------------------------------------------------------
    # Create menus: Timer
    # -------------------------------------------------------------------------

    timer_theme = pygame_menu.themes.THEME_DARK.copy()  # Create a new copy
    timer_theme.background_color = (0, 0, 0, 180)  # Enable transparency

    # Timer
    games_menu = pygame_menu.Menu(
        height=400,
        onclose=pygame_menu.events.RESET,
        theme=timer_theme,
        title='Games Menu',
        width=600
    )

    # Add widgets
    games_menu.add.button('Return to Menu', pygame_menu.events.BACK)
    games_menu.add.button('Close Menu', pygame_menu.events.CLOSE)

    # -------------------------------------------------------------------------
    # Create menus: Help
    # -------------------------------------------------------------------------
    help_theme = pygame_menu.Theme(
        background_color=(30, 50, 107, 190),  # 75% opacity
        title_background_color=(120, 45, 30, 190),
        title_font=pygame_menu.font.FONT_FRANCHISE,
        title_font_size=60,
        widget_font=pygame_menu.font.FONT_FRANCHISE,
        widget_font_color=(170, 170, 170),
        widget_font_shadow=True,
        widget_font_shadow_position=pygame_menu.locals.POSITION_SOUTHEAST,
        widget_font_size=45
    )

    help_menu = pygame_menu.Menu(
        height=600,  # Fullscreen
        theme=help_theme,
        title='Help',
        width=800
    )
    for m in HELP:
        help_menu.add.label(m, align=pygame_menu.locals.ALIGN_CENTER)
    help_menu.add.vertical_margin(25)
    help_menu.add.button('Return to Menu', pygame_menu.events.BACK)

    # -------------------------------------------------------------------------
    # Create menus: About
    # -------------------------------------------------------------------------
    about_theme = pygame_menu.themes.THEME_DARK.copy()
    about_theme.widget_font = pygame_menu.font.FONT_NEVIS
    about_theme.title_font = pygame_menu.font.FONT_8BIT
    about_theme.title_offset = (5, -2)
    about_theme.widget_offset = (0, 0.14)

    about_menu = pygame_menu.Menu(
        center_content=False,
        height=400,
        mouse_visible=False,
        theme=about_theme,
        title='About',
        width=600
    )
    for m in ABOUT:
        about_menu.add.label(m, margin=(0, 0))
    about_menu.add.label('')
    about_menu.add.button('Return to Menu', pygame_menu.events.BACK)

    # -------------------------------------------------------------------------
    # Create menus: Main menu
    # -------------------------------------------------------------------------
    global main_menu
    main_menu = pygame_menu.Menu(
        enabled=False,
        height=400,
        theme=pygame_menu.themes.THEME_DARK,
        title='Main Menu',
        width=600
    )

    # main_menu.add.button(games_menu.get_title(), games_menu)  # Add timer submenu
    main_menu.add.selector('Difficulty: ', [('Easy', 2),('Hard', 1)], onchange=set_difficulty)
    main_menu.add.button(help_menu.get_title(), help_menu)  # Add help submenu
    main_menu.add.button(about_menu.get_title(), about_menu)  # Add about submenu
    main_menu.add.button('Exit', pygame_menu.events.EXIT)  # Add exit function




def convert_blow(blow):
    if difficulty==2:
        if 102000 < blow < 103000:
            blow = 0
        elif 103000 < blow < 104000:
            blow = 0#1
        elif 104000 < blow < 104500:
            blow = 3#2
        elif 104500 < blow < 105000:
            blow = 3#3
        elif 105000 < blow:
            blow = 3#4
        else:
            blow = -1
        return blow
    if difficulty == 1:
        if 102000 < blow < 103000:
            blow = 0
        elif 103000 < blow < 104000:
            blow = 3
        elif 104000 < blow < 104500:
            blow = 3
        elif 104500 < blow < 105000:
            blow = 3
        elif 105000 < blow:
            blow = 3
        else:
            blow = -1
        return blow


try:
    import serial
    import serial.tools.list_ports
except:
    import pip

    pip.main(['install', 'serial'])

PORT_NUMBER = 'COM7'  # TODO change according to port number
BAUDRATE = 9600
arduino_data = serial.Serial(PORT_NUMBER, BAUDRATE)    #Todo: #

# arduino_data.open() #Todo: #
# while True:
#     if arduino_data.in_waiting:
#         packet = arduino_data.readline()
#         a = packet.decode('utf').rstrip('\n')
#         print(a)    # in range: 101,000 - 110,000



# white = (255, 255, 255)
# green = (0, 255, 0)
# blue = (0, 0, 128)
# font = pygame.font.Font('freesansbold.ttf', 32)
# pygame.display.set_caption('Show Text')
# text = font.render('GeeksForGeeks', True, green, blue)

power = 0 # 59.047782557857325
angle = 0 #  1.5707963267948966
blow =-1
# time = 0



if __name__ == '__main__':
    # pygame.init()
    # clock = time.time()
    g = Game()
    my_ball = g.ball
    creat_menu()

    while True:
        if g.ball.throw:
            g.update_ball_pos(x=x , y=y, power=power, angle=angle)

        line = [(my_ball.pos_ball.x, my_ball.pos_ball.y), pygame.mouse.get_pos()]

        # g.ball.update_ball_pos()
        g.draw_all()
        current_menu = main_menu.get_current()
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE and \
                        current_menu.get_title() == 'Main Menu':
                    main_menu.toggle()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if not my_ball.throw:
                    x = my_ball.pos_ball.x
                    y = my_ball.pos_ball.y
                    pos = pygame.mouse.get_pos()
                    my_ball.throw = True
                    print(f'screen: {g.screen.get_height()}')
                    power = math.sqrt((line[1][1] - line[0][1]) ** 2 + (line[1][0] - line[0][1]) ** 2) / 8
                    angle = ball.findAngle(my_ball, pos)
                    # print("p:{}  angle:{}".format(power, angle))
                print("click {}".format(pygame.mouse.get_pos()))
                print("size {}".format(g.ball.scale_ball.x))
            if event.type == pygame.VIDEORESIZE:
                g.update_screen_size()

            if event.type == pygame.KEYDOWN:
                x = my_ball.pos_ball.x
                y = my_ball.pos_ball.y
                # if event.key == pygame.K_ESCAPE:
                #     pygame.quit()
                #     sys.exit()
                if event.key == pygame.K_p:
                    print("start throw")
                    g.set_throw_type()
                if event.key == pygame.K_0:
                    g.set_throw_type(0)
                if event.key == pygame.K_1:
                    g.set_throw_type(1)
                if event.key == pygame.K_2:
                    g.set_throw_type(2)
                if event.key == pygame.K_3:
                    g.set_throw_type(3)
                if event.key == pygame.K_4:
                    g.set_throw_type(4)

        if arduino_data.in_waiting and not g.ball.throw:  #Todo: #
            prev_blow = blow
            x = my_ball.pos_ball.x
            y = my_ball.pos_ball.y

            packet = arduino_data.readline()
            blow = packet.decode('utf').rstrip('\n')
            print(blow)
            blow = convert_blow(int(blow))
            print(blow)
            if blow == prev_blow:
                blow=-1
                print(blow)
            if blow != -1:
                g.set_throw_type(blow)
        else:
            blow=-1
        if arduino_data.in_waiting and g.ball.throw:
            packet = arduino_data.readline()
        #     temp = packet.decode('utf').rstrip('\n')
        # blow=-1

        if main_menu.is_enabled():
            main_menu.draw(g.screen)
            main_menu.update(events)

        pygame.display.update()
