import pygame
from options import GameObject


class Figure(GameObject):
    def __init__(self, x, y, r, color, speed):
        """
        Initialize the Figure object.

        Args:
            x (int): The x-coordinate of the center of the figure.
            y (int): The y-coordinate of the center of the figure.
            r (int): The radius of the figure.
            color (str): The color of the figure.
            speed (int): The speed of the figure.

        Returns:
            None
        """
        super().__init__(x - r, y - r, r * 2, r * 2, speed)
        self.radius = r
        self.diameter = r * 2
        self.color = color

    def draw(self, surface):
        """
        Draw the Figure on the given surface.

        Args:
            surface (pygame.Surface): The surface to draw the Figure on.

        Returns:
            None
        """
        pygame.draw.circle(surface, self.color, self.center, self.radius)

    def update(self):
        """
        Update the state of the Figure.

        Returns:
            None
        """
        super().update()