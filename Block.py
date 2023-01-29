from random import randrange as rnd
from BlockBase import BlockBase


class Block(BlockBase):

    def __init__(self, poz_x: int, poz_y: int):
        super().__init__(10 + 170 * poz_x, 10 + 70 * poz_y, 150, 50)
        self.color = (rnd(30, 156), rnd(30, 256), rnd(30, 156))

    pass
