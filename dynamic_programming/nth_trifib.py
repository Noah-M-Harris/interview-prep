"""

Given a number n, calculate the corresponding Tribonacci number. The Tribonacci sequence 
Tn+3 = Tn + Tn+2 + Tn+1, for n >= 0
T(0) = 0, T(1) = T(2) = 1

"""

def solution(n):

    dp = [0, 1, 1]
    stop = 2
    while stop < n:
        tmp0, tmp1, tmp2 = dp[0], dp[1], dp[2]
        sum = tmp0 + tmp1 + tmp2
        dp[0] = tmp1
        dp[1] = tmp2
        dp[2] = sum
        stop += 1

    return dp[-1]

n = 7
print(solution(n)) # 24

n = 10
print(solution(n)) # 149

n = 5
print(solution(n)) # 7