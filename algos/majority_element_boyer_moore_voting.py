nums = [2, 2, 1, 1, 1, 2, 2]

candidate = count = 0
for n in nums:
    if count == 0:
        candidate = n

    if candidate == n:
        count += 1
    else:
        count -= 1

print(candidate)
