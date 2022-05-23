import sys

from pyfirmata import Arduino, util

import pygame.constants
from pygame import *
import ball
from const import *
import time
import math

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



# white = (255, 255, 255)
# green = (0, 255, 0)
# blue = (0, 0, 128)
# font = pygame.font.Font('freesansbold.ttf', 32)
# pygame.display.set_caption('Show Text')
# text = font.render('GeeksForGeeks', True, green, blue)

power = 0 # 59.047782557857325
angle = 0 #  1.5707963267948966
# time = 0



if __name__ == '__main__':
    # pygame.init()
    # clock = time.time()
    g = Game()
    my_ball = g.ball

    while True:
        if g.ball.throw:
            g.update_ball_pos(x=x , y=y, power=power, angle=angle)

        line = [(my_ball.pos_ball.x, my_ball.pos_ball.y), pygame.mouse.get_pos()]

        # g.ball.update_ball_pos()
        g.draw_all()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # g.pygame.quit()
                sys.exit()
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
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
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

        pygame.display.update()
