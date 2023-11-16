# 2C: Find a Profile-most Probable k-mer in a String

dna = "ACCTGTTTATTGCCTAAGTTCCGAACAAACCCAATATAGCCCGAGGGCCT"
k = 5
dic = {
    'A': [0.2, 0.2, 0.3, 0.2, 0.3],
    'C': [0.4, 0.3, 0.1, 0.5, 0.1],
    'G': [0.3, 0.3, 0.5, 0.2, 0.4],
    'T': [0.1, 0.2, 0.1, 0.1, 0.2]
}

kmers = set(dna[i: i + k] for i in range(len(dna)))
kmers = sorted(list(kmers))

probable_kmer = {kmer: sum(dic[base][i] for i, base in enumerate(kmer)) for kmer in kmers}

max_kmer = max(probable_kmer, key=probable_kmer.get)
print(max_kmer)
