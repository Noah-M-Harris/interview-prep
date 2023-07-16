"""
write a program that takes an arr nums, and an index i in nums, and rearranges the elements such that all elements than nums[i]
appear first, followed by elements equal to the pivot, followed by elements greater than the pivot

input: [0, 1, 2, 0, 2, 1, 1] index = 3
output: [0, 0, 1, 2, 2, 1, 1]

ipnut: [0, 1, 2, 0, 2, 1, 1] index = 2
output: [0, 1, 0, 1, 1, 2, 2]
"""

def solution(nums, idx):
    """ think of the arr as containing the less than, unknown, and greater than space """
    """ left points to beginning of arr (<), unknown is our traversal space, right points to end (>) """
    left, right = 0, len(nums)
    i = 0
    pivot = nums[idx]

    while i < right:
        # print("left:", left, " right:", right, " i:", i)
        if nums[i] < pivot:
            nums[left], nums[i] = nums[i], nums[left]
            left += 1
            i += 1
        elif nums[i] > pivot:
            right -= 1
            nums[i], nums[right] = nums[right], nums[i]
        else:
            i += 1
    
    return nums

print(solution([0, 1, 2, 0, 2, 1, 1], 3))
print(solution([0, 1, 2, 0, 2, 1, 1], 2))

    