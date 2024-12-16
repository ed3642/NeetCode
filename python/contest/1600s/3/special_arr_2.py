# https://leetcode.com/problems/special-array-ii/
from typing import List

class Solution:
    # O(n + q log n) q=num_queries, n=len_nums
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        
        # [4,3,1,6]
        # [0,1,1,0]
        # ranges question
        # define valid ranges, see which queries fall in valid ranges with binary search

        # binary search if a value from a list falls in this range
        def binary_search(target_start, target_end):
            l = 0
            r = len(break_indexes) - 1

            while l <= r:
                m = (l + r) // 2
                breaking_i = break_indexes[m]

                if breaking_i < target_start:
                    l = m + 1
                elif target_end < breaking_i:
                    r = m - 1
                else:
                    # breaking_i is between target_start and target_end
                    return True
            return False

        break_indexes = []

        for i in range(1, len(nums)):
            if nums[i - 1] % 2 == nums[i] % 2:
                break_indexes.append(i)
        
        res = []
        for start, end in queries:
            res.append(not binary_search(start + 1, end))

        return res
    
    # O(n + q)
    def isArraySpecial(self, nums: list[int], queries: list[list[int]]) -> list[bool]:
        # build valid ranges
        # check if query is in a valid range

        n = len(nums)
        valid_ranges = []

        # preprocess
        for i, num in enumerate(nums):
            nums[i] = num % 2

        l = 0
        r = 1

        while r < n:
            par1 = nums[r - 1]
            par2 = nums[r]

            if par1 == par2:
                valid_ranges.append([l, r - 1])
                l = r
                r = l + 1
                while r < n and nums[l] == nums[r]:
                    l += 1
                    r += 1

            if r < n:
                r += 1

        # close last interval
        valid_ranges.append([l, r - 1])

        # farthest each elem can reach with maintaining req
        farthest = [i for i in range(len(nums))]

        for _from, to in valid_ranges:
            for i in range(_from, to + 1):
                farthest[i] = to
                
        # print(farthest)
        # print(nums)
        # print(valid_ranges)

        res = []
        for _from, to in queries:
            if _from == to:
                res.append(True)
                continue
            if farthest[_from] == farthest[to]:
                res.append(True)
            else:
                res.append(False)

        return res