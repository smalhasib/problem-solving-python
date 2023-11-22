from itertools import product
from collections import defaultdict


def generate_kmers(k):
    return [''.join(p) for p in product('ACGT', repeat=k)]


def hamming_dist(a, b):
    return sum(x != y for x, y in zip(a, b))


def kmer_dist_count(kmer, dna):
    return sum(min(hamming_dist(kmer, d[i: i + len(kmer)]) for i in range(len(d) - len(kmer) + 1)) for d in dna)


k = int(input())

dna = []
while True:
    line = input()
    if not line:
        break
    dna.append(line)

kmers = generate_kmers(k)

kmers_count = {kmer: kmer_dist_count(kmer, dna) for kmer in kmers}

print(min(kmers_count, key=kmers_count.get))
