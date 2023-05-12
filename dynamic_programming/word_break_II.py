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

    dp = [False] * (len(str) + 1)
    dp[len(str)] = True
    word = {}

    for i in range(len(str)-1, -1, -1):
        for w in word_dict:
            if (i + len(w)) <= len(str) and str[i: i + len(w)] == w:
                dp[i] = dp[i + len(w)]

    return dp[0]

s = "catsanddog"
word_dict = ["cat", "and", "sands", "cats", "dog"]
print(solution(s, word_dict))