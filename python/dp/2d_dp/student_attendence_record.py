from functools import lru_cache

class Solution:
    def checkRecord(self, n: int) -> int:
        # dp, keep track of state total A's and consecutive L's

        MOD = 10**9 + 7

        # just trial and errored what size i needed
        @lru_cache(maxsize=25)
        def dp(i, a_count, l_con_count):

            if a_count >= 2 or l_con_count >= 3: # dead end path
                return 0
            if i == 0:
                return 1
            
            present = dp(i - 1, a_count, 0) % MOD
            absent = dp(i - 1, a_count + 1, 0) % MOD
            late = dp(i - 1, a_count, l_con_count + 1) % MOD

            return sum([present, absent, late]) % MOD

        return dp(n, 0, 0)