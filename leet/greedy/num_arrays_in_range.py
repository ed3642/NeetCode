# https://leetcode.com/problems/count-the-hidden-sequences/submissions/1613791297/?envType=daily-question&envId=2025-04-21

from typing import List

class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        
        start = 0
        _min = 0
        _max = 0

        for num in differences:
            start += num
            _min = min(start, _min)
            _max = max(start, _max)
            if _max - _min > upper - lower:
                return 0
        
        return (upper - lower) - (_max - _min) + 1 

    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        
        start = 0
        _min = float('inf')
        _max = -float('inf')
        count = 0

        for num in differences:
            start += num
            _min = min(start, _min)
            _max = max(start, _max)
        
        for num in range(lower, upper + 1):
            if num + _min >= lower and num + _max <= upper:
                count += 1
        
        return count
