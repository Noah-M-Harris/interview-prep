"""

Suppose you have the list of weights and corresponding values for n
items. You have a knapsack that can carry a specific amount of weight at a time called capacity.
You need to find the maximum profit of items using the sum of values of the items you can carry in a knapsack. 
The sum of the weights of the items should be less than or equal to the knapsack's capacity.
If any combination can't make the given knapsack capacity of weights, then return 0.

Example:

capacity = 30
weights = [10, 20, 30]
values = [22, 33, 44]

output -> 55 eg. 22 + 33 = 55

"""

def solution(weights, values, capacity):
    """
    for every value, we want to compute a new possible max profit
    any weight corresponding to position in values <= capacity and any capacity is
    max(values[i], profit[capacity - weights[i]] + values[i]), must first initialize a profits array of len(len(capcity) + 1)
    """
    profits = [0] * (capacity + 1)
    for i in range(len(values)):
        for c in range(capacity, -1, -1):
            if (weights[i] <= c):
                profits[c] = max(profits[c], profits[c - weights[i]] + values[i])

    # answer is held at the capacity
    return profits[capacity]

    # running time: O(n * m), n = len(values), m = capacity
    # space complexity: O(m), m = capacity

def solution2(weights, values, capacity):
    # this time utilizing matrix
    matrix = [[0] * (capacity + 1) for i in range(len(values) + 1)]

    # cols pertains to our alloted capacity; rows pertains to alloted values available to us
    for r in range(1, len(matrix)):
        w, val = weights[r - 1], values[r - 1]

        for c in range(1, len(matrix[0])):
            # for every position compute max between immediate left of us and above and next fitting capactiy
            if w <= c:
                matrix[r][c] = max(matrix[r][c], matrix[r - 1][c - w] + val)

    # print(matrix)
    return matrix[len(values) - 1][capacity]
    


capacity = 5
weights = [10, 20, 30]
values = [22, 33, 44]
print("first sol:", solution(weights, values, capacity))
print("second sol:", solution2(weights, values, capacity))


weights = [24, 10, 10, 7]
values = [24, 16, 16, 11]
capacity = 26
print("first sol:", solution(weights, values, capacity))
print("second sol:", solution2(weights, values, capacity))
