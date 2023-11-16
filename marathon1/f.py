line = input()
t = int(line)

while t > 0:
    line = input()
    x, y = map(int, line.split())

    if x <= 8 and x * y <= 500:
        print("YES")
    else:
        print("NO")

    t -= 1
