from functools import lru_cache

class Solution:
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
