from collections import defaultdict

amino_acid_masses = {'G': 57, 'A': 71, 'S': 87, 'P': 97, 'V': 99, 'T': 101, 'C': 103,
                     'I': 113, 'L': 113, 'N': 114, 'D': 115, 'K': 128, 'Q': 128, 'E': 129,
                     'M': 131, 'H': 137, 'F': 147, 'R': 156, 'Y': 163, 'W': 186}

peptide = input()
spectrum = input()
spectrum = list(map(int, spectrum.split(' ')))

p = len(peptide)
pep = peptide + peptide[:-1]

masses = [pep[i: i + j] for i in range(p) for j in range(p) if len(pep[i: i + j]) > 0] + [peptide, '']

spec = sorted(sum(amino_acid_masses[i] for i in st) for st in masses)

dict_t = defaultdict(int)
for i in spectrum:
    dict_t[i] += 1

dict_e = defaultdict(int)
for i in spec:
    dict_e[i] += 1

score = sum(min(dict_t[k], dict_e[k]) for k in dict_e if k in dict_t)
print(score)

