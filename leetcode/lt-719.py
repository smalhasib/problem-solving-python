nums = [1, 3, 1]
k = 1

dist = []
n = len(nums)
for i in range(0, n):
    for j in range(i + 1, n):
        dist.append(abs(nums[i] - nums[j]))

print(sorted(dist)[k - 1])
