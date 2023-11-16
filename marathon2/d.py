line = input()
a, b, c = map(int, line.split())

i = 0
while i <= c:
    if (c - i) % b == 0:
        print("Yes")
        exit()
    i += a
print("No")
