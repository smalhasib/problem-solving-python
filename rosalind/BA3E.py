# 3E: construct the de bruijn graph of a collection of k mers

from collections import defaultdict

kmers = [
    "GAGG",
    "CAGG",
    "GGGG",
    "GGGA",
    "CAGG",
    "AGGG",
    "GGAG"
]

dicts = defaultdict(list)

for kmer in kmers:
    dicts[kmer[:-1]].append(kmer[1:])

for k, items in dicts.items():
    print(f'{k} -> ' + ','.join(items))
