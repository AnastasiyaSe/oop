lines1 = 0
with open('1.txt') as f:
    for line in f:
        lines1 = lines1 + 1
lines2 = 0
with open('2.txt') as f:
    for line in f:
        lines2 = lines2 + 1
lines3 = 0
with open('3.txt') as f:
    for line in f:
        lines3 = lines3 + 1

file_dict = {}
file_dict['1.txt'] = lines1
file_dict['2.txt'] = lines2
file_dict['3.txt'] = lines3

sorted_values = sorted(file_dict.values())
sorted_dict = {}

for i in sorted_values:
    for k in file_dict.keys():
        if file_dict[k] == i:
            sorted_dict[k] = file_dict[k]
            break
for key in sorted_dict:
    f = open(key, 'r')
    newf = open('newfile.txt', 'a')
    lines = f.readlines()
    newf.write(f'{key}\n')
    newf.write(f'{str(sorted_dict[key])}\n')
    for line in lines:
        newf.write(line)
    newf.close()
    f.close()

newf = open('newfile.txt', 'r')
f = newf.read()
print(f)
