def solution(n, dp={}):

    if n <= 1:
        return n
    
    if n not in dp:
        dp[n] = solution(n - 1, dp) + solution(n - 2, dp)
    
    
    return dp[n]

print(solution(7))
