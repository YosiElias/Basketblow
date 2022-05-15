import numpy as np
from ball import Ball
from const import *
import time


class Game:
    def __init__(self):
        self.ball = Ball()
        self.shot = False
        self.score = 0
        self.screen = pygame.display.set_mode(SIZE, pygame.RESIZABLE)
        clock = time.time()
        self.level = 0
        self.get_wight_hight()


    def get_wight_hight(self):
        if self.level == 0:
            self.scale_background = (self.screen.get_width(), self.screen.get_height())
            self.center = (self.screen.get_width()*0.50390625, self.screen.get_height()*0.39027777777)
            self.start_point = [0,0]
        if self.level == 1:
            self.scale_background = (self.screen.get_width()*1.02125, self.screen.get_height()*1.02125)
            self.center = (self.screen.get_width()*0.50390625, self.screen.get_height()*0.39027777777)
            self.start_point = [-19,-8]

