# 4H : Generate the convolution of a spectrum

from collections import defaultdict

spectrum = "0 137 186 323"
spectrum = list(map(int, spectrum.split()))

diff = defaultdict(int)

for i in spectrum:
    for j in spectrum:
        d = i - j
        if d > 0:
            diff[d] += 1

list_of_diff = [(base, key) for key, base in diff.items()]
list_of_diff.sort()

result = [base for key, base in reversed(list_of_diff) for _ in range(key)]

print(' '.join(map(str, result)))
