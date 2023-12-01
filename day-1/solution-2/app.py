import re

total = 0

num_text = "one two three four five six seven eight nine".split()

re_pattern = "(?=(" + "|".join(num_text) + "|\\d))"

def num_util(x):
    if x in num_text:
        return str(num_text.index(x) + 1)
    return x

file_text = open('../input.txt', 'r')
lines = file_text.readlines()

for line in lines:
    num_only = [*map(num_util, re.findall(re_pattern,  line))]
    total += int(num_only[0] + num_only[-1])

print(total)