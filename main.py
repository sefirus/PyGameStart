import argparse
from Game import Game

parser = argparse.ArgumentParser()
parser.add_argument('-pw', '--paddle-width', default=330, help='customize paddle width')
parser.add_argument('-ph', '--paddle-height', default=35, help='customize paddle height')
parser.add_argument('-ps', '--paddle-speed', default=7, help='customize default paddle speed')
parser.add_argument('-dr', '--ball-radius', default=20, help='customize ball radius')
parser.add_argument('-bs', '--ball-speed', default=3, help='customize default ball speed')
parser.add_argument('-d', '--difficulty', default=1, choices=['3', '2', '1'], help='set difficulty level; from 1 to 3')

args = parser.parse_args()

Game(args).run()
