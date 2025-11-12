from enum import Enum
import random
import math
from typing import TYPE_CHECKING
import pygame

from constants import Color, Display
from game_object import GameObject

if TYPE_CHECKING:
    from Asteroids import Game


class AsteroidType(Enum):
    SMALL = 'Small'
    NORMAL = 'Normal'
    LARGE = 'Large'


class Asteroid(GameObject):
    '''Represents breakable asteroid game objects'''

    def __init__(self, x: int, y: int, type_: AsteroidType, game: Game):
        self.x = x
        self.y = y
        if type_ == AsteroidType.SMALL:
            self.size = 30
        elif type_ == AsteroidType.NORMAL:
            self.size = 20
        else:
            self.size = 10
        self.type = type_
        self.game = game

        # Make random speed and direction
        self.speed = random.uniform(1, (40 - self.size) * 4 / 15)
        self.dir = random.randrange(0, 360) * math.pi / 180

        # Make random asteroid sprites
        full_circle = random.uniform(18, 36)
        dist = random.uniform(self.size / 2, self.size)
        self.vertices = []
        while full_circle < 360:
            self.vertices.append([dist, full_circle])
            dist = random.uniform(self.size / 2, self.size)
            full_circle += random.uniform(18, 36)

    def update(self):
        # Move asteroid
        self.x += self.speed * math.cos(self.dir)
        self.y += self.speed * math.sin(self.dir)

        # Check for wrapping
        if self.x > Display.width:
            self.x = 0
        elif self.x < 0:
            self.x = Display.width
        elif self.y > Display.height:
            self.y = 0
        elif self.y < 0:
            self.y = Display.height

    def draw(self):
        for v in range(len(self.vertices)):
            if v == len(self.vertices) - 1:
                next_v = self.vertices[0]
            else:
                next_v = self.vertices[v + 1]
            this_v = self.vertices[v]
            pygame.draw.line(
                self.game.gameDisplay, Color.white,
                (self.x + this_v[0] * math.cos(this_v[1] * math.pi / 180),
                 self.y + this_v[0] * math.sin(this_v[1] * math.pi / 180)),
                (self.x + next_v[0] * math.cos(next_v[1] * math.pi / 180),
                 self.y + next_v[0] * math.sin(next_v[1] * math.pi / 180)))
