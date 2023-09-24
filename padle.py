import pygame

import config as c
from options import GameObject

class Paddle(GameObject):
    def __init__(self, x, y, r,h,color):
        GameObject.__init__(self, x, y, r, h)
        self.color = color
        self.moving_up = False
        self.moving_down = False
        self.moving_left = False
        self.moving_right = False
        super().__init__(x - r, y - r, r * 2, r * 2)
        self.radius = r
        self.diameter = r * 2
        self.color = color

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, self.center, self.radius)

    def handle(self, key):
        if key == pygame.K_LEFT:
            self.moving_left = not self.moving_left
        if key == pygame.K_RIGHT:
            self.moving_right = not self.moving_right
        if key == pygame.K_UP:
            self.moving_up = not self.moving_up
        if key == pygame.K_DOWN:
            self.moving_down = not self.moving_down

    def update(self):
        if self.moving_left:
            dx = self.left
        elif self.moving_right:
            dx = c.screen_width - self.right
        if self.moving_up:
            dy = self.top
        elif self.moving_down:
            dy = c.screen_height - self.bottom
        else:
            return
        self.move(dx, dy)
