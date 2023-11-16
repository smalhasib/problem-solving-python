# 4F: Compute the Score of a Cyclic Peptide Against a Spectrum


amino_acid_masses = {'G': 57, 'A': 71, 'S': 87, 'P': 97, 'V': 99, 'T': 101, 'C': 103, 'I': 113, 'L': 113, 'N': 114,
                     'D': 115, 'K': 128, 'Q': 128, 'E': 129, 'M': 131, 'H': 137, 'F': 147, 'R': 156, 'Y': 163, 'W': 186}


def calc_mass(peptide):
    return sum(amino_acid_masses[acid] for acid in peptide)


def cyclo_spectrum(pept):
    pep = pept * 2
    return [0] + [calc_mass(pep[i: i + j + 1]) for i in range(len(pep)) for j in range(len(pep) - 1)] + [calc_mass(pep)]


spectrum = "0 99 113 114 128 227 257 299 355 356 370 371 484"
spectrum = list(map(int, spectrum.split()))
peptide = "NQEL"

actual = cyclo_spectrum(peptide)

res = sum(list(set(actual)).count(s) for s in spectrum)

print(res)
