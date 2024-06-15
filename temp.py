from functools import lru_cache

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)
        lcs = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
        
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if text1[i - 1] == text2[j - 1]:
                    lcs[i][j] = lcs[i - 1][j - 1] + 1
                else:
                    lcs[i][j] = max(
                        lcs[i - 1][j],
                        lcs[i][j - 1]
                    )
        
        return lcs[n][m]


    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        @lru_cache(maxsize=None)
        def lcs(t1_i, t2_i):
            if t1_i >= len(text1) or t2_i >= len(text2):
                return 0
            
            if text1[t1_i] == text2[t2_i]:
                return lcs(t1_i + 1, t2_i + 1) + 1
            else:
                return max(
                    lcs(t1_i + 1, t2_i), 
                    lcs(t1_i, t2_i + 1)
                )
        
        return lcs(0, 0)
