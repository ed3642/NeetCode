# https://leetcode.com/problems/count-ways-to-build-good-strings
from functools import lru_cache

class Solution:

    # MLE if not doing MOD on all callbacks
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        
        MOD = 10 ** 9 + 7

        @lru_cache(maxsize=None)
        def ways(length):
            if length > high:
                return 0
            if low <= length <= high:
                return 1 + ways(length + zero) + ways(length + one) % MOD
            
            return ways(length + zero) + ways(length + one) % MOD
        
        return ways(0) % MOD
    