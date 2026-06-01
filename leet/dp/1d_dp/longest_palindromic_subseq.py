# https://leetcode.com/problems/longest-palindromic-subsequence/

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        
        n = len(s)
        # dp = longest pal subseq in [l, r]
        dp = [[0 for _ in range(n)] for _ in range(n)]

        for i in range(n):
            dp[i][i] = 1 # 1 len strs

        # even pals
        for l in range(n - 2, -1, -1):
            for r in range(l + 1, n):
                if s[l] == s[r]:
                    dp[l][r] = dp[l + 1][r - 1] + 2
                else:
                    dp[l][r] = max(dp[l + 1][r], dp[l][r - 1])

        return dp[0][n - 1]

    def longestPalindromeSubseq(self, s: str) -> int:
        
        n = len(s)
        # dp = longest pal subseq in [l, r]
        dp = [[0 for _ in range(n)] for _ in range(n)]

        for i in range(n):
            dp[i][i] = 1 # 1 len strs

        # even pals
        for r in range(1, n):
            for l in range(r - 1, -1, -1):
                if s[l] == s[r]:
                    dp[l][r] = dp[l + 1][r - 1] + 2
                else:
                    dp[l][r] = max(dp[l + 1][r], dp[l][r - 1])

        return dp[0][n - 1]


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