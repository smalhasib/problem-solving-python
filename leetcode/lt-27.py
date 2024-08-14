nums = [3, 2, 2, 3]
val = 3

n = len(nums)
i = j = k = 0

while i < n:
    if nums[i] != val:
        nums[i], nums[j] = nums[j], nums[i]
        j += 1
        k += 1
    i += 1

print(nums)
print(k)
