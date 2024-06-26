from functools import lru_cache

class Solution:
    # space optimized, nice solution
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text1) < len(text2): # text2 is shortest
            text1, text2 = text2, text1
        n = len(text1)
        m = len(text2)
        prev_state = [0] * (m + 1)
        curr_state = [0] * (m + 1)
        
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if text1[i - 1] == text2[j - 1]:
                    curr_state[j] = prev_state[j - 1] + 1
                else:
                    curr_state[j] = max(
                        prev_state[j],
                        curr_state[j - 1]
                    )
            prev_state, curr_state = curr_state, prev_state
        
        return prev_state[m]

    # close to top down solution
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

    # O (m n)
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        n = len(text1)
        m = len(text2)

        dp = [[0] * (m + 1) for _ in range((n + 1))] # <max len>

        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                if text1[i] == text2[j]:
                    # case 1: first chars match, both in opt sol
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    # case 2: one of the chars can be in the opt sol
                    dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])

        return dp[0][0]
    
    # O (m n)
    def longestCommonSubsequence3(self, text1: str, text2: str) -> int:
        # look at the first characters
        # should we take it into the opt sol or not

        @lru_cache(maxsize=None)
        def dp(i, j):

            if i == len(text1) or j == len(text2):
                return 0
            
            # case1: first chars match, both in the opt sol
            if text1[i] == text2[j]:
                return 1 + dp(i + 1, j + 1)

            # case2: one of the chars can be in the opt sol
            return max(dp(i, j + 1), dp(i + 1, j))
        
        return dp(0, 0)

    # O (m n^2)
    def longestCommonSubsequence3(self, text1: str, text2: str) -> int:
        # for each char in text1, decide if its in or not in the optimal solution
        # the subproblem is when new text1 and text2 after deciding the inclusion of that char in text1

        @lru_cache(maxsize=None)
        def dp(i, j):

            if i == len(text1) or j == len(text2):
                return 0
            
            char = text1[i]
            first_occurence = text2.find(char, j)

            case1 = dp(i + 1, j) # char is not included
            case2 = 0
            if first_occurence != -1:
                case2 = 1 + dp(i + 1, first_occurence + 1) # char is included

            return max(case1, case2)
        
        return dp(0, 0)

