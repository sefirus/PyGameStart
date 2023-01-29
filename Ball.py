import pygame
from random import randrange as rnd


class Ball(pygame.Rect):

    def __init__(self, radius: int, default_speed: int,  screen_h: int, screen_w: int):
        self.radius = radius
        self.speed = default_speed
        self.box_dimension = int(radius * 2 ** 0.5)
        super().__init__(rnd(self.box_dimension, screen_h - self.box_dimension), screen_w // 2, self.box_dimension,
                         self.box_dimension)
        self.direction_x = 1
        self.direction_y = -1

    pass
