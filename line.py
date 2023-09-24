import pygame
from options import GameObject
import config

class Line(GameObject):
    def __init__(self, x, y, w, h, color, special_effect=None):
        """
        Initialize the Line object.

        Args:
            x (int): The x-coordinate of the starting point of the line.
            y (int): The y-coordinate of the starting point of the line.
            w (int): The x-coordinate of the ending point of the line.
            h (int): The y-coordinate of the ending point of the line.
            color (str): The color of the line.
            special_effect (optional): The special effect of the line.

        Returns:
            None
        """
        super().__init__(x, y, w, h)
        self.color = color
        self.x =x
        self.y =y
        self.w =w
        self.h =h
        self.special_effect = special_effect

    def draw(self, surface):
        """
        Draw the Line on the given surface.

        Args:
            surface (pygame.Surface): The surface to draw the Line on.

        Returns:
            None
        """
        pygame.draw.line(surface, self.color, (self.x, self.y), (self.w, self.h), 3)
