with open("input.txt", "r") as file:
    content = file.readlines()

count = 1
first_num = content[0]

for i in range(1, len(content)):
    current_num = content[i]
    if current_num > first_num:
        count += 1
    first_num = current_num

print(count)
