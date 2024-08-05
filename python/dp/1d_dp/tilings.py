from functools import lru_cache

class Solution:
    def numTilings(self, n: int) -> int:
        # this makes a recursive sequence based of the base cases
        # 1, 1, 2, 5, 11, 24, 53
        # we could also do the module at each level
        if n <= 1:
            return 1
        elif n == 2:
            return 2
        
        dp = [1] * (n + 1)
        dp[2] = 2

        for i in range(3, n + 1):
            dp[i] = dp[i - 1] * 2 + dp[i - 3]

        return dp[n] % (10**9 + 7)

    def numTilings2(self, n: int) -> int:
        # this makes a recursive sequence based of the base cases
        # 1, 1, 2, 5, 11, 24, 53

        @lru_cache(maxsize=None)
        def dp(m):

            if m <= 1:
                return 1
            elif m == 2:
                return 2
            
            return dp(m - 1) * 2 + dp(m - 3)

        return dp(n) % (10**9 + 7)
            