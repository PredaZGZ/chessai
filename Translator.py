from Constants import *


def square_to_tuple(square):
    lst = list(square)
    for i in lst:
        if i in columns:
            lst[0] = columns.index(i)
        else:
            lst[1] = 8 - int(i)
    return tuple(lst)


def tuple_to_square(tup):
    return columns[tup[0]] + str(8 - tup[1])


def piece_to_points(piece):
    for i in PointsConverter:
        if i[0] == piece:
            return i[1]
