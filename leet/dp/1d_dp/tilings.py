# https://leetcode.com/problems/domino-and-tromino-tiling

from functools import lru_cache

class Solution:
    def numTilings(self, n: int) -> int:
        # pure dp solution
        # consider each state the grid can be in
        # make relation from those states

        if n < 2:
            return 1
        elif n == 2:
            return 2
        
        MOD = 10 ** 9 + 7
        BOT = 0 # BOT_SQUARE_MISSING = 0
        TOP = 1 # TOP_SQUARE_MISSING = 1
        VALID = 2 # valid state, full grid

        dp = [[0, 0, 0] for _ in range(n + 1)]
        dp[0][VALID] = 1
        dp[1][VALID] = 1
        dp[2][VALID] = 2
        dp[2][TOP] = 1
        dp[2][BOT] = 1

        for i in range(3, n + 1):
            dp[i][BOT] += (dp[i-2][VALID] + dp[i-1][TOP]) % MOD
            dp[i][TOP] += (dp[i-2][VALID] + dp[i-1][BOT]) % MOD
            dp[i][VALID] += (dp[i-1][VALID] + dp[i-2][VALID] + dp[i-1][BOT] + dp[i-1][TOP]) % MOD

        return dp[n][VALID] % MOD

    def numTilings(self, n: int) -> int:
        
        # 1,1,2,5,11,24,53,117
        # counting problem

        if n < 2:
            return 1
        elif n == 2:
            return 2
        
        MOD = 10 ** 9 + 7

        a_3 = 1
        a_2 = 1
        a_1 = 2
        a = a_1 * 2 + a_3 # n=4

        for a in range(3, n + 1):
            a = (a_1 * 2 + a_3) % MOD
            a_3, a_2, a_1 = a_2, a_1, a

        return a
    
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
            