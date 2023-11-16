line = input()
N, A, B = map(int, line.split())

line = input()
nums = list(map(int, line.split()))

for i in range(len(nums)):
    if nums[i] - A == B:
        print(i + 1)
