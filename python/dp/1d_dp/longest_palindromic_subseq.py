class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        # dp from [start,end] => longest in this range
        # calc subproblems inside [start,end] first

        n = len(s)
        dp = [[0] * n for _ in range(n)]
        # all length 1 are pals
        for i in range(n):
            dp[i][i] = 1

        for end in range(1, n):
            for start in range(end - 1, -1, -1):
                if s[start] == s[end]:
                    dp[start][end] = dp[start + 1][end - 1] + 2
                else:
                    dp[start][end] = max(dp[start][end - 1], dp[start + 1][end])
        
        return dp[0][n - 1]