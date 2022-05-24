import sys

from pyfirmata import Arduino, util
import webbrowser
import pygame.constants
from pygame import *
import ball
from const import *
from Control_key import *
import time
import math
import tkinter as tk
import threading



from game import Game


def convert_blow(blow):
    if 102000 < blow < 103000:
        blow = 0
    elif 103000 < blow < 104000:
        blow = 1
    elif 104000 < blow < 104500:
        blow = 2
    elif 104500 < blow < 105000:
        blow = 3
    elif 105000 < blow:
        blow = 4
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
# arduino_data = serial.Serial(PORT_NUMBER, BAUDRATE)

# arduino_data.open()
# while True:
#     if arduino_data.in_waiting:
#         packet = arduino_data.readline()
#         a = packet.decode('utf').rstrip('\n')
#         print(a)    # in range: 101,000 - 110,000


# __all__ = ['main']

import pygame
import pygame_menu
from pygame_menu.examples import create_example_window

import datetime
from random import randrange
from typing import List, Tuple, Optional

# Constants and global variables
ABOUT = ["This is game of Basket-Blow",
         "",
         'Created By Aviva, Dina, Yagel and Yossi']
COLOR_BACKGROUND = [128, 0, 128]
FPS = 60
H_SIZE = 600  # Height of window size
HELP = ['Press ESC to enable/disable Menu',
        'Choose your game and click on it',
        'Now the window will close and the game will start']
W_SIZE = 800  # Width of window size

screen: Optional['pygame.Surface'] = None
timer: Optional[List[float]] = None

def update_screen_size(background):
    scale_background = (screen.get_width(), screen.get_height())
    imgBackground = pygame.image.load('../source/background_net_game.jpg')
    background = pygame.transform.scale(imgBackground, scale_background)


def background_text():
    label = tk.Label(text='Instead of the space button,  Blow!\nIf you want back to menu please click on \'esc\'',
                     font=('Times', '30'), fg='black', bg='white')
    label.master.overrideredirect(True)
    label.master.geometry("+{}+{}".format(45, screen.get_height()-115))
    label.master.lift()
    label.master.wm_attributes("-topmost", True)
    label.master.wm_attributes("-disabled", True)
    label.master.wm_attributes("-transparentcolor", "white")
    label.pack()
    label.mainloop()

global th_background_text
global th_control_key

def speed_runer():
    # pygame.quit()
    # Create a Thread with a function without any arguments:
    th_background_text = threading.Thread(target=background_text)
    th_control_key = threading.Thread(target=main_key)
    # Start the threads:
    th_background_text.start()
    th_control_key.start()
    print(th_control_key.is_alive())
    print(th_background_text.is_alive())

    webbrowser.open_new_tab("https://clickspeeder.com/corona-runner/")
    # background_text()
    # main_key()


def main(test: bool = False) -> None:
    """
    Main program.

    :param test: Indicate function is being tested
    """

    # -------------------------------------------------------------------------
    # Init
    # -------------------------------------------------------------------------
    # Write help message on console
    for m in HELP:
        print(m)

    # Create window
    global screen
    screen = pygame.display.set_mode(SIZE, pygame.RESIZABLE) #create_example_window('Net-Game', (W_SIZE, H_SIZE))

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
    games_menu.add.button('Corona-runner -> Speed blow', speed_runer)
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
    main_menu = pygame_menu.Menu(
        enabled=False,
        height=400,
        theme=pygame_menu.themes.THEME_DARK,
        title='Main Menu',
        width=600
    )

    main_menu.add.button(games_menu.get_title(), games_menu)  # Add timer submenu
    main_menu.add.button(help_menu.get_title(), help_menu)  # Add help submenu
    main_menu.add.button(about_menu.get_title(), about_menu)  # Add about submenu
    main_menu.add.button('Exit', pygame_menu.events.EXIT)  # Add exit function

    # -------------------------------------------------------------------------
    # Background
    # -------------------------------------------------------------------------
    scale_background = (screen.get_width(), screen.get_height())
    imgBackground = pygame.image.load('../source/background_net_game.jpg')
    global background
    background = pygame.transform.scale(imgBackground, scale_background)

    # -------------------------------------------------------------------------
    # Main loop
    # -------------------------------------------------------------------------
    while True:
        frame += 1
        # Title is evaluated at current level as the title of the base pointer
        # object (main_menu) can change if user opens submenus
        current_menu = main_menu.get_current()
        screen.blit(background, (0, 0))

        # Application events
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE and \
                        current_menu.get_title() == 'Main Menu':
                    main_menu.toggle()
                if event.key == pygame.K_0:
                    control.press(Key.space)
                    # time.sleep(10)
                    control.release(Key.space)
            # if event.type == pygame.VIDEORESIZE:  Todo: add resizeable
            #         update_screen_size(background)

            # if event.type == pygame.KEYDOWN:
                # if event.key == pygame.K_p:
                #     print("start throw")
                #     g.set_throw_type()
                # if event.key == pygame.K_0:
                #     g.set_throw_type(0)
                # if event.key == pygame.K_1:
                #     g.set_throw_type(1)
                # if event.key == pygame.K_2:
                #     g.set_throw_type(2)
                # if event.key == pygame.K_3:
                #     g.set_throw_type(3)
                # if event.key == pygame.K_4:
                #     g.set_throw_type(4)
            # if arduino_data.in_waiting and not g.ball.throw:
            #     x = my_ball.pos_ball.x
            #     y = my_ball.pos_ball.y
            #     packet = arduino_data.readline()
            #     blow = packet.decode('utf').rstrip('\n')
            #     print(blow)
            #     blow = convert_blow(int(blow))
            #     print(blow)
            #     if blow != -1:
            #         g.set_throw_type(blow)

        if main_menu.is_enabled():
            main_menu.draw(screen)
            main_menu.update(events)

        # Flip surface
        pygame.display.flip()



if __name__ == '__main__':
    main()



#
# if __name__ == '__main__':
#     pygame.init()
#     # clock = time.time()
#
#     while True:
#
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 # g.pygame.quit()
#                 sys.exit()
#             if event.type == pygame.MOUSEBUTTONDOWN:
#                 if not my_ball.throw:
#                     x = my_ball.pos_ball.x
#                     y = my_ball.pos_ball.y
#                     pos = pygame.mouse.get_pos()
#                     my_ball.throw = True
#                     print(f'screen: {g.screen.get_height()}')
#                     power = math.sqrt((line[1][1] - line[0][1]) ** 2 + (line[1][0] - line[0][1]) ** 2) / 8
#                     angle = ball.findAngle(my_ball, pos)
#                     # print("p:{}  angle:{}".format(power, angle))
#                 print("click {}".format(pygame.mouse.get_pos()))
#                 print("size {}".format(g.ball.scale_ball.x))
#             if event.type == pygame.VIDEORESIZE:
#                 g.update_screen_size()
#
#             if event.type == pygame.KEYDOWN:
#                 x = my_ball.pos_ball.x
#                 y = my_ball.pos_ball.y
#                 if event.key == pygame.K_ESCAPE:
#                     pygame.quit()
#                     sys.exit()
#                 if event.key == pygame.K_p:
#                     print("start throw")
#                     g.set_throw_type()
#                 if event.key == pygame.K_0:
#                     g.set_throw_type(0)
#                 if event.key == pygame.K_1:
#                     g.set_throw_type(1)
#                 if event.key == pygame.K_2:
#                     g.set_throw_type(2)
#                 if event.key == pygame.K_3:
#                     g.set_throw_type(3)
#                 if event.key == pygame.K_4:
#                     g.set_throw_type(4)
#         # if arduino_data.in_waiting and not g.ball.throw:
#         #     x = my_ball.pos_ball.x
#         #     y = my_ball.pos_ball.y
#         #     packet = arduino_data.readline()
#         #     blow = packet.decode('utf').rstrip('\n')
#         #     print(blow)
#         #     blow = convert_blow(int(blow))
#         #     print(blow)
#         #     if blow != -1:
#         #         g.set_throw_type(blow)
#
#         pygame.display.update()
