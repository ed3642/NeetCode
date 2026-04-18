# https://leetcode.com/problems/max-chunks-to-make-sorted
from typing import List

class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        
        # [0,1,4,2,3,inf]
        partitions = 0
        looking_for = 0

        for i, num in enumerate(arr):
            looking_for = max(num, looking_for)
            if i == looking_for:
                looking_for = i + 1
                partitions += 1
        
        return partitions
