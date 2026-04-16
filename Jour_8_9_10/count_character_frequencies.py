"""
Given a string, create a dictionary where keys are characters and values are their frequencies in the string.
"""

string1 = 'JessadddeJ'

string1_in_list = list(string1)

result = {char: 0 for char in string1}

for i in string1:
    if i in string1_in_list:
        result[i] += 1

print(result)