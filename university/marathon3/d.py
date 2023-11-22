import bisect

line = input()
T = int(line)

line = input()
numbers = list(map(int, line.split()))

line = input()
Q = int(line)

for i in range(Q):
    line = input()
    Y = int(line)

    index = bisect.bisect_left(numbers, Y)

    if numbers[index] == Y:
        print(f'Yes {index + 1}')
    else:
        print(f'No {index + 1}')
