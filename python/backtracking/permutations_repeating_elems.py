# https://leetcode.com/problems/letter-tile-possibilities/
from typing import Counter

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        
        def bt():
            total = 0
            for unique in counts:
                if counts[unique] > 0:
                    counts[unique] -= 1
                    total += bt() + 1
                    counts[unique] += 1
            return total
        
        counts = Counter(tiles)
        return bt()