



def solution(nums):
    n = len(nums)
    dp = [0] * (n + 1)

    dp[0] = 0
    dp[0] = 0

    for i in range(2, len(dp)):
        
        one = nums[i - 1] + dp[i - 1]
        two = nums[i - 2] + dp[i - 2]
        dp[i] = min(one, two)
    
    print(dp)
    return dp[-1]



print(solution([10,15,20]))
print(solution([1,100,1,1,1,100,1,1,100,1]))