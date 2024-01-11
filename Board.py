from Constants import *
from Translator import *
import random


class Board:
    def __init__(self):
        self.board = [[0 for x in range(8)] for y in range(8)]
        self.white_points = 0
        self.black_points = 0
        self.moves = []
        self.whiteTurn = True

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

    def isEmpty(self, sq):
        coords = square_to_tuple(sq)
        piece = self.getBoardValue(coords[0], coords[1])
        if piece == 0:
            return True
        else:
            return False

    def isWhite(self, sq):
        coords = square_to_tuple(sq)
        piece = self.getBoardValue(coords[0], coords[1])
        if piece % 2 > 0:
            return True
        else:
            return False

    def fillNaturalBoard(self):
        # I have to make a deep copy of NaturalBoard because
        # if not it will be a reference to the same object
        # causing NaturalBoard be modified if board does
        for i in range(len(self.board)):
            for j in range(len(self.board)):
                self.board[i][j] = NaturalBoard[i][j]
        self.moves = []
        self.calculatePoints()
        self.whiteTurn = True
        return self.board

    def calculatePoints(self):
        for i in self.board:
            for j in i:
                if j != 0:
                    if j % 2 > 0:
                        self.white_points += piece_to_points(j)
                    elif j % 2 == 0:
                        self.black_points += piece_to_points(j)

        return [self.white_points, self.black_points]

    def move(self, coords1, coords2):
        coords1 = square_to_tuple(coords1)
        coords2 = square_to_tuple(coords2)
        msg = self.checkmove(coords1, coords2)
        if msg == "OK":
            self.setBoardValue(
                coords2[0], coords2[1], self.getBoardValue(coords1[0], coords1[1]))

            self.setBoardValue(coords1[0], coords1[1], 0)

            self.moves.append([self.whiteTurn, tuple_to_square(
                coords1), tuple_to_square(coords2)])

            self.whiteTurn = not self.whiteTurn
            return msg
        else:
            return msg

    def checkmove(self, coords1, coords2):
        if self.getBoardValue(coords1[0], coords1[1]) % 2 == 0 and self.whiteTurn:
            return "It is White Turn"
        if self.getBoardValue(coords1[0], coords1[1]) % 2 > 0 and not self.whiteTurn:
            return "It is Black Turn"
        if coords1[0] == coords2[0] and coords1[1] == coords2[1]:
            return "Destination same as starting position"
        if self.getBoardValue(coords1[0], coords1[1]) == 0:
            return "No piece at starting position"
        return "OK"

    def makeRandomMove(self, color):
        possible_moves = []
        if color == "white":
            options = [1, 3, 5, 7, 9, 11]
        elif color == "black":
            options = [2, 4, 6, 8, 10, 12]
        for i in range(len(self.board)):
            for j in range(len(self.board)):
                if self.board[i][j] in options:
                    moves = self.getMovesOfPiece(tuple_to_square((j, i)))
                    if len(moves) > 0:
                        possible_moves.append([tuple_to_square((j, i)), moves])

        if len(possible_moves) > 0:
            piece = random.choice(possible_moves)
            move = random.choice(piece[1])
            return [piece[0], move]

    def getMovesOfPiece(self, coords):
        coords = square_to_tuple(coords)
        piece = self.getBoardValue(coords[0], coords[1])
        moves = []
        # White Pawn
        if piece == 1:
            # Check if pawn can go forward one
            if 0 <= coords[1]-1 < 8 and self.getBoardValue(coords[0], coords[1]-1) == 0:
                moves.append((coords[0], coords[1] - 1))
            # Check if pawn can go forward two
            if coords[1] == 6 and 0 <= coords[1]-2 < 8 and self.getBoardValue(coords[0], coords[1]-2) == 0:
                moves.append((coords[0], coords[1] - 2))
            # Check if pawn can take a piece at left diagonal
            if 0 <= coords[0]-1 < 8 and 0 <= coords[1]-1 < 8 and self.getBoardValue(coords[0]-1, coords[1]-1) != 0:
                moves.append((coords[0]-1, coords[1] - 1))
            # Check if pawn can take a piece at right diagonal
            if 0 <= coords[0]+1 < 8 and 0 <= coords[1]-1 < 8 and self.getBoardValue(coords[0]+1, coords[1]-1) != 0:
                moves.append((coords[0]+1, coords[1] - 1))
            # Check if pawn can en passant
            if coords[1] == 3:
                # Check if there is a black pawn to the left for en passant
                if 0 <= coords[0]-1 < 8 and self.getBoardValue(coords[0]-1, coords[1]) == 2:
                    moves.append((coords[0]-1, coords[1]-1))
                # Check if there is a black pawn to the right for en passant
                if 0 <= coords[0]+1 < 8 and self.getBoardValue(coords[0]+1, coords[1]) == 2:
                    moves.append((coords[0]+1, coords[1]-1))
            # Black Pawn
        elif piece == 2:
            # Check if pawn can go forward one
            if 0 <= coords[1]+1 < 8 and self.getBoardValue(coords[0], coords[1]+1) == 0:
                moves.append((coords[0], coords[1] + 1))
            # Check if pawn can go forward two
            if coords[1] == 1 and 0 <= coords[1]+2 < 8 and self.getBoardValue(coords[0], coords[1]+2) == 0:
                moves.append((coords[0], coords[1] + 2))
            # Check if pawn can take a piece at left diagonal
            if 0 <= coords[0]-1 < 8 and 0 <= coords[1]+1 < 8 and self.getBoardValue(coords[0]-1, coords[1]+1) != 0:
                moves.append((coords[0]-1, coords[1] + 1))
            # Check if pawn can take a piece at right diagonal
            if 0 <= coords[0]+1 < 8 and 0 <= coords[1]+1 < 8 and self.getBoardValue(coords[0]+1, coords[1]+1) != 0:
                moves.append((coords[0]+1, coords[1] + 1))
            # Check if pawn can en passant
            if coords[1] == 4:
                # Check if there is a white pawn to the left for en passant
                if 0 <= coords[0]-1 < 8 and self.getBoardValue(coords[0]-1, coords[1]) == 1:
                    moves.append((coords[0]-1, coords[1]+1))
                # Check if there is a white pawn to the right for en passant
                if 0 <= coords[0]+1 < 8 and self.getBoardValue(coords[0]+1, coords[1]) == 1:
                    moves.append((coords[0]+1, coords[1]+1))
        # Knight
        elif piece == 5 or piece == 6:
            # Check if knight can go forward two and left one
            if coords[1] > 1 and coords[0] > 0:
                if self.getBoardValue(coords[0]-1, coords[1]-2) == 0 or self.getBoardValue(coords[0]-1, coords[1]-2) % 2 != piece % 2:
                    moves.append((coords[0]-1, coords[1]-2))
            # Check if knight can go forward two and right one
            if coords[1] > 1 and coords[0] < 7:
                if self.getBoardValue(coords[0]+1, coords[1]-2) == 0 or self.getBoardValue(coords[0]+1, coords[1]-2) % 2 != piece % 2:
                    moves.append((coords[0]+1, coords[1]-2))
            # Check if knight can go forward one and left two
            if coords[1] > 0 and coords[0] > 1:
                if self.getBoardValue(coords[0]-2, coords[1]-1) == 0 or self.getBoardValue(coords[0]-2, coords[1]-1) % 2 != piece % 2:
                    moves.append((coords[0]-2, coords[1]-1))
            # Check if knight can go forward one and right two
            if coords[1] > 0 and coords[0] < 6:
                if self.getBoardValue(coords[0]+2, coords[1]-1) == 0 or self.getBoardValue(coords[0]+2, coords[1]-1) % 2 != piece % 2:
                    moves.append((coords[0]+2, coords[1]-1))
            # Check if knight can go backward two and left one
            if coords[1] < 6 and coords[0] > 0:
                if self.getBoardValue(coords[0]-1, coords[1]+2) == 0 or self.getBoardValue(coords[0]-1, coords[1]+2) % 2 != piece % 2:
                    moves.append((coords[0]-1, coords[1]+2))
            # Check if knight can go backward two and right one
            if coords[1] < 6 and coords[0] < 7:
                if self.getBoardValue(coords[0]+1, coords[1]+2) == 0 or self.getBoardValue(coords[0]+1, coords[1]+2) % 2 != piece % 2:
                    moves.append((coords[0]+1, coords[1]+2))
            # Check if knight can go backward one and left two
            if coords[1] < 7 and coords[0] > 1:
                if self.getBoardValue(coords[0]-2, coords[1]+1) == 0 or self.getBoardValue(coords[0]-2, coords[1]+1) % 2 != piece % 2:
                    moves.append((coords[0]-2, coords[1]+1))
            # Check if knight can go backward one and right two
            if coords[1] < 7 and coords[0] < 6:
                if self.getBoardValue(coords[0]+2, coords[1]+1) == 0 or self.getBoardValue(coords[0]+2, coords[1]+1) % 2 != piece % 2:
                    moves.append((coords[0]+2, coords[1]+1))

        # Bishop
        elif piece == 8 or piece == 7:
            # Check if bishop can go forward left
            for i in range(1, 8):
                if coords[0]-i < 0 or coords[1]-i < 0:
                    break
                if self.getBoardValue(coords[0]-i, coords[1]-i) == 0:
                    moves.append((coords[0]-i, coords[1]-i))
                elif self.getBoardValue(coords[0]-i, coords[1]-i) % 2 != piece % 2:
                    moves.append((coords[0]-i, coords[1]-i))
                    break
                else:
                    break
            # Check if bishop can go forward right
            for i in range(1, 8):
                if coords[0]+i > 7 or coords[1]-i < 0:
                    break
                if self.getBoardValue(coords[0]+i, coords[1]-i) == 0:
                    moves.append((coords[0]+i, coords[1]-i))
                elif self.getBoardValue(coords[0]+i, coords[1]-i) % 2 != piece % 2:
                    moves.append((coords[0]+i, coords[1]-i))
                    break
                else:
                    break
            # Check if bishop can go backward left
            for i in range(1, 8):
                if coords[0]-i < 0 or coords[1]+i > 7:
                    break
                if self.getBoardValue(coords[0]-i, coords[1]+i) == 0:
                    moves.append((coords[0]-i, coords[1]+i))
                elif self.getBoardValue(coords[0]-i, coords[1]+i) % 2 != piece % 2:
                    moves.append((coords[0]-i, coords[1]+i))
                    break
                else:
                    break
            # Check if bishop can go backward right
            for i in range(1, 8):
                if coords[0]+i > 7 or coords[1]+i > 7:
                    break
                if self.getBoardValue(coords[0]+i, coords[1]+i) == 0:
                    moves.append((coords[0]+i, coords[1]+i))
                elif self.getBoardValue(coords[0]+i, coords[1]+i) % 2 != piece % 2:
                    moves.append((coords[0]+i, coords[1]+i))
                    break
                else:
                    break

        # Rook
        elif piece == 3 or piece == 4:
            # Check if rook can go forward
            for i in range(1, 8):
                if coords[1]-i < 0:
                    break
                if self.getBoardValue(coords[0], coords[1]-i) == 0:
                    moves.append((coords[0], coords[1]-i))
                elif self.getBoardValue(coords[0], coords[1]-i) % 2 != piece % 2:
                    moves.append((coords[0], coords[1]-i))
                    break
                else:
                    break
            # Check if rook can go backward
            for i in range(1, 8):
                if coords[1]+i > 7:
                    break
                if self.getBoardValue(coords[0], coords[1]+i) == 0:
                    moves.append((coords[0], coords[1]+i))
                elif self.getBoardValue(coords[0], coords[1]+i) % 2 != piece % 2:
                    moves.append((coords[0], coords[1]+i))
                    break
                else:
                    break
            # Check if rook can go left
            for i in range(1, 8):
                if coords[0]-i < 0:
                    break
                if self.getBoardValue(coords[0]-i, coords[1]) == 0:
                    moves.append((coords[0]-i, coords[1]))
                elif self.getBoardValue(coords[0]-i, coords[1]) % 2 != piece % 2:
                    moves.append((coords[0]-i, coords[1]))
                    break
                else:
                    break
            # Check if rook can go right
            for i in range(1, 8):
                if coords[0]+i > 7:
                    break
                if self.getBoardValue(coords[0]+i, coords[1]) == 0:
                    moves.append((coords[0]+i, coords[1]))
                elif self.getBoardValue(coords[0]+i, coords[1]) % 2 != piece % 2:
                    moves.append((coords[0]+i, coords[1]))
                    break
                else:
                    break

        # Queen
        elif piece == 9 or piece == 10:
            # Check if queen can go forward
            for i in range(1, 8):
                if coords[1]-i < 0:
                    break
                if self.getBoardValue(coords[0], coords[1]-i) == 0:
                    moves.append((coords[0], coords[1]-i))
                elif self.getBoardValue(coords[0], coords[1]-i) % 2 != piece % 2:
                    moves.append((coords[0], coords[1]-i))
                    break
                else:
                    break
            # Check if queen can go backward
            for i in range(1, 8):
                if coords[1]+i > 7:
                    break
                if self.getBoardValue(coords[0], coords[1]+i) == 0:
                    moves.append((coords[0], coords[1]+i))
                elif self.getBoardValue(coords[0], coords[1]+i) % 2 != piece % 2:
                    moves.append((coords[0], coords[1]+i))
                    break
                else:
                    break
            # Check if queen can go left
            for i in range(1, 8):
                if coords[0]-i < 0:
                    break
                if self.getBoardValue(coords[0]-i, coords[1]) == 0:
                    moves.append((coords[0]-i, coords[1]))
                elif self.getBoardValue(coords[0]-i, coords[1]) % 2 != piece % 2:
                    moves.append((coords[0]-i, coords[1]))
                    break
                else:
                    break
            # Check if queen can go right
            for i in range(1, 8):
                if coords[0]+i > 7:
                    break
                if self.getBoardValue(coords[0]+i, coords[1]) == 0:
                    moves.append((coords[0]+i, coords[1]))
                elif self.getBoardValue(coords[0]+i, coords[1]) % 2 != piece % 2:
                    moves.append((coords[0]+i, coords[1]))
                    break
                else:
                    break
            # Check if queen can go forward left
            for i in range(1, 8):
                if coords[0]-i < 0 or coords[1]-i < 0:
                    break
                if self.getBoardValue(coords[0]-i, coords[1]-i) == 0:
                    moves.append((coords[0]-i, coords[1]-i))
                elif self.getBoardValue(coords[0]-i, coords[1]-i) % 2 != piece % 2:
                    moves.append((coords[0]-i, coords[1]-i))
                    break
                else:
                    break
            # Check if queen can go forward right
            for i in range(1, 8):
                if coords[0]+i > 7 or coords[1]-i < 0:
                    break
                if self.getBoardValue(coords[0]+i, coords[1]-i) == 0:
                    moves.append((coords[0]+i, coords[1]-i))
                elif self.getBoardValue(coords[0]+i, coords[1]-i) % 2 != piece % 2:
                    moves.append((coords[0]+i, coords[1]-i))
                    break
                else:
                    break
            # Check if queen can go backward left
            for i in range(1, 8):
                if coords[0]-i < 0 or coords[1]+i > 7:
                    break
                if self.getBoardValue(coords[0]-i, coords[1]+i) == 0:
                    moves.append((coords[0]-i, coords[1]+i))
                elif self.getBoardValue(coords[0]-i, coords[1]+i) % 2 != piece % 2:
                    moves.append((coords[0]-i, coords[1]+i))
                    break
                else:
                    break
            # Check if queen can go backward right
            for i in range(1, 8):
                if coords[0]+i > 7 or coords[1]+i > 7:
                    break
                if self.getBoardValue(coords[0]+i, coords[1]+i) == 0:
                    moves.append((coords[0]+i, coords[1]+i))
                elif self.getBoardValue(coords[0]+i, coords[1]+i) % 2 != piece % 2:
                    moves.append((coords[0]+i, coords[1]+i))
                    break
                else:
                    break

        # King
        elif piece == 11 or piece == 12:
            # Check if king can go forward
            if coords[1]-1 >= 0:
                if self.getBoardValue(coords[0], coords[1]-1) == 0 or self.getBoardValue(coords[0], coords[1]-1) % 2 != piece % 2:
                    moves.append((coords[0], coords[1]-1))
            # Check if king can go backward
            if coords[1]+1 <= 7:
                if self.getBoardValue(coords[0], coords[1]+1) == 0 or self.getBoardValue(coords[0], coords[1]+1) % 2 != piece % 2:
                    moves.append((coords[0], coords[1]+1))
            # Check if king can go left
            if coords[0]-1 >= 0:
                if self.getBoardValue(coords[0]-1, coords[1]) == 0 or self.getBoardValue(coords[0]-1, coords[1]) % 2 != piece % 2:
                    moves.append((coords[0]-1, coords[1]))
            # Check if king can go right
            if coords[0]+1 <= 7:
                if self.getBoardValue(coords[0]+1, coords[1]) == 0 or self.getBoardValue(coords[0]+1, coords[1]) % 2 != piece % 2:
                    moves.append((coords[0]+1, coords[1]))
            # Check if king can go forward left
            if coords[0]-1 >= 0 and coords[1]-1 >= 0:
                if self.getBoardValue(coords[0]-1, coords[1]-1) == 0 or self.getBoardValue(coords[0]-1, coords[1]-1) % 2 != piece % 2:
                    moves.append((coords[0]-1, coords[1]-1))
            # Check if king can go forward right
            if coords[0]+1 <= 7 and coords[1]-1 >= 0:
                if self.getBoardValue(coords[0]+1, coords[1]-1) == 0 or self.getBoardValue(coords[0]+1, coords[1]-1) % 2 != piece % 2:
                    moves.append((coords[0]+1, coords[1]-1))
            # Check if king
            if coords[0]-1 >= 0 and coords[1]+1 <= 7:
                if self.getBoardValue(coords[0]-1, coords[1]+1) == 0 or self.getBoardValue(coords[0]-1, coords[1]+1) % 2 != piece % 2:
                    moves.append((coords[0]-1, coords[1]+1))
            # Check if king
            if coords[0]+1 <= 7 and coords[1]+1 <= 7:
                if self.getBoardValue(coords[0]+1, coords[1]+1) == 0 or self.getBoardValue(coords[0]+1, coords[1]+1) % 2 != piece % 2:
                    moves.append((coords[0]+1, coords[1]+1))

        for i in range(len(moves)):
            moves[i] = tuple_to_square(moves[i])

        return moves

    def getBoardOfMoves(self, moves):
        board = [[0 for x in range(8)] for y in range(8)]
        for move in moves:
            coords = square_to_tuple(move)
            board[coords[1]][coords[0]] = 1
        return board
