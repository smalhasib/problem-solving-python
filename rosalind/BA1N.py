from itertools import product


def generate_kmer(k):
    return [''.join(p) for p in product('ACGT', repeat=k)]


def hamming_dist(a, b):
    return sum(x != y for x, y in zip(a, b))


pattern = input()
d = int(input())

k = len(pattern)

kmers = generate_kmer(k)

possible_kmers = [kmer for kmer in kmers if hamming_dist(kmer, pattern) <= d]


with open('out.txt', 'w') as file:
    for kmer in possible_kmers:
        file.write(kmer+'\n')
