# https://leetcode.com/problems/count-the-number-of-powerful-integers

from functools import lru_cache

class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        
        # digit dp
        high = str(finish)
        N = len(high)
        low = str(start).zfill(N)
        prefix_len = N - len(s)

        @lru_cache(maxsize=None)
        def dp(i, builder_eq_start, builder_eq_finish):
            if i == N:
                return 1
            
            lo = int(low[i]) if builder_eq_start else 0
            hi = int(high[i]) if builder_eq_finish else 9

            count = 0

            if i < prefix_len:
                # place digits less before suffix
                for digit in range(lo, min(hi, limit) + 1):
                    count += dp(i + 1, 
                                builder_eq_start and lo == digit, 
                                builder_eq_finish and hi == digit)
            else:
                # make the suffix
                digit = int(s[i - prefix_len])
                if lo <= digit <= min(hi, limit): 
                    count += dp(i + 1,
                                builder_eq_start and lo == digit,
                                builder_eq_finish and hi == digit)
            return count

        return dp(0, True, True)