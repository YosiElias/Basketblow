from types import SimpleNamespace

import pygame
import numpy as np
import math



class Ball():
    def __init__(self, screen, center):
        self.speed_up_down: float = None  # set value in 'update_level_and_scale_accordingly' and maybe will update in 'set_throw_type'
        self.way_down: float = None  # set value in 'update_level_and_scale_accordingly'
        self.way_mid: float = None  # set value in 'update_level_and_scale_accordingly'
        self.way_up: float = None  # set value in 'update_level_and_scale_accordingly'
        self.half_way_up = None  # set value in 'update_level_and_scale_accordingly'

        self.center = center
        self.screen = screen
        self.shot = False
        self.throw = False
        self.up = True


        # init ball:
        self.scale_ball = SimpleNamespace(x=150, y=150)  # Todo: set right value
        self.pos_ball = SimpleNamespace(x=self.center.x,
                                        y=self.screen.get_height() - self.scale_ball.x)  # -40  # Todo: set right value
        self.imgBall = pygame.image.load('bestBall/result.png')
        self.ball = pygame.transform.scale(self.imgBall, (self.scale_ball.x, self.scale_ball.y))

    def draw_ball(self):
        self.ball = pygame.transform.scale(self.imgBall, (self.scale_ball.x, self.scale_ball.y))
        self.screen.blit(self.ball, (self.pos_ball.x, self.pos_ball.y))

    def update_ball_pos(self):
        if self.throw:
            if self.up:
                if self.pos_ball.y > self.screen.get_height() * self.half_way_up:
                    self.pos_ball.y -= self.speed_up_down
                    self.scale_ball.x -= 0.2
                    self.scale_ball.y -= 0.2
                elif self.pos_ball.y > self.screen.get_height() * self.way_up:
                    self.pos_ball.y -= self.speed_up_down / 2
                    self.scale_ball.x -= 0.2
                    self.scale_ball.y -= 0.2
                else:
                    self.up = False

            if not self.up:
                if self.pos_ball.y < self.screen.get_height() * self.way_mid:
                    self.pos_ball.y += self.speed_up_down / 4
                    self.scale_ball.x -= 0.4
                    self.scale_ball.y -= 0.4
                elif self.pos_ball.y < self.screen.get_height() * self.way_down:
                    self.pos_ball.y += self.speed_up_down
                    self.scale_ball.x -= 0.2
                    self.scale_ball.y -= 0.2
                else:   # end of throw
                    # Todo: add function to show message here and update score..
                    self.throw = False
                    self.up = True
                    self.back_ball_to_start()

    def back_ball_to_start(self):
        self.scale_ball = SimpleNamespace(x=150, y=150)  # Todo: set right value
        self.pos_ball = SimpleNamespace(x=self.center.x,
                                        y=self.screen.get_height() - self.scale_ball.x)

    # @staticmethod
def ballPath(startx, starty, power, ang, time):
    angle = ang
    velx = math.cos(angle) * power
    vely = math.sin(angle) * power

    distX = velx * time
    distY = (vely * time) + ((-4.9 * (time ** 2)) / 2)

    newx = round(distX + startx)
    newy = round(starty - distY)


    return (newx, newy)


def findAngle(golfball, pos):
    sX = golfball.pos_ball.x
    sY = golfball.pos_ball.y
    try:
        angle = math.atan((sY - pos[1]) / (sX - pos[0]))
    except:
        angle = math.pi / 2

    if pos[1] < sY and pos[0] > sX:
        angle = abs(angle)
    elif pos[1] < sY and pos[0] < sX:
        angle = math.pi - angle
    elif pos[1] > sY and pos[0] < sX:
        angle = math.pi + abs(angle)
    elif pos[1] > sY and pos[0] > sX:
        angle = (math.pi * 2) - angle

    return angle