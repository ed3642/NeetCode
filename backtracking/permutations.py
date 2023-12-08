class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        def backtrack(builder):
            # found
            if len(builder) == len(nums):
                res.append(list(builder))
            
            # explore
            for num in nums:
                if num not in builder:
                    builder.append(num)
                    backtrack(builder)
                    builder.pop()

        res = []
        backtrack([])
        return res