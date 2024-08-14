nums = [2, 2, 1, 1, 1, 2, 2]

cnt = n = 0

for i in nums:
    if cnt == 0:
        n = i

    if n == i:
        cnt += 1
    else:
        cnt -= 1

print(n)
