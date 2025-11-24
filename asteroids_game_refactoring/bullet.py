import math

import pygame

from constants import BULLET_SPEED, Display, Color
from game_object import GameObject


class Bullet(GameObject):
    '''Projectile object for Player and Saucer'''

    def __init__(self, x: float, y: float,
                 direction: float, surface: pygame.Surface):
        self.x = x
        self.y = y
        self.direction_degree = direction
        self.live_frames_left = 30
        self.surface = surface

    def update(self):
        self.x += (
            BULLET_SPEED *
            math.cos(self.direction_degree * math.pi / 180)
        )
        self.y += (
            BULLET_SPEED *
            math.sin(self.direction_degree * math.pi / 180)
        )

        if self.x > Display.width:
            self.x = 0
        elif self.x < 0:
            self.x = Display.width
        elif self.y > Display.height:
            self.y = 0
        elif self.y < 0:
            self.y = Display.height
        self.live_frames_left -= 1

    def draw(self):
        pygame.draw.circle(
            self.surface, Color.white,
            (int(self.x), int(self.y)), 3)
