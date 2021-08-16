import numpy as np
from numpy.core.fromnumeric import transpose
from random import choice


KEY = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9], dtype=np.int8)


def borders_square_x(x: int, y: int):
    """Returns the extreme points of 3x3 squares"""
    if x < 3:
        Xstart = 0
        Xend = 3
    elif x < 6:
        Xstart = 3 
        Xend = 6
    elif x < 9:
        Xstart = 6
        Xend = 9

    if y < 3:
        Ystart = 0
        Yend = 3
    elif y < 6:
        Ystart = 3
        Yend = 6
    elif y < 9:
        Ystart = 6
        Yend = 9
    return Xstart, Xend, Ystart, Yend


def num_in_square(x: int, y: int , field: np.array):
    """Finding known values in a 3x3 square"""
    Xstart, Xend, Ystart, Yend = borders_square_x(x, y)
    all_varinat_in_sq = []
    for r in range(Xstart, Xend):
        for p in range(Ystart, Yend):
            if field[r][p] != 0:
                all_varinat_in_sq.append(field[r][p])
    return all_varinat_in_sq



def find_sudoku() -> list[np.array, int]:
    """Finding the correct matrix"""
    i = 0
    while True:
        field = np.array([[0, 0, 3, 0, 1, 4, 6, 7, 2],
                            [4, 7, 0, 6, 2, 3, 5, 8, 1],
                            [6, 1, 0, 0, 7, 8, 4, 9, 0],
                            [2, 3, 1, 8, 9, 0, 0, 0, 4],
                            [0, 0, 4, 2, 0, 7, 9, 1, 8],
                            [9, 8, 7, 0, 5, 1, 3, 2, 6],
                            [1, 0, 5, 3, 0, 2, 8, 4, 0],
                            [0, 0, 6, 1, 0, 9, 0, 3, 5],
                            [0, 2, 8, 7, 4, 5, 0, 0, 9]], dtype=np.int8)
        i += 1
        for x in range(9):
            for y in range(9):
                if field[x][y] == 0:
                    transpose_field = field.transpose()
                    all_variant = []
                    for n in KEY:
                        if (n not in field[x] and n not in transpose_field[y]
                                     and n not in num_in_square(x, y , field)):
                            all_variant.append(n)
                    if len(all_variant) != 0:
                        field[x][y] = choice(all_variant)
        if 0 not in field:
            return field, i
        

if __name__ == "__main__":
       finish_variant, number_options = find_sudoku()
       print(finish_variant, '\nVariant №:', number_options)
