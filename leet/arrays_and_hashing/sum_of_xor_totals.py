
from itertools import chain, combinations

# there is a O(n) bit manipulation solution but these are more intuitive for me.

class Solution:
    def subsetXORSum(self, nums: list[int]) -> int:
        # gen subsets
        # run xor reduction on all of them
        # sum the result

        def reduce(nums):
            res = 0
            for num in nums:
                res ^= num
            return res

        def powerset(iterable):
            s = list(iterable)
            return chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))


        subsets = powerset(nums)
        total = 0

        for subset in subsets:
            total += reduce(subset)

        return total

    def subsetXORSum2(self, nums: list[int]) -> int:
        # gen subsets
        # run xor reduction on all of them
        # sum the result

        def reduce(nums):
            res = 0
            for num in nums:
                res ^= num
            return res

        def backtrack(start, builder):

            subsets.append(builder.copy())
            if start == len(nums):
                return

            for i in range(start, len(nums)):
                builder.append(nums[i])
                backtrack(i + 1, builder)
                builder.pop()

        subsets = []
        backtrack(0, [])
        total = 0

        for subset in subsets:
            total += reduce(subset)

        return total