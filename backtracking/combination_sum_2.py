class Solution:
    def combinationSum2(self, nums: list[int], target: int) -> list[list[int]]:
        def backtrack(start, remainder, res):
            if remainder == 0:
                res.append(builder.copy())
                return
            elif remainder < 0:
                return

            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                builder.append(nums[i])
                backtrack(i + 1, remainder - nums[i], res)
                builder.pop()

        res = []
        builder = []
        nums.sort()
        backtrack(0, target, res)
        return res