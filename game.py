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
