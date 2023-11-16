nums1 = [1]
nums2 = []
m = 1
n = 0

if n == 0:
    print(nums1)
else:
    res, i, j = [], 0, 0
    while m != 0 and n != 0 and i < m:
        while nums1[i] != 0 and nums1[i] <= nums2[j]:
            res.append(nums1[i])
            i += 1
        if nums1[i] == 0:
            break
        res.append(nums2[j])
        j += 1

    if j < n:
        res += nums2[j:]

    nums1.clear()
    print(nums1)
