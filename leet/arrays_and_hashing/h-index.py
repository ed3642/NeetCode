# https://leetcode.com/problems/h-index

from collections import Counter
from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        
        # [6,5,3,1,0]
        # [3,1,1] -> [3,1]

        counts = Counter(citations)
        max_possible = max(counts.keys())
        cummulative = 0

        for k in range(max_possible, -1, -1):
            cummulative += counts[k]
            if cummulative >= k:
                return k
        
        return -1 # shouldnt happen
