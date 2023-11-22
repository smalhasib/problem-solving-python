line = input()
n = int(line)

line = input()
numbers = list(map(int, line.split()))

min_value = min(numbers)
min_indices = [index for index, value in enumerate(numbers) if value == min_value]

min_dist = 1000000000
for i in range(len(min_indices) - 1):
    dist = abs(min_indices[i] - min_indices[i + 1])
    if dist < min_dist:
        min_dist = dist

print(min_dist)
