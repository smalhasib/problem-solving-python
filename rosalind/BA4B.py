from Bio.Seq import Seq

dna = input()
amino = input()

k = len(amino) * 3
for i in range(len(dna) - k + 1):
    seq = Seq(dna[i: i + k])
    if seq.translate() == amino or seq.reverse_complement().translate() == amino:
        print(seq)
