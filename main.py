
import sys
from pyfirmata import Arduino, util

import pygame.constants
from pygame import display

from const import *
import time
import numpy as np

from game import Game

# screen = display.set_mode((WIDTH, HEIGHT), depth=32, flags=pygame.RESIZABLE)

# screen = pygame.display.set_mode(SIZE, depth=32, flags=pygame.RESIZABLE)

if __name__ == '__main__':
    # pygame.init()
    clock = time.time()
    g = Game()
    # img = pygame.image.load('source/img4.jpg')
    # change_w, change_h = 0.95, 1
    # background = pygame.transform.scale(img, g.scale_background)
    # g.screen.blit(background, (g.start_point[0], g.start_point[1]))
    # g.draw_ball()

    while True:
        g.ball.update_ball_pos()
        g.draw_all()
        # g.pos_ball.y -= 0.03
        # if g.scale_ball.x > 0:
        #     g.scale_ball.x -= 0.03
        #     g.scale_ball.y -= 0.03
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                g.pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                print("click {}".format(pygame.mouse.get_pos()))
            if event.type == pygame.VIDEORESIZE:
                g.update_screen_size()
                # background = pygame.transform.scale(g.imgBackground, (g.screen.get_width(), g.screen.get_height()))
                # g.screen.blit(background, (g.start_point.x, g.start_point.y))
                # g.draw_ball()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_p:
                    print("start throw")
                    g.set_throw_type()
                if event.key == pygame.K_1:
                    g.update_level_and_scale_accordingly(1)
                    # print("center = {}".format((g.screen.get_width()*0.50390625, g.screen.get_height()*0.39027777777)))
                    # background = pygame.transform.scale(img,g.scale_background)
                if event.key == pygame.K_0:
                    g.update_level_and_scale_accordingly(0)
                if event.key == pygame.K_b:
                    print("b")
                    g.draw_ball()
                # if event.key == pygame.K_z:
                #     print("click {}".format(pygame.mouse.get_pos()))
                    # change_w *= 1.075
                    # change_h *= 1.05
                    # if change_w > 2.3:
                    #     continue
                    # g.start_point[0] =  g.start_point[0] - 19
                    # g.start_point[1] =  g.start_point[1] - 8
                    # g.background = pygame.transform.scale(g.imgBackground,(g.screen.get_width() * change_w, g.screen.get_height() * change_w))
                    # print(change_w)
                    # print(change_w)

        pygame.display.update()
