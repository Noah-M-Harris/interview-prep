"""
URLify: write a method to replace all spaces in a string with '%20'. May assume that the string has sufficent space at the end to hold
the additional characters, and that you are given the 'true' length of the string
eg.
input: "Mr_John_Smith_____", 13
output: Mr%20John%20Smith
"""
# _ identifies the spaces

def solution(str):
    """ identify the final letter in the string, identify the leading letter in the string as we do not put '%20' in beginning or end """
    """ identify the spaces between both those two idx, then add %20 into string @ those positions """
    result = []
    for i in range(len(str)):
        if str[i] == " ":
            result.append("%20")
        else:
            result.append(str[i])
    
    # start from the front of array and locate leading letter
    lead = 0
    for  i in range(len(result)):
        if result[i] != "%20":
            lead = i
            break
        lead = i
        
    end = len(result) -1
    for i in range(len(result)-1, -1, -1):
        if result[i] != "%20":
            break
        end = i
    
    result = result[lead: end]

    # now look for spaces in between that are next to each other, we only want to include one '%20' for every variable number space
    true_result = []
    for i in range(len(result)):
        if result[i] != "%20":
            true_result.append(result[i])
        else:
            # make sure that that there is not procedding space in true_result
            if true_result[-1] != "%20":
                true_result.append(result[i])

    return "".join(true_result)

print(solution("Mr John Smith     "))
print(solution("    Noah    Harris    "))