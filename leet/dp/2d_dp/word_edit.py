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