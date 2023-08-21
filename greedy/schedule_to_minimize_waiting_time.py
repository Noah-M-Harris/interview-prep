'''
a db has to respond to a set of client SQL queries. The service time required for each query is known in advance
For this application, the queries must be processed by the db one at a time but can be done in any order.
The time aquery waits before its turn comes is called its waiting time
Given service times for a set of queries, compute a schedule for processing that minimizes the total waiting time.
'''


def solution(nums):
    nums.sort()
    prev = 0
    total = 0
    for i in range(len(nums)-1):
        n = nums[i]
        total += (prev + n)
        prev = (prev + n)
    return total


nums = [2, 5, 1, 3]
print(solution(nums))