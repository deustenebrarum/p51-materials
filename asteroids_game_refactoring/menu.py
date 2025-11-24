import pygame
from constants import Color, Display
from typing import TYPE_CHECKING

from game_object import GameObject
from utilities import draw_text

if TYPE_CHECKING:
    from game import Game


class Menu(GameObject):
    def __init__(self, game: Game):
        self.game = game

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game.quit()
            if event.type == pygame.KEYDOWN:
                self.game.start_levels()

    def draw(self):
        self.game.display.fill(Color.black)
        draw_text(self.game.display, "ASTEROIDS", Color.white,
                  Display.width / 2, Display.height / 2, 100)
        draw_text(self.game.display, "Press any key to START",
                  Color.white,
                  Display.width / 2, Display.height / 2 + 100, 50)
