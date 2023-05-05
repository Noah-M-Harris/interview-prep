"""

Given a non-empty array of positive integers, 
determine if the array can be divided into two subsets so that the sum of both the subsets is equal.

eg.
arr = [1, 2, 3, 5, 11] = TRUE
[1, 2,  3, 5] == [11]

arr = [1, 3, 7, 3] = TRUE
[1, 3, 3] == [7]
"""

def solution(arr):
    """
    for both partitions of the arr to be equal to each other, the sum(arr) must be even
    starting from the end of the arr, we want to add each num in the arr to every num in our set
    if we ever spot the target, sum(arr) / 2, in our set, return True, else False
    """
    if sum(arr) % 2:
        return False
    
    tot = sum(arr)
    dp = set()
    # base case, 0 is always possible to sum up to
    dp.add(0)

    for i in range(len(arr)-1, -1, -1):
        nextDP = set()
        for num in dp:
            nextDP.add(num)
            nextDP.add(num + arr[i])
        dp = nextDP
    return True if (tot / 2) in dp else False



arr = [1, 2, 3, 5, 11]
print(solution(arr)) # True

arr = [1, 3, 7, 3]
print(solution(arr)) # True

arr = [1, 2, 5]
print(solution(arr)) # False