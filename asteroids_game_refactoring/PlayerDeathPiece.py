import math
import random
from typing import TYPE_CHECKING

from constants import Color

if TYPE_CHECKING:
    from game import Game

import pygame


class PlayerDeathPiece:
    def __init__(self, x: float, y: float, length, game: Game):
        self.angle = random.randrange(0, 360) * math.pi / 180
        self.dir = random.randrange(0, 360) * math.pi / 180
        self.rtspd = random.uniform(-0.25, 0.25)
        self.x = x
        self.y = y
        self.length = length
        self.speed = random.randint(2, 8)
        self.game = game

    def updateDeadPlayer(self):
        pygame.draw.line(self.game.display, Color.white,
                         (self.x + self.length * math.cos(self.angle) / 2,
                          self.y + self.length * math.sin(self.angle) / 2),
                         (self.x - self.length * math.cos(self.angle) / 2,
                          self.y - self.length * math.sin(self.angle) / 2))
        self.angle += self.rtspd
        self.x += self.speed * math.cos(self.dir)
        self.y += self.speed * math.sin(self.dir)
