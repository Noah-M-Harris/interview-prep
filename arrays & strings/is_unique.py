""" return true if the str is unique, else False """

def solution(str):
    """ implement an algorithm to determine if a string has all unique characters """
    return len(str) == len(set(str))

def solution_2(str):
    """ if we can not use additional data structures, sort str, make sure we have not already seen that char """
    sorted_str = "".join(sorted(str))
    char = sorted_str[0]

    for i in range(1, len(sorted_str)):
        if sorted_str[i] == char:
            return False
        char = sorted_str[i]
    
    return True

print(solution("abcdef")) # True
print(solution_2("abcdef")) # True
print(solution("abcdfef")) # False
print(solution_2("abcdfef")) # False
