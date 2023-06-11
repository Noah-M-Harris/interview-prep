"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, 
it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.
"""

def _check(string, ptr):
    return 48 <= ord(string[ptr]) <= 57 or 97 <= ord(string[ptr]) <= 122
    
def solution(string):
    """ using two ptrs, we can start at both ends of the string, when both point to a char, compare, return False !=, else exit = True"""
    if not string: 
        return True

    # convert all uppercase letters to lowercase beforehand
    # uppercase letters: 65 <= ptr <= 90
    result = ""
    for char in string:
        result += char.lower()
            
    string = result
    left, right = 0, len(string)-1

    # numeric: 48 <= ptr <= 57
    # lowercase: 97 <= ptr <= 122
    while left < right:
        # handle case we are not pointing to a alphanumeric char
        while not _check(string, left):
            left += 1
        while not _check(string, right):
            right -= 1
        
        if string[left] != string[right]:
            print(string[left], string[right])
            return False
        
        left += 1
        right -= 1
    return True

print(solution("A man, a plan, a canal: Panama")) # True
print(solution("race a car")) # False
