'''
suppose you are given a 2D array of integers and a 1D array of integers. Pattern occurs if it is possible
to start from some entry in the grid and traverse adjacent entries in the order specified by the pattern till all entries 
in the pattern have been visited.
'''

def solution(grid, pattern):
    ROWS, COLS = len(grid), len(grid[0])
    adj = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    # might be needed for backtracking - if we cannot visit a cell more than once, assume we can visit a cell more than once 
    visited = set()


    def dfs(i, r, c):
        # no next integer to look for
        if i >= (len(pattern) - 1):
            return True

        # now we want to look for the next letter starting here 
        for dr, dc in adj:
            if min(dr + r, dc + c) > -1 and (dr + r) < ROWS and (dc + c) < COLS and grid[dr + r][dc + c] == pattern[i + 1]:
                if dfs(i + 1, dr + r, dc + c):
                    return True
        return False

    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] == pattern[0]:
                if dfs(0, r, c):
                    return True
    return False


grid = [[1, 2, 3], [3, 4, 5], [5, 6, 7]]
pattern = [1, 3, 4, 6]
print(solution(grid, pattern))
pattern = [1, 4, 6, 7]
print(solution(grid, pattern))