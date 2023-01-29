import pygame
import Ball


class BlockBase(pygame.Rect):

    def __init__(self, left, top, width, height):
        super().__init__(left, top, width, height)

    def process_collision(self, ball: Ball):
        if not ball.colliderect(self):
            return

        # distance_x - distance between the ball and horizontally hit block
        if ball.direction_x > 0:  # the ball is heading ->
            # distance between right side of the ball and left side of the block
            distance_x = ball.right - self.left
        else:  # the ball is heading <-
            # distance between left side of the ball and right side of the block
            distance_x = self.right - ball.left

        # distance_y - distance between the ball and horizontally hit block
        if ball.direction_y > 0:  # the ball is heading downwards
            # distance between the ball bottom and the block top
            distance_y = ball.bottom - self.top
        else:  # the ball is heading upwards
            # distance between the ball top and the block bottom
            distance_y = self.bottom - ball.top

        if abs(distance_x) <= ball.radius and abs(distance_y) <= ball.radius:  # both distances are small
            # the ball will hit corner of the block => need to flip both directions
            ball.direction_x, ball.direction_y = -ball.direction_x, -ball.direction_y
        elif distance_x > distance_y:  # horizontal distance a bigger
            # the ball will hit top or bottom => need to flip vertical direction
            ball.direction_y = -ball.direction_y
        elif distance_y > distance_x:  # vertical distance a bigger
            # the ball will hit left or right => need to flip horizontal direction
            ball.direction_x = -ball.direction_x

    pass
