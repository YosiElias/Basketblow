import pygame
import numpy as np


class Ball(pygame.sprite.Sprite):
    def __init__(self):
        """
        initializing the object ball
        """
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.image = pygame.transform.scale(self.image, (radius * 2, radius * 2))
        self.state = [0, 0, 0, 0]
        self.prev_state = [0, 0, 0, 0]
        self.mass = mass
        self.t = 0
        self.radius = radius
        # self.friction = 0.0001
        self.g = 9.8

    def draw_ball(self, surface):
        """
        This function draw one image onto another
        :param surface: pygame object for representing images
        :return: null
        """
        rect = self.image.get_rect()
        rect.center = (self.state[0], 640 - self.state[1])  # Flipping y
        surface.blit(self.image, rect)
