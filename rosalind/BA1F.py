genome = input()

skew, g, c = [], 0, 0
for i in genome:
    if i == 'G':
        g += 1
    elif i == 'C':
        c += 1
    skew.append(g - c)

minimum = min(skew)
indices = [index + 1 for index, value in enumerate(skew) if value == minimum]

print(' '.join(map(str, indices)))
