from functools import lru_cache

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)
        dp = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                s1 = text1[i]
                s2 = text2[j]

                if s1 == s2:
                    dp[i][j] = dp[i + 1][j + 1] + 1
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])
        
        return dp[0][0]

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        @lru_cache(maxsize=None)
        def dp(i, j):

            if i == len(text1) or j == len(text2):
                return 0

            s1 = text1[i]
            s2 = text2[j]
            
            if s1 == s2:
                return dp(i + 1, j + 1) + 1
            return max(dp(i + 1, j), dp(i, j + 1))
        
        return dp(0, 0)
