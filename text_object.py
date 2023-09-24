import pygame


class TextObject:
    def __init__(self, x, y, text_func, color, font_name, font_size):
        """
        Initialize the TextObject.

        Args:
            x (int): The x-coordinate of the top-left corner of the TextObject.
            y (int): The y-coordinate of the top-left corner of the TextObject.
            text_func (function): A function that returns the text to be displayed.
            color (str): The color of the text.
            font_name (str): The name of the font to be used.
            font_size (int): The size of the font.

        Returns:
            None
        """
        self.pos = (x, y)
        self.text_func = text_func
        self.color = color
        self.font = pygame.font.SysFont(font_name, font_size)
        self.bounds = self.get_surface(text_func())

    def draw(self, surface, centralized=False):
        """
        Draw the TextObject on the given surface.

        Args:
            surface (pygame.Surface): The surface to draw the TextObject on.
            centralized (bool, optional): Whether to center the text horizontally.

        Returns:
            None
        """
        text_surface, self.bounds = self.get_surface(self.text_func())
        if centralized:
            pos = (self.pos[0] - self.bounds.width // 2, self.pos[1])
        else:
            pos = self.pos
        surface.blit(text_surface, pos)

    def get_surface(self, text):
        """
        Return the text surface and its bounds.

        Args:
            text (str): The text to be displayed.

        Returns:
            pygame.Surface, pygame.Rect: The text surface and its bounds.
        """
        text_surface = self.font.render(text, False, self.color)
        return text_surface, text_surface.get_rect()

    def update(self):
        """
        Update the state of the TextObject.

        Returns:
            None
        """
        pass