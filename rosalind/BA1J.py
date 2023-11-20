from Bio.Seq import Seq
from collections import defaultdict
from itertools import product


def generate_kmers(k):
    return [''.join(p) for p in product("ACGT", repeat=k)]


def hamming_dist(a, b):
    return sum(x != y for x, y in zip(a, b))


seq = input()
line = input()
k, d = map(int, line.split())

kmers = generate_kmers(k)

kmer_count = defaultdict(int)
for kmer in kmers:
    a = sum(hamming_dist(kmer, seq[i: i + k]) <= d for i in range(len(seq) - k + 1))
    b = sum(hamming_dist(kmer, Seq(seq[i: i + k]).reverse_complement()) <= d for i in range(len(seq) - k + 1))
    kmer_count[kmer] = a + b

max_value = max(kmer_count.values())

max_valued_kmers = [key for key, value in kmer_count.items() if value == max_value]

print(' '.join(max_valued_kmers))
