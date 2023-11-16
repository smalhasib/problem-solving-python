line = input()
n = int(line)

line = input()
numbers = list(map(int, line.split()))

for i in numbers:
    if i % 2 == 0:
        print(i)