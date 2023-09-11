
from Board import Board
from Translator import *

board = Board()

board.fillNaturalBoard()
board.printBoard()

while True:
    sq1 = input("Enter starting square: ")
    if board.isEmpty(sq1):
        print("It is empty")
    elif (len(board.moves) == 0) or (board.moves[-1][0] != board.isWhite(sq1)):
        print(board.getMovesOfPiece(sq1))
        sq2 = input("Enter ending square: ")
        print(board.move(sq1, sq2))
    else:
        print("Is not your piece")
    board.printBoard()
    print(board.moves)
