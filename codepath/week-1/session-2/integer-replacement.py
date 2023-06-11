"""
Given a positive integer n, you can apply one of the following operations:

If n is even, replace n with n / 2. If n is odd, replace n with either n + 1 or n - 1. 
Return the minimum number of operations needed for n to become 1.
"""

def solution(n):
    
    def _solution(n, steps, memo):
        """ if n is an odd number we have to cal the route of going down n + 1 and n - 1, and store the min """
        # base case
        if n == 1:
            return steps

        # check to see if n already stored in memo
        if n in memo:
            return memo[n]
        
        # even or odd
        if n % 2 == 1:
            memo[n] = min(_solution(n + 1, steps + 1, memo), _solution(n - 1, steps + 1, memo))

        else:
            memo[n] = _solution(n // 2, steps + 1, memo)
        
        return memo[n]

    memo, steps = {}, 0
    _solution(n, steps, memo)
    return memo[n]

print(solution(8)) # 3
print(solution(7)) # 4
print(solution(4)) # 2
