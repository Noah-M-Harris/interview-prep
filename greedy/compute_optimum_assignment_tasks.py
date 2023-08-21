'''
we consider the problem of assigning tasks to workers. Each worker must be assigned 
exactly two tasks. Each task takes a fixed amount of time. Tasks are independent. Any task can be assigned to any worker.
We want to assign tasks as to minimize how long it takes before all the tasks are completed.
'''

def solution(tasks):
    
    # always update the max output -> max(max_output, tasks[left] + tasks[right])
    max_output = float('-inf')
    tasks.sort()
    left, right = 0, len(tasks)-1

    while left <= right:
        if left == right:
            max_output = max(max_output, tasks[left])
        else:
            max_output = max(max_output, tasks[left] + tasks[right])
        left += 1
        right -= 1
    
    return max_output

tasks = [5, 2, 1, 6, 4, 4]
print(solution(tasks))
tasks = [86, 34, 1, 43, 4]
print(solution(tasks))