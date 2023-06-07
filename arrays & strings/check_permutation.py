"""
check_permuation: given two strings, write a method to determine if two strings are permutations of each other 
permutation eg. abc = acb = bca = cab = ...
"""

def solution(str_1, str_2):
    """ count the number of times each letter appears in each word, loop over the dicts, if they never differ, return True
        else False
    """
    if len(str_1) != len(str_2):
        return False

    dict_1, dict_2 = {}, {}

    for c in str_1:
        dict_1[c] = dict_1.get(c, 0) + 1
    for c in str_2:
        dict_2[c] = dict_2.get(c, 0) + 1
    
    """ flag = True if two strings are permutations, else False """
    flag = True
    for key in dict_1:
        if key not in dict_2 or dict_1[key] != dict_2[key]:
            flag = False
            break
    return flag

print(solution("abc", "acb")) # True
print(solution("avvbd", "aavbd")) # False
print(solution("aaaa", "aaa")) # False
