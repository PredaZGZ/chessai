from Constants import *
from Translator import *


class Board:
    def __init__(self):
        self.board = [[0 for x in range(8)] for y in range(8)]

    def printBoard(self):
        for row in self.board:
            print(row)
        print("\n\n")

    def getBoard(self):
        return self.board

    def setBoard(self, board):
        self.board = board

    def setBoardValue(self, x, y, value):
        self.board[y][x] = value

    def getBoardValue(self, x, y):
        return self.board[y][x]

    def fillNaturalBoard(self):
        self.setBoard(NaturalBoard)

    def move(self, coords1, coords2):
        coords1 = square_to_tuple(coords1)
        coords2 = square_to_tuple(coords2)
        msg = self.checkmove(coords1, coords2)
        if msg == "OK":
            self.setBoardValue(
                coords2[0], coords2[1], self.getBoardValue(coords1[0], coords1[1]))
            self.setBoardValue(coords1[0], coords1[1], 0)
            return msg
        else:
            return msg

    def checkmove(self, coords1, coords2):
        if coords1[0] == coords2[0] and coords1[1] == coords2[1]:
            return "Destination same as starting position"
        if self.getBoardValue(coords1[0], coords1[1]) == 0:
            return "No piece at starting position"
        return "OK"
