"""
You are given a matrix of integers field of size height * width representing a game field, and also a matrix of inte-
gers figure of size 3 * 3 representing a figure. Both matrices contain only 0s and 1s, where 1 means that the cell is
occupied, and 0 means that the cell is free.

You choose a position at the top of the game field where you put the figure and then drop it down. The figure
falls down until it either reaches the ground (bottom of the field) or lands on an occupied cell, which blocks it
from falling further. After the figure has stopped falling, some of the rows in the field may become fully occu-
pied.

Your task is to find the dropping position such that at least one full row is formed. As a dropping position, you
should return the column index of the cell in the game field which matches the top left corner of the figure’s 3 × 3
matrix. If there are multiple dropping positions satisfying the condition, feel free to return any of them. If there
are no such dropping positions, return -1.

Note: The figure must be dropped so that its entire 3 * 3 matrix fits inside the field, even if part of the matrix is
empty.

Example 1:
field = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
        [1, 0, 0],
        [1, 1, 0]]
and
figure = [[0, 0, 1],
        [0, 1, 1],
        [0, 0, 1]]
The output should be solution(field, figure) = 0.
Because the field is a 3 * 3 matrix, the figure can be dropped only from position 0. When the figure stops
falling, two fully occupied rows are formed, so dropping position 0 satisfies the condition.
"""
def findPosition(field, figure):
    height = len(field)
    width = len(field[0])
    fig_size = len(figure)  # same height and width
    
    for col in range(width-fig_size+1):
        row = 1
        while row < height-fig_size+1:
            fit = True
            for dx in range(fig_size):
                for dy in range(fig_size):
                    if field[row+dx][col+dy] == 1 and figure[dx][dy] == 1:
                        fit = False
            if not fit:
                break
            row += 1
        row -= 1
        
        for dx in range(fig_size):
            row_filled = True
            for col_idx in range(width):
                if not (field[row+dx][col_idx] == 1 or (col <= col_idx <= col + fig_size and figure[dx][col_idx-col])):
                    row_filled = False
        if row_filled:
            return col
        
    return -1

print(findPosition([[0, 0, 0],
                    [0, 0, 0],
                    [0, 0, 0],
                    [1, 0, 0],
                    [1, 1, 0]], 
        [[0, 0, 1],
        [0, 1, 1],
        [0, 0, 1]]))