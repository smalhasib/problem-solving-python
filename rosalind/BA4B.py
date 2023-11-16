# 4B: find substrings of a genome encoding a given amino acid string

from Bio.Seq import Seq

dna = "ATGGCCATGGCCCCCAGAACTGAGATCAATAGTACCCGTATTAACGGGTGA"
amino = "MA"

k = len(amino) * 3

for i in range(len(dna) - k + 1):
    ts = Seq(dna[i: i + k])
    if ts.translate() == amino or ts.reverse_complement().translate() == amino:
        print(ts)
