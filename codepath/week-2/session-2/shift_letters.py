"""
You are given a string s of lowercase English letters and an integer array shifts of the same length.

Call the shift() of a letter, the next letter in the alphabet, (wrapping around so that 'z' becomes 'a').

Input: s = "abc", shifts = [3,5,9]
Output: "rpl"

Explanation: We start with "abc".
After shifting the first 1 letters of s by 3, we have "dbc".
After shifting the first 2 letters of s by 5, we have "igc".
After shifting the first 3 letters of s by 9, we have "rpl", the answer.
"""

def solution(string, shifts):
    """ let's find the sum of the shifts arr, apply those amount of shifts to chr we are at, 
    then subtract sum - shifts[i] and continue 
    """
    
    currSum = sum(shifts)
    ptr = 0
    result = ""
    for c in string:
        if currSum + ord(c) > ord("z"):
            result += chr(96 + ((ord(c) + currSum) % ord("z")))
        else:
            result += chr(currSum + ord(c))
        currSum -= shifts[ptr]
        ptr += 1
    return result

print(solution("abc", [3, 5, 9])) # "rpl"
print(solution("aaa", [1, 2, 3])) # "gfd"
print(solution("xyz", [4, 5, 6])) # "mjf"
print(solution("axy", [3, 5, 9])) # "rlh"