from BlockBase import BlockBase


class Paddle(BlockBase):
    def __init__(self, width: int, height: int, speed: float, screen_h: int, screen_w: int):
        self.width = width
        self.height = height
        self.speed = speed
        super().__init__(screen_w // 2 - width // 2, screen_h - height - 10, width, height)

    pass
