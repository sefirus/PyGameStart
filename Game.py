import pygame

from Ball import Ball
from Block import Block
from Paddle import Paddle


class Game:
    SCREEN_WIDTH, SCREEN_HEIGHT = 1200, 800
    FPS = 120

    def adjust_difficulty(self):
        if int(self.args.difficulty) == 1:
            self.args.paddle_width = 330
            self.diff = 0.2
        elif int(self.args.difficulty) == 2:
            self.args.paddle_width = 270
            self.diff = 0.5
        else:
            self.args.paddle_width = 240
            self.diff = 0.7

    def __init__(self, args):
        self.args = args
        self.adjust_difficulty()
        # paddle settings
        paddle_w = int(self.args.paddle_width)
        paddle_h = int(self.args.paddle_height)
        self.paddle_speed = float(self.args.paddle_speed)
        self.paddle = Paddle(paddle_w, paddle_h, self.paddle_speed, Game.SCREEN_HEIGHT, Game.SCREEN_WIDTH)
        # ball settings
        ball_radius = int(self.args.ball_radius)
        ball_speed = int(self.args.ball_speed)
        self.ball = Ball(ball_radius, ball_speed, Game.SCREEN_HEIGHT, Game.SCREEN_WIDTH)
        # blocks settings
        self.block_list = [Block(i, j) for i in range(7) for j in range(4)]

    def process_bounds_collisions(self):
        if self.ball.centerx < self.ball.radius - self.ball.speed \
                or self.ball.centerx > Game.SCREEN_WIDTH - self.ball.radius + self.ball.speed:
            self.ball.direction_x = -self.ball.direction_x
        if self.ball.centery < self.ball.radius - self.ball.speed:
            self.ball.direction_y = -self.ball.direction_y

    def process_blocks_collisions(self):
        if self.ball.colliderect(self.paddle) and self.ball.direction_y > 0:
            self.paddle.process_collision(self.ball)

        hit_index = self.ball.collidelist(self.block_list)
        if hit_index != -1:
            hit_rect = self.block_list.pop(hit_index)
            hit_rect.process_collision(self.ball)
            self.ball.speed += self.diff
            self.paddle.speed += 3 * self.diff

    def run(self):
        pygame.init()
        sc = pygame.display.set_mode((Game.SCREEN_WIDTH, Game.SCREEN_HEIGHT))
        clock = pygame.time.Clock()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
            sc.fill((0, 0, 0))
            # drawing blocks
            [pygame.draw.rect(sc, block.color, block) for color, block in enumerate(self.block_list)]
            pygame.draw.rect(sc, pygame.Color('orange'), self.paddle)
            pygame.draw.circle(sc, pygame.Color('white'), self.ball.center, self.ball.radius)
            # ball movement
            self.ball.x += self.ball.speed * self.ball.direction_x
            self.ball.y += self.ball.speed * self.ball.direction_y
            # collision with bounds
            self.process_bounds_collisions()
            # collision with blocks
            self.process_blocks_collisions()
            # win, game over
            if self.ball.bottom > Game.SCREEN_HEIGHT:
                print('Game over!')
                exit()
            elif not len(self.block_list):
                print('Congrats!')
                exit()
            # control
            key = pygame.key.get_pressed()
            if key[pygame.K_LEFT] and self.paddle.left > 0:
                self.paddle.left -= self.paddle_speed
            if key[pygame.K_RIGHT] and self.paddle.right < Game.SCREEN_WIDTH:
                self.paddle.right += self.paddle_speed
            # update screen
            pygame.display.flip()
            clock.tick(Game.FPS)

    pass
