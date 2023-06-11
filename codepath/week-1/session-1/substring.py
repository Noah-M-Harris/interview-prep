"""
Write a function that takes in two strings and 
returns true if the second string is substring of the first, and false otherwise.

eg. 
Input: laboratory, rat
Output: true

Input: cat, meow
Output: false
"""

def solution(s_1, s_2):
    """ two ptrs, loop through string 1, increment both ptrs if the character at index match, else ptr2 = 0, ptr1 += 1 always """
    """ if ptr_2 == len(s_2) return True, exit loop, False """

    # edge cases:
    if not s_2 or ( not s_1 and not s_2):
        return True
    if not s_1 and s_2:
        return False

    ptr_1, ptr_2 = 0, 0

    while ptr_1 < len(s_1):

        if s_1[ptr_1] == s_2[ptr_2]:
            ptr_2 += 1
        else:
            ptr_2 = 0
        ptr_1 += 1

        if ptr_2 == len(s_2):
            return True
    return False

print(solution("laboratory", "rat")) # True
print(solution("cat", "meow")) # False
print(solution("", "")) # True
print(solution("cat", "")) # True
print(solution("", "meow")) # False
