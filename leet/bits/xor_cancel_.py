# https://leetcode.com/problems/neighboring-bitwise-xor
from typing import List

class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        
        # xor must cancel out

        total_xor = 0
        for bit in derived:
            total_xor ^= bit
        return total_xor == 0