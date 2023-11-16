# 2B: Find a median string

k = 6
dnas = [
    "GGATCTTGCTGTATGGGAGGGTAACTGTAGTTGGAGTTTAGG",
    "TAATGGCTGTAATATGCCATAAACATCTGAGACTTAATGACC",
    "TCGTTGGTTCCTCTTAACGTTATTCTGTAGCGTGCTGCACCC",
    "CGGGGACTAACGATTTTCCTGTACTCGGAGCTGCCGTGGCCG",
    "CTGTATCCGACGGCCCGTGATTCGCGATACTGTGACTGACAT",
    "GTTCGCCCTCAACGTTGACTGTACGTACGCATCGGTATAATC",
    "CCGTAACTGTAAAAAGGGTACCTGCCTCTTTAGACAAGAATC",
    "AGCTTCCTGTAAGACAGCTGGCTTGTCTAGTATTGGACTCTA",
    "AGACTTCTGTAAAGTTGACCCTCTGTTAAAAAAATTACCATC",
    "TCCTTTCCTGCTCTGTAGAGTGAGCACACTGTAAGAAGACGT"
]


def create(s, kmers):
    if len(s) == k:
        kmers.append(s)
        return s
    create(s + "A", kmers)
    create(s + "C", kmers)
    create(s + "G", kmers)
    create(s + "T", kmers)


def hamming_dist(dna, kmer):
    return sum(x != y for x, y in zip(dna, kmer))


def min_dist_dna_kmer(dna, kmer):
    return min(hamming_dist(dna[i:i + len(kmer)], kmer) for i in range(len(dna) - len(kmer) + 1))


def min_dist_of_kmer_for_all_dna(dnas, kmer):
    return sum(min_dist_dna_kmer(dna, kmer) for dna in dnas)


kmers = []
create('', kmers)

min_dist_kmer = {kmer: min_dist_of_kmer_for_all_dna(dnas, kmer) for kmer in kmers}

kmer = min(min_dist_kmer, key=min_dist_kmer.get)
print(kmer)