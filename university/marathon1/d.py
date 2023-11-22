line = input()
t = int(line)

while t > 0:
    line = input()
    n = int(line)

    line = input()
    balls_played = list(map(int, line.split()))

    sm, count = 0, 0
    for index in range(n):
        sm += balls_played[index]
        if sm / (index + 1) == 1:
            count += 1

    print(count)
    t -= 1
