text = input()
k = int(input())

probability = {}
for i in 'ACGT':
    line = input()
    probability[i] = list(map(float, line.split()))

kmers = sorted(set(text[i: i+k] for i in range(len(text) - k + 1)))

kmers_count = {kmer: sum(probability[value][index] for index, value in enumerate(kmer)) for kmer in kmers}

print(max(kmers_count, key=kmers_count.get))
