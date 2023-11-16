# 2H:  Implement DistanceBetweenPatternAndStrings

def hamming_dist(dna, p):
    return sum(x != y for x, y in zip(dna, p))


def pattern_and_string_dist(pattern, dns):
    return sum(
        min(hamming_dist(dna[i: i + len(pattern)], pattern) for i in range(len(dna) - len(pattern) + 1)) for dna in dns)


pattern = "AAA"
dnas = ["TTACCTTAAC", "GATATCTGTC", "ACGGCGTTCG", "CCCTAAAGAG", "CGTCAGAGGT"]

distance = pattern_and_string_dist(pattern, dnas)
print(distance)
