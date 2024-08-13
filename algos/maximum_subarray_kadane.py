# resource -> https://www.geeksforgeeks.org/largest-sum-contiguous-subarray/

nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

current_sum, maximum = 0, float('-inf')
start = 0
end = 0
s = 0

for i in range(len(nums)):
    current_sum += nums[i]
    if current_sum > maximum:
        maximum = current_sum
        start = s
        end = i

    if current_sum < 0:
        current_sum = 0
        s = i+1

print(maximum)
print([start, end])
