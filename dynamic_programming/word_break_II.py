"""

Given a string s and a dictionary of strings word_dict, 
add spaces in s to construct a sentence where each word is a valid dictionary word. 
Return all such possible sentences in any order.

eg. 
s = "catsanddog"
word_dict = ["cat", "and", "sands", "cats", "dog"]

output = ["cats and dog", "cat sand dog"]

"""

def solution(str, word_dict):

    dict = set(word_dict)
    result = {}