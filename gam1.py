from types import SimpleNamespace

import numpy as np
from ball import Ball
from const import *
import time


class Game:
    def __init__(self):
        # init for game:
        # self.speed_up_down: float = None  # set value in 'update_level_and_scale_accordingly' and maybe will update in 'set_throw_type'
        # self.way_down: float = None  # set value in 'update_level_and_scale_accordingly'
        # self.way_mid: float = None  # set value in 'update_level_and_scale_accordingly'
        # self.way_up: float = None  # set value in 'update_level_and_scale_accordingly'
        # self.half_way_up = None # set value in 'update_level_and_scale_accordingly'

        # self.up = True
        # self.throw = False

        self.shot = False
        self.score = 0

        # init pygame:
        self.pygame = pygame.init()
        clock = time.time()
        self.screen = pygame.display.set_mode(SIZE, pygame.RESIZABLE)
        self.center = SimpleNamespace(x=self.screen.get_width() * 0.48609375,
                                      y=self.screen.get_height() * 0.39027777777)

        # init background:
        self.scale_background = (self.screen.get_width(), self.screen.get_height())
        self.imgBackground = pygame.image.load('source/img4.jpg')
        self.background = pygame.transform.scale(self.imgBackground, self.scale_background)
        # self.update_level_and_scale_accordingly()  # init to level 0

        # init ball:
        self.ball = Ball(self.screen, self.center)
        self.update_level_and_scale_accordingly()  # init to level 0

        # self.scale_ball = SimpleNamespace(x=150, y=150)  # Todo: set right value
        # self.pos_ball = SimpleNamespace(x=self.center.x,
        #                                 y=self.screen.get_height() - self.scale_ball.x) #-40  # Todo: set right value
        # self.imgBall = pygame.image.load('bestBall/result.png')
        # self.ball = pygame.transform.scale(self.imgBall, (self.scale_ball.x, self.scale_ball.y))

        clock = time.time()

    def update_level_and_scale_accordingly(self, level: int = 0):
        self.level = level
        if self.level == 0:
            # background update:
            self.scale_background = (self.screen.get_width(), self.screen.get_height())
            self.center = SimpleNamespace(x=self.screen.get_width() * 0.48609375,
                                          y=self.screen.get_height() * 0.39027777777)   #0.50390625
            self.start_point = SimpleNamespace(x=0, y=0)
            # ball update:
            self.ball.way_up = 0.15
            self.ball.half_way_up = 0.20
            self.ball.way_mid = 0.27
            self.ball.way_down = 0.45
            self.ball.speed_up_down = 3

        if self.level == 1:
            # background update:
            self.scale_background = (self.screen.get_width() * 1.02125, self.screen.get_height() * 1.02125)
            self.center = SimpleNamespace(x=self.screen.get_width() * 0.50390625,
                                          y=self.screen.get_height() * 0.39027777777)
            self.start_point = SimpleNamespace(x=-19, y=-8)
            # ball update:
            # Todo: add value according to level 1 (way and speed)

    def draw_all(self):
        self.draw_background()
        self.ball.draw_ball() # self.draw_ball()

    # def draw_ball(self):
    #     self.ball = pygame.transform.scale(self.imgBall, (self.scale_ball.x, self.scale_ball.y))
    #     self.screen.blit(self.ball, (self.pos_ball.x, self.pos_ball.y))

    def draw_background(self):
        self.background = pygame.transform.scale(self.imgBackground, self.scale_background)
        self.screen.blit(self.background, (self.start_point.x, self.start_point.y))

    def update_screen_size(self):
        # update background:
        self.center = SimpleNamespace(x=self.screen.get_width() * 0.50390625,
                                      y=self.screen.get_height() * 0.39027777777)
        self.scale_background = (self.screen.get_width(), self.screen.get_height())
        self.background = pygame.transform.scale(self.imgBackground, self.scale_background)
        # update ball:
        self.pos_ball = SimpleNamespace(x=self.center.x,
                                        y=self.screen.get_height() - self.ball.scale_ball.x)  # Todo: set right value

    # def update_ball_pos(self):
    #     if self.throw:
    #         if self.up:
    #             if self.pos_ball.y > self.screen.get_height() * self.half_way_up:
    #                 self.pos_ball.y -= self.speed_up_down
    #                 self.scale_ball.x -= 0.2
    #                 self.scale_ball.y -= 0.2
    #             elif self.pos_ball.y > self.screen.get_height() * self.way_up:
    #                 self.pos_ball.y -= self.speed_up_down / 2
    #                 self.scale_ball.x -= 0.2
    #                 self.scale_ball.y -= 0.2
    #             else:
    #                 self.up = False
    #
    #         if not self.up:
    #             if self.pos_ball.y < self.screen.get_height() * self.way_mid:
    #                 self.pos_ball.y += self.speed_up_down / 4
    #                 self.scale_ball.x -= 0.4
    #                 self.scale_ball.y -= 0.4
    #             elif self.pos_ball.y < self.screen.get_height() * self.way_down:
    #                 self.pos_ball.y += self.speed_up_down
    #                 self.scale_ball.x -= 0.2
    #                 self.scale_ball.y -= 0.2
    #             else:   # end of throw
    #                 # Todo: add function to show message here and update score..
    #                 self.throw = False
    #                 self.up = True
    #                 self.back_ball_to_start()


    def set_throw_type(self, throw_type: int = PERFECT):
        """
        here we get the strength of the blow from player as number in range of 0-4
        :param throw_type: (int) Represent the strength of the blow:
        TOO_WEAK_x2 = 0
        TOO_WEAK_x2 = 1
        PERFECT = 2
        TOO_STRONG = 3
        TOO_STRONG_x2 = 4
        """
        self.ball.up = True  # change to up and later will change to False
        self.ball.throw = True
        self.throw_type = PERFECT   # Todo: here need to update the throw_type
        self.speed_up_down = 3   # Todo: here need to update speed according to the throw_type

    def back_ball_to_start(self):
        self.ball.back_ball_to_start()
        # self.pos_ball.y = self.screen.get_height() - self.scale_ball.x
        # self.scale_ball = SimpleNamespace(x=150, y=150)  # Todo: set right value



