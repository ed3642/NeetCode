class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:

        def backtrack(i, total, builder):
            
            if total == target:
                res.append(builder.copy())
                return
            
            if total > target:
                return

            for j in range(i, len(candidates)):
                builder.append(candidates[j])
                total += candidates[j]
                backtrack(j, total, builder)
                builder.pop()
                total -= candidates[j]
            
        res = []
        backtrack(0, 0, [])
        return res
    
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
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