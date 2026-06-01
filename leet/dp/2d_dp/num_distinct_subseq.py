# https://leetcode.com/problems/distinct-subsequences

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # the solution can be compressed into a 1d dp but this is fine
        
        n = len(s)
        m = len(t)

        # Subsequence Count
        # ssc[i][j]: seq count in s[:i] that equal s[:j]
        sc = [[0 for _ in range(m+1)] for _ in range(n+1)]

        # emtpy t
        for i in range(n+1):
            sc[i][0] = 1
        
        for i in range(n):
            for j in range(m):
                if t[j] == s[i]:
                    # sc[i][j]: states that use s[i]
                    # sc[i][j+1]: states that skip s[i]
                    sc[i+1][j+1] += sc[i][j]+sc[i][j+1] # both states
                else:
                    sc[i+1][j+1] = sc[i][j+1]

        return sc[n][m]