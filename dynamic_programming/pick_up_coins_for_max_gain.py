'''
design an efficent algorithm for computing the maximum total value for the starting player
in the puckup coins game. 
Two players take turns choosing from the two ends of the row of coins. Each plays optimally, game ends where there
are no more coins left. Find max coins player one can get
'''

def solution(coins):
    # we can use a flag to indicate who is picking or utilize minMax approach

    dp = {} # key -> tuple of available coins

    def dfs(left, right):
        if (left, right) in dp:
            return dp[(left, right)]
        if left > right:
            return 0

        choose_left = coins[left] + min(dfs(left + 2, right), dfs(left + 1, right - 1))
        choose_right = coins[right] + min(dfs(left, right - 2), dfs(left + 1, right - 1))
        dp[(left, right)] = max(choose_left, choose_right)
        return dp[((left, right))]

    return dfs(0, len(coins)-1)

coins = [25, 5, 10, 5, 10, 5, 10, 25, 1, 25, 1, 25, 1, 25, 5, 10]
print(solution(coins))
coins = [1, 2]
print(solution(coins))
coins = [1, 2, 3]
print(solution(coins))