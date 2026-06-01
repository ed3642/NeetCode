# https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings

from functools import lru_cache

class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        
        n = len(s1)
        m = len(s2)
        dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)] # [i][j]

        # need these base cases to build states
        # they represent deleting only from one word
        for i in range(1, n + 1):
            dp[i][0] = dp[i - 1][0] + ord(s1[i - 1])
        for j in range(1, m + 1):
            dp[0][j] = dp[0][j - 1] + ord(s2[j - 1])

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j] + ord(s1[i - 1]), dp[i][j - 1] + ord(s2[j - 1]))
        
        return dp[n][m]

    def minimumDeleteSum(self, s1: str, s2: str) -> int:

        @lru_cache(maxsize=None)
        def dp(i, j):

            if i == len(s1) and j == len(s2):
                return 0
            
            if i == len(s1):
                return postfix2[j]
            if j == len(s2):
                return postfix1[i]

            if s1[i] == s2[j]:
                return dp(i + 1, j + 1)

            del1 = dp(i + 1, j) + ord(s1[i])
            del2 = dp(i, j + 1) + ord(s2[j])

            return min(del1, del2)
        
        postfix1 = [ord(c) for c in s1]
        postfix2 = [ord(c) for c in s2]

        for i in range(len(s1) - 2, -1, -1):
            postfix1[i] += postfix1[i + 1]
        for i in range(len(s2) - 2, -1, -1):
            postfix2[i] += postfix2[i + 1]

        return dp(0, 0)