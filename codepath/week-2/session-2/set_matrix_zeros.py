"""
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's, and return the matrix.

You must do it in place.

Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]
"""

def solution(matrix):
    """ have an arr that accounts for the horizontal, have an arr that accounts for the vertical """
    rows = [False for _ in range(len(matrix))]
    cols = [False for _ in range(len(matrix[0]))]

    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            # if we find a zero, we know this row and this col is going to be 0
            if matrix[r][c] == 0:
                rows[r] = True
                cols[c] = True

    # loop back over the matrix and place 0's appropriately
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            if rows[r] == True or cols[c] == True:
                matrix[r][c] = 0

    return matrix




matrix = [[1,1,1],[1,0,1],[1,1,1]]
real = solution(matrix) # [[1,0,1],[0,0,0],[1,0,1]]

matrix = [[0, 1, 1], [1, 1, 0], [1, 1, 1]]
real2 = (solution(matrix)) # [[0, 0, 0], [0, 0, 0], [0, 1, 0]]


def solution(matrix):
    """ we will look at the first row and col to tell us if any position needs zeroing """
    ROWS, COLS = len(matrix), len(matrix[0])
    
    # use for first row since we will be modifying it
    firstRow = False

    for r in range(ROWS):
        for c in range(COLS):
            if matrix[r][c] == 0:
                matrix[r][0] = 0

                if r > 0:
                    matrix[0][c] = 0
                else:
                    firstRow = True

    # loop back over the arr and fix 
    for r in range(1, ROWS):
        for c in range(1, COLS):
            if matrix[0][c] == 0 or matrix[r][0] == 0:
                matrix[r][c] = 0

    if matrix[0][0] == 0:
        for r in range(ROWS):
            matrix[r][0] = 0

    if firstRow:
        for c in range(COLS):
            matrix[0][c] = 0

    return matrix

matrix = [[1,1,1],[1,0,1],[1,1,1]]
print(solution(matrix) == real) # [[1,0,1],[0,0,0],[1,0,1]]

matrix = [[0, 1, 1], [1, 1, 0], [1, 1, 1]]
print(solution(matrix) == real2) # [[0, 0, 0], [0, 0, 0], [0, 1, 0]]
