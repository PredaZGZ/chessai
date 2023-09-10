
from Board import Board
from Translator import *

board = Board()

board.fillNaturalBoard()
board.printBoard()

while True:
    sq1 = input("Enter starting square: ")
    sq2 = input("Enter ending square: ")
    print(board.move(sq1, sq2))
    board.printBoard()
