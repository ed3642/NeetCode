# https://leetcode.com/problems/make-lexicographically-smallest-array-by-swapping-elements
from typing import List

class Solution:
    # NOTE: could have also grouped them with UnionFind
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        
        # 2,1,0
        # 0,1,2

        def reorder_group(positions):
            placer_i = 0
            for i in sorted(positions):
                res[i] = nums[positions[placer_i]]
                placer_i += 1

        N = len(nums)
        if N == 1:
            return nums
        
        sorted_nums = sorted([(num, i) for i, num in enumerate(nums)], key=lambda x: x[0])
        adj_list = [[i] for i in range(N)] # so its neat when sorting the groups we point to itself at the start of the list
        res = nums.copy()

        # link nodes
        i = 0
        while i < N - 1:
            i2 = i
            while i < N - 1 and sorted_nums[i + 1][0] - sorted_nums[i][0] <= limit:
                adj_list[sorted_nums[i2][1]].append(sorted_nums[i + 1][1])
                i += 1
            else:
                i += 1
        
        # sort same group nodes
        for node in range(N):
            if len(adj_list[node]) > 1:
                reorder_group(adj_list[node])
        
        return res
