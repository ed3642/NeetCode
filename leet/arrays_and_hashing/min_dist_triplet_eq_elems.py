# https://leetcode.com/problems/minimum-distance-between-three-equal-elements-i
# https://leetcode.com/problems/minimum-distance-between-three-equal-elements-ii/

from collections import defaultdict
from typing import List

class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        
        min_dist = float('inf')
        cand_i = defaultdict(list)
        f = defaultdict(int)

        for i, num in enumerate(nums):
            f[num] += 1

            if f[num] < 3:
                cand_i[num].append(i)
            elif f[num] == 3:
                cand_i[num].append(i)
                min_dist = min(abs(i - cand_i[num][0]) * 2, min_dist)
            else:
                cand_i[num][0], cand_i[num][1], cand_i[num][2] = cand_i[num][1], cand_i[num][2], i 
                min_dist = min(abs(i - cand_i[num][0]) * 2, min_dist)
        
        return min_dist if min_dist != float('inf') else -1
    
    def minimumDistance(self, nums: List[int]) -> int:
        # abs(k - i) * 2
        
        f = defaultdict(int)
        min_dist = float('inf')
        cand_i = defaultdict(list)

        for i, num in enumerate(nums):
            f[num] += 1
            if f[num] < 3:
                cand_i[num].append(i)
            elif f[num] == 3:
                cand_i[num].append(i)
                min_dist = min(abs(i - cand_i[num][0]) * 2, min_dist)
            else:
                # shift the queue
                cand_i[num][0], cand_i[num][1], cand_i[num][2] = cand_i[num][1], cand_i[num][2], i
                min_dist = min(abs(i - cand_i[num][0]) * 2, min_dist)

        return -1 if min_dist == float('inf') else min_dist