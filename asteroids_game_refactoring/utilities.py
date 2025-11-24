import pygame

from constants import Color


def draw_text(surface: pygame.Surface, message: str,
              color: tuple[int, int, int],
              x: float, y: float, size: int, center=True):
    '''Function to draw text on the screen'''
    font = pygame.font.SysFont("Calibri", size)
    screen_text = font.render(message, True, color)
    if center:
        rect = screen_text.get_rect()
        rect.center = (int(x), int(y))
    else:
        rect = pygame.Rect(x, y, size, size)
    surface.blit(screen_text, rect)


def is_colliding(centerX: int, centerY: int,
                 centerXTo: int, centerYTo: int, radius: int):
    '''Create function to check for collision'''
    is_horizontal_collided = (
        centerX > centerXTo - radius and
        centerX < centerXTo + radius
    )
    is_vertical_collided = (
        centerY > centerYTo - radius and
        centerY < centerYTo + radius
    )
    return is_horizontal_collided and is_vertical_collided
