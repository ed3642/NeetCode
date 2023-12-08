class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        def backtrack(start, builder: list[int]):
            # found
            if sum(builder) == target:
                res.append(list(builder))

            # explore
            for i in range(start, len(candidates)):
                if sum(builder) + candidates[i] <= target:
                    builder.append(candidates[i])
                    backtrack(i, builder)
                    builder.pop()

        res = []
        backtrack(0, [])
        return res