"""
write a program that takes two arrays representing integers, and returns an integer representing their product
eg. [2, 3], [4] -> [9, 2]
"""

def solution(nums1, nums2):
    sum_1 = 0
    zeros = "1"
    
    negative1 = True if nums1[0] < 0 else False
    negative2 = True if nums2[0] < 0 else False

    for i in range(len(nums1)-1, -1, -1):
        sum_1 += abs(nums1[i]) * int(zeros)
        zeros += "0"
    
    sum_2 = 0
    zeros = "1"
    for i in range(len(nums2)-1, -1, -1):
        sum_2 += abs(nums2[i]) * int(zeros)
        zeros += "0"
    

    total = sum_1 * sum_2
    # if (negative1 and not negative2) or negative2 and not negative1:
       # total *= -1
    # print(total)

    result = []
    for i in range(len(str(total)) -1, -1, -1):
        result.append(total % 10)
        total //= 10
    
    if (negative1 and not negative2) or (negative2 and not negative1):
        result[-1] *= -1
    return result[::-1]

print(solution([-2, 3], [4])) # [9, 2]
print(solution([1, 9, 3, 7, 0, 7, 7, 2, 1], [-7, 6, 1, 8, 3, 8, 2, 5, 7, 2, 8, 7])) 
# [-1, 4, 7, 5, 7, 3, 9, 5, 2, 5, 8, 9, 6, 7, 6, 4, 1, 2, 9, 2, 7]