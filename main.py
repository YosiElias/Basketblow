
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
    pygame.init()
    clock = time.time()
    g = Game()
    img = pygame.image.load('source/img4.jpg')
    change_w, change_h = 0.95, 1
    background = pygame.transform.scale(img, g.background_scale)

    while True:
        g.screen.blit(background, ( g.start_point[0],  g.start_point[1]))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                print("click {}".format(pygame.mouse.get_pos()))
            if event.type == pygame.VIDEORESIZE:
                background = pygame.transform.scale(img, (g.screen.get_width(), g.screen.get_height()))
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_p:
                    print("width = {} -- hight = {}".format(g.screen.get_width(), g.screen.get_height()))
                if event.key == pygame.K_1:
                    g.level = 1
                    g.get_wight_hight()
                    print("center = {}".format((g.screen.get_width()*0.50390625, g.screen.get_height()*0.39027777777)))
                    background = pygame.transform.scale(img, g.background_scale)
                if event.key == pygame.K_2:
                    print("center = {}".format((g.screen.get_width()*0.50390625, g.screen.get_height()*0.39027777777)))
                    background = pygame.transform.scale(img, g.background_scale)
                if event.key == pygame.K_z:
                    print("click {}".format(pygame.mouse.get_pos()))
                    change_w *= 1.075
                    change_h *= 1.05
                    # if change_w > 2.3:
                    #     continue
                    g.start_point[0] =  g.start_point[0] - 19
                    g.start_point[1] =  g.start_point[1] - 8
                    background = pygame.transform.scale(img,(g.screen.get_width() * change_w, g.screen.get_height() * change_w))
                    print(change_w)
                    print(change_w)

        pygame.display.update()
