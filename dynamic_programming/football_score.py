'''
write a program that takes a final score and scores the individual plays, and returns the number
of combinations of plays that result in the final score

n = 9
Output = 3
7 + 2 = 9
6 + 3 = 9
2 + 7 = 9
'''


def solution(n):

    dp = [[0] * (n + 1) for _ in range(4)]
    ROWS, COLS = len(dp), len(dp[0])
    for r in range(1, ROWS):
        dp[r][0] = 1

    points = [2, 3, 7]
    for r in range(1, ROWS):
        p = points[r - 1]
        for c in range(1, COLS):
            if (c - p) > -1:
                dp[r][c] = dp[r][c - p]
            dp[r][c] += dp[r - 1][c]

    print(dp)
    return dp[-1][-1]

print(solution(9))
print(solution(12))
print(solution(23))
print(solution(2))