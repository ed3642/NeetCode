# https://leetcode.com/problems/divide-array-into-equal-pairs
from typing import List

class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        # xor doesnt work here
        _set = set()
        for num in nums:
            if num in _set:
                _set.remove(num)
            else:
                _set.add(num)
        return len(_set) == 0