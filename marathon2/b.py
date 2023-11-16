line = input()
n, H, W = map(int, line.split())

for i in range(n):
    line = input()
    h, w = line.split()

    res = []
    if h == 'Y':
        res.append('Y')
        H -= 1
        W += 1
    else:
        if W < 1:
            res.append('Y')
            H -= 1
            W += 1
        else:
            res.append('N')

    if w == 'Y':
        res.append('Y')
        H += 1
        W -= 1
    else:
        if H < 1:
            res.append('Y')
            H += 1
            W -= 1
        else:
            res.append('N')

    print(' '.join(res))

