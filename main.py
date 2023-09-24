import pygame
import sys

from collections import defaultdict


class Game:
    def __init__(self, caption, width, height, back_image_filename, frame_rate):
        """
        Initialize the game.

        Args:
            caption (str): The caption for the game window.
            width (int): The width of the game window.
            height (int): The height of the game window.
            back_image_filename (str): The filename of the background image.
            frame_rate (int): The frame rate of the game.

        Returns:
            None
        """
        self.background_image = pygame.image.load(back_image_filename)
        self.frame_rate = frame_rate
        self.game_over = False
        self.objects = []
        pygame.mixer.init(44100, -16, 2, 4096)
        pygame.init()
        pygame.font.init()
        self.surface = pygame.display.set_mode((width, height))
        pygame.display.set_caption(caption)
        self.clock = pygame.time.Clock()
        self.keydown_handlers = defaultdict(list)
        self.keyup_handlers = defaultdict(list)
        self.mouse_handlers = []

    def update(self):
        """
        Update the game state.

        Returns:
            None
        """
        for o in self.objects:
            o.update()

    def draw(self):
        """
        Draw the game objects on the game surface.

        Returns:
            None
        """
        for o in self.objects:
            o.draw(self.surface)

    def handle_events(self):
        """
        Handle user input events.

        Returns:
            None
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                for handler in self.keydown_handlers[event.key]:
                    handler(event.key)
            elif event.type == pygame.KEYUP:
                for handler in self.keyup_handlers[event.key]:
                    handler(event.key)
            elif event.type in (pygame.MOUSEBUTTONDOWN, pygame.MOUSEBUTTONUP, pygame.MOUSEMOTION):
                for handler in self.mouse_handlers:
                    handler(event.type, event.pos)

    def run(self):
        """
        Run the game loop.

        Returns:
            None
        """
        while not self.game_over:
            self.surface.blit(self.background_image, (0, 0))

            self.handle_events()
            self.update()
            self.draw()

            pygame.display.update()
            self.clock.tick(self.frame_rate)