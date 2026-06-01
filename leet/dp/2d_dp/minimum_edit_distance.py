# https://leetcode.com/problems/edit-distance

from functools import lru_cache

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        @lru_cache(maxsize=None)
        def dp(i, j):

            if i == len(word1) and j == len(word2):
                return 0
            
            if i == len(word1):
                return len(word2) - j
            if j == len(word2):
                return len(word1) - i

            if word1[i] == word2[j]:
                return dp(i + 1, j + 1)
            
            insert = dp(i, j + 1)
            delete = dp(i + 1, j)
            replace = dp(i + 1, j + 1)

            return min(insert, delete, replace) + 1
        
        return dp(0, 0)

    def minDistance(self, word1: str, word2: str) -> int:

        if not word1:
            return len(word2)
        if not word2:
            return len(word1)

        # do with bu dp
        INF = float('inf')
        n = len(word1)
        m = len(word2)
        # dp[i][j] min ops to make strings eq up to i and j on each string respectively
        dp = [[INF for _ in range(m+1)] for _ in range(n+1)]
        dp[0][0] = 0 # empty strings
        
        for i in range(1, n+1): # empty word2, cost is all of remaining word1
            dp[i][0] = i
        for j in range(1, m+1): # empty word1
            dp[0][j] = j

        for i in range(1, n+1):
            for j in range(1, m+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = min(dp[i-1][j-1], dp[i][j]) # equal
                else:
                    dp[i][j] = min(dp[i][j-1]+1, # insert
                                dp[i-1][j]+1, # delete
                                dp[i-1][j-1]+1) # replace

        return dp[n][m]
        
    def minDistance(self, word1: str, word2: str) -> int:
        
        @lru_cache(maxsize=None)
        def min_actions(i1, i2):
            if i1 >= len(word1) and i2 >= len(word2):
                return 0
            if i1 >= len(word1) and not i2 >= len(word2):
                return min_actions(i1, i2 + 1) + 1 # insert the rest of word2
            if not i1 >= len(word1) and i2 >= len(word2):
                return min_actions(i1 + 1, i2) + 1 # delete from word1 to make word2
            if word1[i1] == word2[i2]:
                return min_actions(i1 + 1, i2 + 1)
            
            return min(
                min_actions(i1, i2 + 1), # insert
                min_actions(i1 + 1, i2), # delete
                min_actions(i1 + 1, i2 + 1) # replace
            ) + 1

        return min_actions(0, 0)

    def minDistance(self, word1: str, word2: str) -> int:
        
        @lru_cache(maxsize=None)
        def dp(w1_i, w2_i):
            
            # reaching the end of a word, remaining operations is how many letters we didnt get to in the other word
            if w1_i >= len(word1):
                return len(word2) - w2_i
            if w2_i >= len(word2):
                return len(word1) - w1_i
            
            if word1[w1_i] == word2[w2_i]:
                return dp(w1_i + 1, w2_i + 1) # already equal
            
            replace = dp(w1_i + 1, w2_i + 1) # represents that we moved what we need from w2 and replacing it with a letter we dont need in w1, so we dealt with both positions
            remove = dp(w1_i + 1, w2_i) # represents dealing with the letter we need to get rid of in w1
            insert = dp(w1_i, w2_i + 1) # represents dealing with the letter we need from w2 and putting in it w1

            return min(replace, remove, insert) + 1
        
        return dp(0, 0)
