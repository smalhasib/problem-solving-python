nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]

track = {}
k = 0

for i in nums:
    if i not in track:
        track[i] = 1
        nums[k] = i
        k += 1
    elif track[i] < 2:
        track[i] += 1
        nums[k] = i
        k += 1

print(nums)
print(k)
