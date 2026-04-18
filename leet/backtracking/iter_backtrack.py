class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        def backtrack(start, builder, res):
            res.append(builder.copy())

            for i in range(start, len(nums)):
                builder.append(nums[i])
                backtrack(i + 1, builder, res)
                builder.pop()

        res = []
        backtrack(0, [], res)
        return res

    def permute(self, nums: list[int], k: int) -> list[list[int]]:
        def backtrack(builder, res):
            if len(builder) == k:
                res.append(builder.copy())
            
            for num in nums:
                if num not in builder:
                    builder.append(num)
                    backtrack(builder, res)
                    builder.pop()

        res = []
        backtrack([], res)
        return res
    
    # the only difference bt comb and subsets is that we dont care about the size in subsets
    def combinations(self, nums: list[int], k: int) -> list[list[int]]:
        def backtrack(start, builder, res):
            if len(builder) == k:
                res.append(builder.copy())

            for i in range(start, len(nums)):
                builder.append(nums[i])
                backtrack(i + 1, builder, res)
                builder.pop()

        res = []
        backtrack(0, [], res)
        return res
    
    # combinations with repetition
    def combinationSum(self, nums: list[int], target: int) -> list[list[int]]:
        def backtrack(start, builder, res):
            if sum(builder) == target:
                res.append(builder.copy())

            for i in range(start, len(nums)):
                if sum(builder) + nums[i] <= target:
                    builder.append(nums[i])
                    backtrack(i, builder, res)
                    builder.pop()

        res = []
        backtrack(0, [], res)
        return res