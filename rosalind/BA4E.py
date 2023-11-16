# 4E: find a cyclic peptide with theoretical spectrum matching an ideal spectrum

import itertools

spec = '0 113 128 186 241 299 314 427'
spec = list(map(int, spec.split()))


def cyclopeptide_sequencing_problem(spect):
    mass = 0
    result = []
    for i in range(1, len(spect)):
        mass += spect[i]
        result.append(spect[i])
        if mass == spect[len(spect) - 1]:
            break

    return list(itertools.permutations(result))


res = cyclopeptide_sequencing_problem(spec)
print(" ".join('-'.join(map(str, result)) for result in res))
