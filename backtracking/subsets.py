class Solution:
    #O(n 2^n)
    def subsets(self, nums: list[int]) -> list[list[int]]:
        def backtrack(i, builder):
            # found
            if builder not in res:
                res.add(builder)

            # explore
            if i < len(nums):
                backtrack(i + 1, builder)
                backtrack(i + 1, builder + (nums[i], ))


        res = set()
        backtrack(0, tuple())
        return [list(tup) for tup in res]
    
    def subsets2(self, nums: list[int]) -> list[list[int]]:
        def backtrack(start, builder):
            res.append(builder)
            
            for i in range(start, len(nums)):
                backtrack(i + 1, builder + [nums[i]])

        res = []
        backtrack(0, [])
        return res