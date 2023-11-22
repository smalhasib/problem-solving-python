from collections import defaultdict

kmers = []
while True:
    line = input()
    if not line:
        break
    kmers.append(line)

graph = defaultdict(list)
for kmer in kmers:
    graph[kmer[:-1]].append(kmer[1:])

with open('out.txt', 'w') as file:
    for k, value in graph.items():
        file.write(f'{k} -> ' + ','.join(value) + '\n')
