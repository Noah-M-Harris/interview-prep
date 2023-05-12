"""
given a sorted lst of integers and a target integer, find the left most instance of target if present within the lst, if not
find the idx where it should be placed

eg.
nums = [1, 2, 4, 5, 6, 7] target = 8
output = 6

nums = [1, 3, 5, 6, 6, 9] target = 6
output = 3
"""


def solution(nums, target):
    
    if target > nums[len(nums)-1]:
        return len(nums)
    if target < nums[0]:
        return 0

    lo, hi = 0, len(nums)-1

    while lo <= hi:
        # get the mid_idx
        mid = lo + ((hi - lo) // 2)

        # if mid is target or is greater than target search left
        if nums[mid] == target:
            # update found as we know it is in the lst, but continue to look for furthest left
            found = mid
            hi = mid - 1
        elif target < nums[mid]:
            # search left
            hi = mid - 1
        else:
            lo = mid + 1
    return found

def solution_recursive(nums, target):
    if target < nums[0]:
        return 0
    if target > nums[-1]:
        return len(nums)
    
    found = [-1]
    def helper(lo, hi, target):
        if lo > hi:
            return

        mid = lo + ((hi - lo) // 2)

        if nums[mid] == target:
            found[0] = mid
            helper(lo, mid - 1, target)
        elif nums[mid] > target:
            helper(lo, mid - 1, target)
        else:
            helper(mid + 1, hi, target)  

    helper(0, len(nums)-1, target)
    return found[0]

nums = [1, 2, 4, 5, 6, 7]
target = 8
print(solution(nums, target)) # 6

nums = [1, 2, 4, 5, 6, 7]
target = 8
print("recurisve", solution_recursive(nums, target)) # 6

nums = [1, 3, 5, 6, 6, 9] 
target = 6
print(solution(nums, target)) # 3

nums = [1, 2, 4, 5, 6, 7]
target = 0
print(solution(nums, target)) # 0

nums = [2, 2, 2, 2, 2, 2, 2, 2]
target = 2
print(solution(nums, target)) # 0

nums = [2, 2, 2, 2, 2, 2, 2, 2]
target = 2
print("recurisve", solution_recursive(nums, target)) # 0

nums = [1, 3, 3, 3, 5, 7, 8, 12]
target = 3
print(solution(nums, target)) # 1

nums = [1, 3, 3, 3, 5, 7, 8, 12]
target = 3
print("recurisve", solution_recursive(nums, target)) # 1
