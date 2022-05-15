
import sys
from pyfirmata import Arduino, util

import pygame.constants

from const import *
import time
import numpy as np

screen = pygame.display.set_mode(SIZE, pygame.RESIZABLE)
clock = time.time()

if __name__ == '__main__':
    background = pygame.image.load(r'C:\Users\dfred\Desktop\hackathon\project\images\img4.jpg')
    change_w, change_h = 0.95, 1
    start_point = [0, 0]
    background = pygame.transform.scale(background, (screen.get_width(), screen.get_height()))
    while True:
        screen.blit(background, (start_point[0], start_point[1]))
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.constants.MOUSEBUTTONDOWN:
                    print("click {}".format(pygame.mouse.get_pos()))
                if event.key == pygame.K_z:
                    change_w *= 1.075
                    change_h *= 1.05
                    if change_w > 2.3:
                        continue
                    start_point[0] = start_point[0] - 135
                    start_point[1] = start_point[1] - 45
                    background = pygame.transform.scale(background,
                                                        (screen.get_width() * change_w
                                                         , screen.get_height() * change_h))

        pygame.display.update()
