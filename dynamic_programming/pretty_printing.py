'''
consider the problem of laying out text using a fixed width font. Each line can hold no more than a fixed number of characters
Words on a line are to be seperated by exactly one blank. Therefore, we may be left with whitespace at the end of the line.
Given text, ie. a string of words seperated by single blanks, decompose the text into lines such that no word is split across
lines and the messiness of the decomposition is minimizes. Each line can hold no more than a specified number of characters
'''


def solution(words, line_width):
    pass




text = """I have inserted a large number of new exmaples from the papers for the Mathematical Tripos during the last twenty years, which
    should be useful to Cambridge students."""

print(solution(text, 36))