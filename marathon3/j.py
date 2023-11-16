line = input()
n = int(line)

line = input()

count = {}

for i in range(n - 1):
    two_gram = line[i: i + 2]
    if two_gram in count:
        count[two_gram] += 1
    else:
        count[two_gram] = 1

print(max(count, key=count.get))
