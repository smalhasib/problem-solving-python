line = input()
t = int(line)

while t > 0:
    line = input()
    n = int(line)

    b_max, result = 0, 0
    for i in range(n):
        line = input()
        a, b = map(int, line.split())

        if 10 >= a and b_max < b:
            b_max, result = b, i+1

    print(result)

    t -= 1
