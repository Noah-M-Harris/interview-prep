"""
In the "100 game" two players take turns adding, to a running total, any integer from 1 to 10. 
The player who first causes the running total to reach or exceed 100 wins.

What if we change the game so that players cannot re-use integers?

For example, two players might take turns drawing from a common pool of numbers from 1 to 15 
without replacement until they reach a total >= 100.


Given two integers maxChoosableInteger and desiredTotal, 
return true if the first player to move can force a win, otherwise, return false. 
Assume both players play optimally.
"""

def solution(maxInt, desiredTotal):

    # available numbers to choose from
    nums = [n for n in range(1, maxInt + 1)]

    def _solution(maxInt, desired, memo, flag):
        """ based on the nums available to us, we can determine if we can win """
        
        # base case: we have no choices to make

    memo = {}
    _solution(maxInt, desiredTotal, memo, True)
    return memo[desiredTotal]


print(solution(10, 11)) # False
print(solution(10, 1)) # True
print(solution(10, 0)) # True
print(solution(34, 500))


"""
    # if i know I can't beat it by taking the max, then i might as well take the min
    #  keep a variable that always refers to the minimum possible
    def _solution(maxI, desired, min, memo, flag):
        
        # try to take max and min at every step
        if maxI >= desired:
            memo[desired] = flag
            return flag
        
        # check to see if deisred already in memo
        if desired in memo:
            return memo[desired]
        
        # check taking the max and taking the min
        take_max = _solution(maxI - 1, desired - maxI, min, memo, not flag)
        take_min = _solution(maxI, desired - min, min - 1, memo, not flag)

        if take_max or take_min:
            memo[desired] = True
        else:
            memo[desired] = False

        return memo[desired]
"""