file_text = open('input.txt', 'r')
lines = file_text.readlines()

codes = []

for line in lines:
    #print(line)
    num_only = [int(i) for i in line if i.isdigit()]
    #print(num_only)
    num_pair = num_only[::len(num_only)-1 if len(num_only) > 1 else None]
    num_str = ''.join([str(i) for i in num_pair])
    calibration_code = int(num_str) if len(num_str) > 1 else int(str(num_str)+str(num_str))
    codes.append(calibration_code)

print(sum(codes))