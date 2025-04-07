# https://leetcode.com/problems/alternating-groups-ii

from typing import List

class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        
        N = len(colors)
        colors = colors * 2

        count = 0
        streak = 0

        for i in range(1, N + k - 1):
            if colors[i] != colors[i - 1]:
                if streak < k - 1:
                    streak += 1
            else:
                streak = 0
            if streak == k - 1:
                count += 1
        
        return count
