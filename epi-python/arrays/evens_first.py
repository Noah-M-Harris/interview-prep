"""
given an array of nums, arrange it so thst any even elements appear first in the array prior to odd elements.
Do not use any additional space.

input: [3, 4, 1, 5, 7, 8, 2]
output: [4, 8, 2, 3, 1, 5, 7]
"""

def solution(nums):
    """ loop over arr, have a ptr that points to the first idx in arr, anytime we find even int, swap, i += 1 """
    ptr = 0
    for i in range(len(nums)):
        n = nums[i]
        if n % 2 == 0:
            nums[ptr], nums[i] = n, nums[ptr]
            ptr += 1
    return nums

print(solution([3, 4, 1, 5, 7, 8, 2]))
print(solution([3, 2, 1, 4, 7, 8, 2]))
print(solution([1, 3, 5, 7, 2, 4, 6, 8]))

"""
When it comes to arrs, take advantage of the fact operatio on both sides is effecient, O(1), two ptrs, three ptrs, etc
Utilize sliding window, mathematical computation, and ptr solutions
"""