from functools import lru_cache

class Solution:
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
