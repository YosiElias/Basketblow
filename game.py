import numpy as np
from ball import Ball
from const import *
import time


class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode(SIZE, pygame.RESIZABLE)
        self.background_scale = (self.screen.get_width(), self.screen.get_height())
        self.center = (self.screen.get_width() * 0.50390625, self.screen.get_height() * 0.39027777777)
        self.start_point = [0, 0]

        self.ball = Ball()

        self.shot = False
        self.score = 0

        clock = time.time()
        self.level = 0

    def get_wight_height(self):
        """
        :return: background scale (width, height)
        """
        return self.background_scale

    def set_wight_height(self):
        """
        This function sets the background scale, center and the start point according to the level the user wants.
        :return: null
        """
        if self.level == 0:
            self.background_scale = (self.screen.get_width(), self.screen.get_height())
            self.center = (self.screen.get_width() * 0.50390625, self.screen.get_height() * 0.39027777777)
            self.start_point = [0, 0]
        if self.level == 1:
            self.background_scale = (self.screen.get_width() * 1.02125, self.screen.get_height() * 1.02125)
            self.center = (self.screen.get_width() * 0.50390625, self.screen.get_height() * 0.39027777777)
            self.start_point = [-19, -8]

    def set_level(self, level):
        """
        :param level: the level the user wants to play at
        :return: null
        """
        self.level = level
