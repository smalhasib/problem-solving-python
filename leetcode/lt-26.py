nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]

track = {}
k = 0

for i in nums:
    if i not in track:
        track[i] = True
        nums[k] = i
        k += 1

print(nums)
print(k)
