# https://leetcode.com/problems/minimum-insertion-steps-to-make-a-string-palindrome

class Solution:
    def minInsertions(self, s: str) -> int:
        
        # mbadm
        # mdabm
        # leetcode
        # edocteel
        # if we get the LCS of s and rev(s) then the characters that couldnt be matched must have a new character inserted into the string to match them
        # so answer is len(s) - LCS(s, rev(s))

        def get_lcs_len(s1, s2):
            n = len(s1)
            m = len(s2)
            dp = [[0 for _ in range(m+1)] for _ in range(n+1)]

            for i in range(n):
                for j in range(m):
                    if s1[i] == s2[j]:
                        dp[i+1][j+1] = max(dp[i][j]+1, dp[i+1][j+1])
                    else:
                        dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
            return dp[n][m]
        
        return len(s) - get_lcs_len(s, s[::-1])