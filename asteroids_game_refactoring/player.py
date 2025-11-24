import math

import pygame

from constants import (
    PLAYER_SIZE, PLAYER_MAX_SPEED, ACCELERATION,
    DECELERATION, Color, Display
)
from typing import TYPE_CHECKING

from game_object import GameObject

if TYPE_CHECKING:
    from game import Game


class Player(GameObject):
    def __init__(self, x: float, y: float, game: Game):
        self.x = x
        self.y = y
        self.hspeed = 0
        self.vspeed = 0
        self.dir = -90
        self.rtspd = 0
        self.thrust = False
        self.game = game

    def update(self):
        # Move player
        speed = math.sqrt(self.hspeed**2 + self.vspeed**2)
        if self.thrust:
            if speed + ACCELERATION < PLAYER_MAX_SPEED:
                self.hspeed += ACCELERATION * \
                    math.cos(self.dir * math.pi / 180)
                self.vspeed += ACCELERATION * \
                    math.sin(self.dir * math.pi / 180)
            else:
                self.hspeed = PLAYER_MAX_SPEED * \
                    math.cos(self.dir * math.pi / 180)
                self.vspeed = PLAYER_MAX_SPEED * \
                    math.sin(self.dir * math.pi / 180)
        else:
            if speed - DECELERATION > 0:
                change_in_hspeed = (
                    DECELERATION * math.cos(self.vspeed / self.hspeed))
                change_in_vspeed = (
                    DECELERATION * math.sin(self.vspeed / self.hspeed))
                if self.hspeed != 0:
                    if change_in_hspeed / abs(change_in_hspeed) == self.hspeed / abs(self.hspeed):
                        self.hspeed -= change_in_hspeed
                    else:
                        self.hspeed += change_in_hspeed
                if self.vspeed != 0:
                    if change_in_vspeed / abs(change_in_vspeed) == self.vspeed / abs(self.vspeed):
                        self.vspeed -= change_in_vspeed
                    else:
                        self.vspeed += change_in_vspeed
            else:
                self.hspeed = 0
                self.vspeed = 0
        self.x += self.hspeed
        self.y += self.vspeed

        # Check for wrapping
        if self.x > Display.width:
            self.x = 0
        elif self.x < 0:
            self.x = Display.width
        elif self.y > Display.height:
            self.y = 0
        elif self.y < 0:
            self.y = Display.height

        # Rotate player
        self.dir += self.rtspd

    def draw(self):
        a = math.radians(self.dir)
        x = self.x
        y = self.y
        s = PLAYER_SIZE
        t = self.thrust
        # Draw player
        pygame.draw.line(
            self.game.display, Color.white,
            (x - (s * math.sqrt(130) / 12) * math.cos(math.atan(7 / 9) + a),
             y - (s * math.sqrt(130) / 12) * math.sin(math.atan(7 / 9) + a)),
            (x + s * math.cos(a), y + s * math.sin(a)))

        pygame.draw.line(
            self.game.display, Color.white,
            (x - (s * math.sqrt(130) / 12) * math.cos(math.atan(7 / 9) - a),
             y + (s * math.sqrt(130) / 12) * math.sin(math.atan(7 / 9) - a)),
            (x + s * math.cos(a), y + s * math.sin(a)))

        pygame.draw.line(
            self.game.display, Color.white,
            (x - (s * math.sqrt(2) / 2) * math.cos(a + math.pi / 4),
             y - (s * math.sqrt(2) / 2) * math.sin(a + math.pi / 4)),
            (x - (s * math.sqrt(2) / 2) * math.cos(-a + math.pi / 4),
             y + (s * math.sqrt(2) / 2) * math.sin(-a + math.pi / 4)))
        if t:
            pygame.draw.line(
                self.game.display, Color.white,
                (x - s * math.cos(a),
                 y - s * math.sin(a)),
                (x - (s * math.sqrt(5) / 4) * math.cos(a + math.pi / 6),
                 y - (s * math.sqrt(5) / 4) * math.sin(a + math.pi / 6)))
            pygame.draw.line(
                self.game.display, Color.white,
                (x - s * math.cos(-a),
                 y + s * math.sin(-a)),
                (x - (s * math.sqrt(5) / 4) * math.cos(-a + math.pi / 6),
                 y + (s * math.sqrt(5) / 4) * math.sin(-a + math.pi / 6)))

    def killPlayer(self):
        # Reset the player
        self.x = Display.width / 2
        self.y = Display.height / 2
        self.thrust = False
        self.dir = -90
        self.hspeed = 0
        self.vspeed = 0
