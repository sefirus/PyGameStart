import argparse
from Game import Game

parser = argparse.ArgumentParser()
parser.add_argument('-pw', '--paddle-width', default=330, help='customize paddle width')
parser.add_argument('-ph', '--paddle-height', default=35, help='customize paddle height')
parser.add_argument('-ps', '--paddle-speed', default=15, help='customize default paddle speed')
parser.add_argument('-dr', '--ball-radius', default=20, help='customize ball radius')
parser.add_argument('-bs', '--ball-speed', default=6, help='customize default ball speed')
parser.add_argument('-d', '--difficulty-delta', default=0.3, help='customize difficulty increase speed')

args = parser.parse_args()

Game(args).run()
