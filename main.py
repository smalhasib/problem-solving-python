from collections import defaultdict

pep = "EAST"
amino_acid_masses = {'G': 57, 'A': 71, 'S': 87, 'P': 97, 'V': 99, 'T': 101, 'C': 103,
                     'I': 113, 'L': 113, 'N': 114, 'D': 115, 'K': 128, 'Q': 128, 'E': 129,
                     'M': 131, 'H': 137, 'F': 147, 'R': 156, 'Y': 163, 'W': 186}

spectrums = [pep[i: i + j + 1] for i in range(len(pep)) for j in range(len(pep) - 1)] + [pep, '']


def calc_mass(peptide):
    return sum(amino_acid_masses[acid] for acid in peptide)


weights = [calc_mass(spectrum) for spectrum in spectrums]
weights.sort()
print(' '.join(map(str, weights)))

diff = defaultdict(int)

for i in weights:
    for j in weights:
        d = i - j
        if d > 0:
            diff[d] += 1

list_of_diff = [(base, key) for key, base in diff.items()]
list_of_diff.sort()

print(list_of_diff)

result = [base for key, base in reversed(list_of_diff) for _ in range(key)]

print(' '.join(map(str, result)))
