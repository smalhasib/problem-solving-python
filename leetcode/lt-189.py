nums = [1, 2, 3, 4, 5, 6, 7]
k = 3

track = []
n = len(nums)

for i in range(k, 0, -1):
    track.append(nums[n - i])

i = n - k - 1
j = n - 1

while i >= 0:
    nums[i], nums[j] = nums[j], nums[i]
    i -= 1
    j -= 1

for i in range(k):
    nums[i] = track[i]

print(nums)
