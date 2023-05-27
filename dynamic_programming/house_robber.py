def solution(nums):
    """ given an arr, return the max value of the arr when not being allowed to choose any adj numbers """
    
    a, b = 0, 0
    for n in nums:
        """ 
        a b [#, #, ...]
        when looping over nums, always changing where a and b are, a + n becomes b as we move to the next num, on first run, etc
        """
        tmp = max(a + n, b)
        a = b
        b = tmp
    return b



nums = [1, 3, 5] # 6
print(solution(nums))

nums = [3, 4, 6, 65, 56, 8] # 77
print(solution(nums))

nums = [1,2,3,1]
print(solution(nums)) # 4

nums = [2,7,9,3,1]
print(solution(nums)) # 12

nums = [2,1,1,2]
print(solution(nums)) # 4