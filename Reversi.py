import random
from datetime import datetime, timedelta
from reversi-master import ex
import os
import time
import pygame
from pygame.rect import Rect
from padle import Paddle
import config as c
from figure import Figure
from figure_enemy import FigureEnemy
from button import Button
from main import Game
from line import Line
from text_object import TextObject
import colors

assert os.path.isfile('sound/start.wav')


class Reversi(Game):
    def __init__(self):
        Game.__init__(self, 'Reversi', c.screen_width, c.screen_height, c.background_image, c.frame_rate)
        self.sound_effects = {name: pygame.mixer.Sound(sound) for name, sound in c.sounds_effects.items()}
        self.start_level = False
        self.line = None
        self.paddle = None
        self.figure = None
        self.figure_enemy = None
        self.menu_buttons = []
        self.is_game_running = False
        self.create_objects()
    def create_menu(self):
        def on_play(button):
            for b in self.menu_buttons:
                self.objects.remove(b)

            self.is_game_running = True
            self.start_level = True



        def on_quit(button):
            self.game_over = True
            self.is_game_running = False
            self.game_over = True

        for i, (text, click_handler) in enumerate((('PLAY', on_play), ('QUIT', on_quit))):
            b = Button(c.menu_offset_x,
                       c.menu_offset_y + (c.menu_button_h + 5) * i,
                       c.menu_button_w,
                       c.menu_button_h,
                       text,
                       click_handler,
                       padding=5)
            self.objects.append(b)
            self.menu_buttons.append(b)
            self.mouse_handlers.append(b.handle_mouse_event)

    def create_objects(self):

        self.create_lines()
        self.create_paddle()
        self.create_menu()





    def create_lines(self):
        x = c.screen_width - c.screen_height
        y = 0
        line_color = c.line_color
        lines = []
        for row in range(c.row_count+1):
            line = Line(x,
                        y,
                          x,
                          y+c.screen_height,
                        line_color)
            lines.append(line)
            self.objects.append(line)
            x = x + (c.screen_height / 8)
        y = 0
        x = c.screen_width - c.screen_height
        for col in range(c.column_count+1):
            line = Line(x,
                        y,
                          x+c.screen_height,
                          y,
                        line_color)
            lines.append(line)
            self.objects.append(line)
            y = y+(c.screen_height/8)
        self.lines = lines
    def create_figure(self, x,y):

        self.figure = Figure(x,
                         y,
                         30,
                         c.figure_color)

    def create_figure_enemy(self, x, y):

        self.figure_enemy = FigureEnemy(x,
                             y,
                             30,
                             c.figure_enemy_color)

    def create_paddle(self):
        x = c.screen_width - c.screen_height+50
        y = 50
        paddle = Paddle(x,
                        y,
                        c.paddle_radius,
                        c.paddle_radius,
                        c.paddle_color)
        self.keydown_handlers[pygame.K_DOWN].append(paddle.handle)
        self.keydown_handlers[pygame.K_RIGHT].append(paddle.handle)
        self.keyup_handlers[pygame.K_LEFT].append(paddle.handle)
        self.keyup_handlers[pygame.K_RIGHT].append(paddle.handle)
        self.paddle = paddle
        self.objects.append(self.paddle)

    def handle_ball_collisions(self):
        def intersect(obj, ball):
            edges = dict(left=Rect(obj.left, obj.top, 1, obj.height),
                         right=Rect(obj.right, obj.top, 1, obj.height),
                         top=Rect(obj.left, obj.top, obj.width, 1),
                         bottom=Rect(obj.left, obj.bottom, obj.width, 1))
            collisions = set(edge for edge, rect in edges.items() if ball.bounds.colliderect(rect))
            if not collisions:
                return None

            if len(collisions) == 1:
                return list(collisions)[0]

            if 'top' in collisions:
                if ball.centery >= obj.top:
                    return 'top'
                if ball.centerx < obj.left:
                    return 'left'
                else:
                    return 'right'

            if 'bottom' in collisions:
                if ball.centery >= obj.bottom:
                    return 'bottom'
                if ball.centerx < obj.left:
                    return 'left'
                else:
                    return 'right'

        # Hit paddle
        s = self.ball.speed
        edge = intersect(self.paddle, self.ball)
        if edge is not None:
            self.sound_effects['paddle_hit'].play()
        if edge == 'top':
            speed_x = s[0]
            speed_y = -s[1]
            if self.paddle.moving_left:
                speed_x -= 1
            elif self.paddle.moving_left:
                speed_x += 1
            self.ball.speed = speed_x, speed_y
        elif edge in ('left', 'right'):
            self.ball.speed = (-s[0], s[1])

        # Hit floor
        if self.ball.top > c.screen_height:
            self.lives -= 1
            if self.lives == 0:
                self.game_over = True
            else:
                self.create_ball()

        # Hit ceiling
        if self.ball.top < 0:
            self.ball.speed = (s[0], -s[1])

        # Hit wall
        if self.ball.left < 0 or self.ball.right > c.screen_width:
            self.ball.speed = (-s[0], s[1])

        # Hit brick
        for brick in self.bricks:
            edge = intersect(brick, self.ball)
            if not edge:
                continue

            self.sound_effects['brick_hit'].play()
            self.bricks.remove(brick)
            self.objects.remove(brick)
            self.score += self.points_per_brick

            if edge in ('top', 'bottom'):
                self.ball.speed = (s[0], -s[1])
            else:
                self.ball.speed = (-s[0], s[1])

            if brick.special_effect is not None:
                # Reset previous effect if any
                if self.reset_effect is not None:
                    self.reset_effect(self)

                # Trigger special effect
                self.effect_start_time = datetime.now()
                brick.special_effect[0](self)
                # Set current reset effect function
                self.reset_effect = brick.special_effect[1]

    def update(self):
        if not self.is_game_running:
            return

        if self.start_level:
            self.start_level = False
            self.show_message('GET READY!', centralized=True)

        if not self.bricks:
            self.show_message('YOU WIN!!!', centralized=True)
            self.is_game_running = False
            self.game_over = True
            return

        # Reset special effect if needed
        if self.reset_effect:
            if datetime.now() - self.effect_start_time >= timedelta(seconds=c.effect_duration):
                self.reset_effect(self)
                self.reset_effect = None

        self.handle_ball_collisions()
        super().update()

        if self.game_over:
            self.show_message('GAME OVER!', centralized=True)

    def show_message(self, text, color=colors.WHITE, font_name='Arial', font_size=20, centralized=False):
        message = TextObject(c.screen_width // 2, c.screen_height // 2, lambda: text, color, font_name, font_size)
        self.draw()
        message.draw(self.surface, centralized)
        pygame.display.update()
        time.sleep(c.message_duration)


def main():
    Reversi().run()


if __name__ == '__main__':
    main()
