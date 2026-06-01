# https://leetcode.com/problems/count-ways-to-build-good-strings

from functools import lru_cache

class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        
        MOD = 10**9+7

        # dp[i] = ways to build a string size i
        dp = [0] * (high+1)
        dp[0] = 1

        for i in range(high):
            if i+zero <= high:
                dp[i+zero] = (dp[i+zero]+dp[i]) % MOD
            if i+one <= high:
                dp[i+one] = (dp[i+one]+dp[i]) % MOD
        
        for i in range(1, high+1):
            dp[i] = (dp[i]+dp[i-1]) % MOD

        return (dp[high] - dp[low-1]) % MOD
    
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
    