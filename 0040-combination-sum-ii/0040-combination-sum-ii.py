from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def dfs(start, path, remain):
            if remain == 0:
                res.append(path[:])
                return

            for i in range(start, len(candidates)):
                # Skip duplicates
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                # Since array is sorted, no need to continue
                if candidates[i] > remain:
                    break

                path.append(candidates[i])
                dfs(i + 1, path, remain - candidates[i])  # i+1 because each number is used once
                path.pop()

        dfs(0, [], target)
        return res