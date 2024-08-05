class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        def backtrack(start, builder, res): # passing res makes it faster
            res.append(builder.copy())

            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]: # skip dups
                    continue
                builder.append(nums[i])
                backtrack(i + 1, builder, res)
                builder.pop()

        res = []
        nums.sort()
        backtrack(0, [], res)
        return res