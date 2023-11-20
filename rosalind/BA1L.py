dna = input()

seq = {
    'A': 0,
    'C': 1,
    'G': 2,
    'T': 3
}

ans = sum(seq[dna[i]] * pow(4, len(dna) - i - 1) for i in range(len(dna)))

print(ans)
