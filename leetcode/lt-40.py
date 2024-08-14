from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        solutions = []
        n = len(candidates)

        def subset_sum(i, remaining, subset):
            if remaining == 0:
                solutions.append(subset[:])
                return

            for j in range(i, n):
                if j > i and candidates[j] == candidates[j - 1]:
                    continue
                if candidates[j] > remaining:
                    break

                subset.append(candidates[j])
                subset_sum(j + 1, remaining - candidates[j], subset)
                subset.pop()

        candidates.sort()
        subset_sum(0, target, [])

        return solutions
