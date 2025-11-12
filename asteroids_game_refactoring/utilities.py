import pygame


def draw_text(gameDisplay: pygame.Surface, message: str,
              color: pygame.Color,
              x: int, y: int, size: int, center=True):
    '''Function to draw text on the screen'''
    font = pygame.font.SysFont("Calibri", size)
    screen_text = font.render(message, True, color)
    if center:
        rect = screen_text.get_rect()
        rect.center = (x, y)
    else:
        rect = pygame.Rect(x, y, size, size)
    gameDisplay.blit(screen_text, rect)


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
