file_text = open('../input.txt', 'r')
lines = file_text.readlines()

total = 0

for line in lines:
    num_only = [i for i in line if i.isdigit()]
    total += int(num_only[0] + num_only[-1])

print(total)