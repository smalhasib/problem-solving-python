def hamming_dist(a, b):
    return sum(x != y for x, y in zip(a, b))


pattern = input()
dnas = input()
dnas = dnas.split(' ')

distance = sum(
    min(hamming_dist(pattern, dna[i: i + len(pattern)]) for i in range(len(dna) - len(pattern) + 1)) for dna in dnas)

print(distance)
