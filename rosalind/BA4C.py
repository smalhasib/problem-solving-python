amino_acid_masses = {'G': 57, 'A': 71, 'S': 87, 'P': 97, 'V': 99, 'T': 101, 'C': 103,
                     'I': 113, 'L': 113, 'N': 114, 'D': 115, 'K': 128, 'Q': 128, 'E': 129,
                     'M': 131, 'H': 137, 'F': 147, 'R': 156, 'Y': 163, 'W': 186}

pep = input()
p = len(pep)
peptide = pep + pep[:-1]

masses = [peptide[i:i + j] for i in range(p) for j in range(p) if len(peptide[i:i + j]) > 0] + [pep, '']

spectrum = [sum(amino_acid_masses[i] for i in mass) for mass in masses]

print(' '.join(map(str, sorted(spectrum))))
