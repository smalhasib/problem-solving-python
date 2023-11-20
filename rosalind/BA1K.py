from itertools import product


def generate_kmers(k):
    return [''.join(p) for p in product('ACGT', repeat=k)]


dna = input()
k = int(input())

kmers = generate_kmers(k)

freq = [sum(1 for i in range(len(dna) - k + 1) if kmer == dna[i: i+k]) for kmer in kmers]

print(' '.join(map(str, freq)))
