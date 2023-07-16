

def solution(nums):
    """ search for min starting from right, search for max starting from right """
    """ if max > min, result += max - min """
    """
    Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
    Output: 6
    """

    max_arr = []
    min_arr = []

    curr_max = float("-inf")
    curr_min = float("inf")

    for i in range(len(nums)):
        min_arr.append(max(nums[i], curr_max))
        curr_min = max(nums[i], curr_max)

    for i in range(len(nums)-1, -1, -1):
        max_arr.append(max(nums[i], curr_max))
        curr_max = max(nums[i], )