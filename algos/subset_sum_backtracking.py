solutions = []

def subset_sum(i, n, _set, target_sum, subset):
    global solutions

    # If targetSum is zero, then there exists a subset
    if target_sum == 0:
        solutions.append(subset[:])
        return

    # Return if we have reached the end of the array
    if i == n:
        return

    # Not considering the current element
    subset_sum(i + 1, n, _set, target_sum, subset)

    # Consider the current element if it is less than or equal to targetSum
    if _set[i] <= target_sum:
        # Push the current element into the subset
        subset.append(_set[i])

        # Recursive call for considering the current element
        subset_sum(i + 1, n, _set, target_sum - _set[i], subset)

        # Remove the last element after recursive call to restore subset's original configuration
        subset.pop()


# set_1 = [1, 1, 2]
# sum_1 = 3
set_1 = [10,1,2,7,6,1,5]
sum_1 = 8

subset_sum(0, len(set_1), sorted(set_1), sum_1, [])

print(solutions)
