with open("input.txt", "r") as file:
    content = file.readlines()

def main():
    count = 0
    x = 0
    y = 0
    z = 0
    sum_old = 0
    sum_new = 0
    for i in range(1998):
        if(x == y == z == 0):
            x = int(content[i])
            y = int(content[i])
            z = int(content[i])

            sum_old = x + y + z
        else:
            x = y
            y = z
            z = int(content[i])
            sum_new = x + y + z
            if(sum_new > sum_old):
                count += 1
                sum_old = sum_new
            else:
                sum_old = sum_new

    print("Final Answer: ", count)


main()