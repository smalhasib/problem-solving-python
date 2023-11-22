from collections import defaultdict


def compare(item):
    return item[0], -item[1]


spectrum = input()
spectrum = list(map(int, spectrum.split()))

dict_s = defaultdict(int)

for i in spectrum:
    for j in spectrum:
        d = i - j
        if d > 0:
            dict_s[d] += 1

list_of_diff = [(value, index) for index, value in dict_s.items()]
list_of_diff.sort(key=compare)

result = [value for index, value in reversed(list_of_diff) for _ in range(index)]

with open('out.txt', 'w') as file:
    file.write(' '.join(map(str, result)))
