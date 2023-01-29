import pygame

from Ball import Ball
from Block import Block
from Paddle import Paddle


class Game:
    SCREEN_WIDTH, SCREEN_HEIGHT = 1200, 800
    FPS = 60

    def __init__(self, args):
        self.args = args

    @staticmethod
    def process_bounds_collisions(ball: Ball):
        if ball.centerx < ball.radius or ball.centerx > Game.SCREEN_WIDTH - ball.radius:
            ball.direction_x = -ball.direction_x
        if ball.centery < ball.radius:
            ball.direction_y = -ball.direction_y

    @staticmethod
    def process_blocks_collisions(ball: Ball, paddle: Paddle, blocks: list[Block], diff: float):
        if ball.colliderect(paddle) and ball.direction_y > 0:
            paddle.process_collision(ball)

        hit_index = ball.collidelist(blocks)
        if hit_index != -1:
            hit_rect = blocks.pop(hit_index)
            hit_rect.process_collision(ball)
            ball.speed += diff
            paddle.speed += 3 * diff

    def run(self):
        # paddle settings
        paddle_w = int(self.args.paddle_width)
        paddle_h = int(self.args.paddle_height)
        paddle_speed = float(self.args.paddle_speed)
        paddle = Paddle(paddle_w, paddle_h, paddle_speed, Game.SCREEN_HEIGHT, Game.SCREEN_WIDTH)
        # ball settings
        ball_radius = int(self.args.ball_radius)
        ball_speed = int(self.args.ball_speed)
        diff = float(self.args.difficulty_delta)
        ball = Ball(ball_radius, ball_speed, Game.SCREEN_HEIGHT, Game.SCREEN_WIDTH)
        # blocks settings
        block_list = [Block(i, j) for i in range(7) for j in range(4)]

        pygame.init()
        sc = pygame.display.set_mode((Game.SCREEN_WIDTH, Game.SCREEN_HEIGHT))
        clock = pygame.time.Clock()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
            sc.fill((0, 0, 0))
            # drawing blocks
            [pygame.draw.rect(sc, block.color, block) for color, block in enumerate(block_list)]
            pygame.draw.rect(sc, pygame.Color('orange'), paddle)
            pygame.draw.circle(sc, pygame.Color('white'), ball.center, ball_radius)
            # ball movement
            ball.x += ball_speed * ball.direction_x
            ball.y += ball_speed * ball.direction_y
            # collision with bounds
            Game.process_bounds_collisions(ball)
            # collision with blocks
            Game.process_blocks_collisions(ball, paddle, block_list, diff)
            # win, game over
            if ball.bottom > Game.SCREEN_HEIGHT:
                print('Game over!')
                exit()
            elif not len(block_list):
                print('Congrats!')
                exit()
            # control
            key = pygame.key.get_pressed()
            if key[pygame.K_LEFT] and paddle.left > 0:
                paddle.left -= paddle_speed
            if key[pygame.K_RIGHT] and paddle.right < Game.SCREEN_WIDTH:
                paddle.right += paddle_speed
            # update screen
            pygame.display.flip()
            clock.tick(Game.FPS)

    pass
