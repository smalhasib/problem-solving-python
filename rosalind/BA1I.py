from itertools import product


def generate_kmers(k):
    return [''.join(p) for p in product("ACGT", repeat=k)]


def hamming_dist(a, b):
    return sum(x != y for x, y in zip(a, b))


seq = input()
line = input()
k, d = map(int, line.split())

kmers = generate_kmers(k)

kmer_count = {kmer: sum(hamming_dist(kmer, seq[i: i + k]) <= d for i in range(len(seq) - k + 1)) for kmer in kmers}

max_value = max(kmer_count.values())

max_valued_kmers = [key for key, value in kmer_count.items() if value == max_value]

print(' '.join(max_valued_kmers))
