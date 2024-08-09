# https://leetcode.com/problems/combination-sum/
class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        
        def backtrack(start, builder: list, curr_sum):
            if curr_sum > target:
                return 
            if curr_sum == target:
                combinations.append(builder.copy())
                return 

            for i in range(start, len(candidates)):
                builder.append(candidates[i])
                backtrack(i, builder, curr_sum + candidates[i])
                builder.pop()

        combinations = []
        candidates.sort()
        backtrack(0, [], 0)
        return combinations
    
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