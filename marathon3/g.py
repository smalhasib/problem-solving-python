from sys import stdin, stdout


def compare(item):
    return item[0], -item[1]


t = stdin.readline().split()[0]
t = int(t)

for i in range(t):
    n = stdin.readline().split()[0]
    n = int(n)

    points = []
    for j in range(n):
        x, y = stdin.readline().split()
        points.append((int(x), int(y)))

    points.sort(key=compare)

    for point in points:
        stdout.write(f'{point[0]} {point[1]}\n')
