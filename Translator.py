from Constants import *


def square_to_tuple(square):
    lst = list(square)
    for i in lst:
        if i in columns:
            lst[0] = columns.index(i)
        else:
            lst[1] = 8 - int(i)
    return tuple(lst)
