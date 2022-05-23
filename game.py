from types import SimpleNamespace

import numpy as np
from ball import Ball, ballPath
from const import *
import time


class Game:
    def __init__(self):
        self.throw_type = None
        self.shot = False
        self.score = 0
        self.time = 0
        self.this_time = None
        self.this_time_fail = None

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
        self.dec_bal = None
        self.angle = None
        self.power = None
        self.bottom = self.screen.get_height() - self.ball.scale_ball.x + 1
        self.up = True
        self.update_level_and_scale_accordingly()  # init to level 0

        # text:
        pygame.font.init()
        self.FONT = pygame.font.SysFont('comicsans', int(self.screen.get_width()/11), bold=True)


    def update_level_and_scale_accordingly(self, level: int = 0):
        self.level = level
        if self.level == 0:
            # background update:
            self.scale_background = (self.screen.get_width(), self.screen.get_height())
            self.center = SimpleNamespace(x=self.screen.get_width() * 0.48609375,
                                          y=self.screen.get_height() * 0.39027777777)   #0.50390625
            self.start_point = SimpleNamespace(x=0, y=0)
            self.angle = 1.574783546494607 # 1.5658754526309344  # 1.5747771974857827
            self.dec_bal = 0.2
            self.power = 90.65892573997625 # 90.80007192301386# 81.6645702910162
            # ball update:
            # self.ball.way_up = 0.15
            # self.ball.half_way_up = 0.20
            # self.ball.way_mid = 0.27
            # self.ball.way_down = 0.45
            # self.ball.speed_up_down = 3

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
        self.ball.draw_ball()
        if 27.9 < self.ball.scale_ball.x < 29.65 and (409/1061 * self.screen.get_height()) < self.ball.pos_ball.y < (411/1061 * self.screen.get_height()):
            self.this_time = time.time()
        if self.this_time != None and (self.this_time+1.5) > time.time() > self.this_time:
            text = self.FONT.render("Good Job ! ! !", True, (20, 225, 20))
            self.screen.blit(text, (440/1920 * self.screen.get_width(), 423/1061 * self.screen.get_height()))

        if self.throw_type==TOO_WEAK_x2 and self.ball.pos_ball.y - (702/1061 * self.screen.get_height()) < 0.0000000000000001 and self.ball.scale_ball.x-85.80 < 0.00000000000000001:
            self.this_time_fail = time.time()
            print(time.time())
        if self.this_time_fail != None and (self.this_time_fail+2) > time.time() > self.this_time_fail:
            text = self.FONT.render("Try Again  :) ", True, (255, 0, 0))
            self.screen.blit(text, (440/1920 * self.screen.get_width(), 423/1061 * self.screen.get_height()))


    def draw_background(self):
        self.background = pygame.transform.scale(self.imgBackground, self.scale_background)
        self.screen.blit(self.background, (self.start_point.x, self.start_point.y))

    def update_screen_size(self):
        # update background:
        self.center = SimpleNamespace(x=self.screen.get_width() * 0.50390625,
                                      y=self.screen.get_height() * 0.39027777777)
        self.ball.center = self.center
        self.scale_background = (self.screen.get_width(), self.screen.get_height())
        self.background = pygame.transform.scale(self.imgBackground, self.scale_background)
        # update ball:
        self.ball.pos_ball = SimpleNamespace(x=self.center.x,
                                        y=self.screen.get_height() - self.ball.scale_ball.x)  # Todo: set right value



    def set_throw_type(self, throw_type: int = PERFECT):
        """
        here we get the strength of the blow from player as number in range of 0-4
        :param throw_type: (int) Represent the strength of the blow:
        TOO_WEAK_X2 = 0
        TOO_WEAK = 1
        PERFECT = 2
        TOO_STRONG = 3
        TOO_STRONG_x2 = 4
        """
        # self.ball.up = True  # change to up and later will change to False
        # self.speed_up_down = 3   # Todo: here need to update speed according to the throw_type
        self.ball.throw = True
        self.up = True
        self.throw_type = throw_type
        if throw_type == TOO_WEAK_x2:
            self.angle = 1.615389170947775
            self.power = 55.55543402764486
            self.bottom = 0.6981 * self.screen.get_height()
        if throw_type == TOO_WEAK_x1:
            self.angle = 1.615389170947775
            self.power = 55.55543402764486
        if throw_type == TOO_WEAK:
            self.angle = 1.5785016537496093
            self.power = 73.97972695272672
        if throw_type == PERFECT:
            self.angle = 1.574783546494607
            self.power = 90.65892573997625
            self.bottom = self.screen.get_height() - self.ball.scale_ball.x + 1
        if throw_type == TOO_STRONG:
            self.angle = 1.5701569406927685
            self.power = 98.56192533123529


    def back_ball_to_start(self):
        self.ball.back_ball_to_start()

    def update_ball_pos(self, x, y, power = 110, angle=110):
        if self.ball.pos_ball.y < self.bottom or self.up:
            power = self.power
            angle = self.angle
            self.time += 0.05
            po = ballPath(x, y, power, angle, self.time)
            if po[1] < self.ball.pos_ball.y -10:
                self.up = False
            self.ball.pos_ball.x = po[0]
            self.ball.pos_ball.y = po[1]
            if self.ball.scale_ball.x > 10:
                self.ball.scale_ball.x -= self.dec_bal
                self.ball.scale_ball.y -= self.dec_bal
            else:
                self.ball.scale_ball.x = 0
                self.ball.scale_ball.y = 0
                self.ball.throw = False
                self.time = 0
                self.ball.back_ball_to_start()
        else:
            self.ball.throw = False
            self.time = 0
            self.ball.back_ball_to_start()




