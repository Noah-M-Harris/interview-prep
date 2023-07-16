



def solution(nums):
    min_val, max_val = float("inf"), float("-inf")
    left, right = 0, len(nums)-1
    water = 0
    
    while left < right:
        # from left calc max, from right calc min
        pos_max = nums[left]
        pos_min = nums[right]

        min_val, max_val = min(min_val, pos_min), max(max_val, pos_max)
        if max_val > min_val:
            water += max_val - min_val
        
        if nums[left] < nums[right]:
            left += 1
        else:
            right -= 1
    
    return water

print(solution([0, 2, 0, 1, 0, 2]))