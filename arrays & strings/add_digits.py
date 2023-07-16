"""
given an arr of digits representing a number, produce the number + 1
eg. [1, 2, 9] -> [1, 3, 0]
"""
''
def solution(nums):
    carry = 1

    nums = nums[::-1]
    for i in range(len(nums)):
        n = (carry + nums[i])
        nums[i] = n % 10
        carry = n // 10
    
    if carry:
        nums.append(carry)
    return nums[::-1]


    """
    carry = 1
    nums = nums[::-1]
    result = []

    for n in nums:

        result.append((n + carry) % 10)
        if carry + n >= 10:
            carry = 1
        else:
            carry = 0
            

    if carry:
        result.append(carry)

    return result[::-1]
    """

print(solution([1, 2, 9]))
print(solution([9, 9, 9]))
print(solution([2, 3, 4]))