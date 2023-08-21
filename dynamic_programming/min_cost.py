



def solution(nums):
    
    a, b = 0, 0
    for n in nums:
        nxt = min(a + n, b + n)
        a, b = b, nxt
    
    return min(a, b)


print(solution([10,15,20]))
print(solution([1,100,1,1,1,100,1,1,100,1]))