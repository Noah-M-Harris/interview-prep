"""

You're given an integer total and a list of integers called coins. 
The variable coins hold a list of coin denominations, and total is the total amount of money.
You have to find the minimum number of coins that can make up the total amount by using any combination of the coins. 
If the amount can't be made up, return -1. If the total amount is 0, return 0.


eg. 
coins = [1, 3, 4, 5]
total = 7

output = 2 <- two coins: 4 + 3
"""

def solution(coins, total):
    """
    top-down: recursive dfs, for amount, branch for each coin, cache to store prev coin_count for each amount; 
    bottom-up: compute coins for amount = 1, up until n, using for each coin (amount - coin), cache prev values
    """
    if total == 0:
        return 0
    dp = [(total + 1) for _ in range(total + 1)]
    # we need 0 coins to hit 0
    dp[0] = 0

    for i in range(len(dp)):
        for c in coins:
            if c <= i:
                dp[i] = min(dp[i], 1 + dp[i - c])

    if dp[-1] == (total + 1):
        return -1

    return dp[total]
    


coins = [1, 3, 4, 5]
total = 7
print(solution(coins, total)) # 2

coins = [1, 2, 5]
total = 11
print(solution(coins, total)) # 3 

coins = [2]
total = 3
print(solution(coins, total)) # -1

coins = [2]
total = 4
print(solution(coins, total)) # 2


"""

if total == 0:
        return 0
        
    dp = [[0] * (total + 1) for _ in range(len(coins) + 1)]

    for r in range(1, len(dp)):
        coin = coins[r - 1]
        for c in range(1, len(dp[0])):
            # move horizontally through computing new value to store
            amount = c
            # consider coin > amount and else case
            if coin > amount:
                dp[r][c] = dp[r - 1][c]
            elif r != 1:
                dp[r][c] = min(dp[r - 1][c], 1 + dp[r][amount - coin])
            else:
                dp[r][c] = 1 + dp[r][amount - coin]

    return dp[-1][-1]

"""
