arr = [ 2, 3, 4, 10, 40 ]
x = 10

def binary_search(low, high) -> int:
    if high >= low:
        mid = (high + low) // 2
        if (arr[mid]) == x:
            return mid
        elif arr[mid] > x:
            return binary_search(low, mid - 1)
        else:
            return binary_search(mid + 1, high)
    else:
        return -1

def b_search(low, high) -> int:
    while high >= low:
        mid = (low + high) // 2


print(binary_search(0, len(arr)))