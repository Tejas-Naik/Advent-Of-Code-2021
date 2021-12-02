with open('input.txt', 'r') as file:
    content = file.readlines()

horizontal = 0
depth = 0
aim = 0
for inp in content:
    if 'forward' in inp:
        splitted_inp = inp.split()
        horizontal += int(splitted_inp[-1])
    elif 'down' in inp:
        splitted_inp = inp.split()
        depth += int(splitted_inp[-1])
    elif 'up' in inp:
        splitted_inp = inp.split()
        depth -= int(splitted_inp[-1])

print(horizontal * depth)