from typing import List

class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        
        n = len(colors)
        r = n - 1

        max_dist = 0
        for l in range(n - 1):
            if colors[l] != colors[r]:
                max_dist = r - l
                break
        
        l = 0
        for r in range(n - 1, 0, -1):
            if colors[l] != colors[r]:
                return max(max_dist, r - l)

        return -1 # shouldnt happen
