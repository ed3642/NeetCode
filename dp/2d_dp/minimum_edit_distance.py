from functools import lru_cache

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        @lru_cache(maxsize=None)
        def dp(len_str_1, len_str_2):
            
            if len_str_1 == 0:
                return len_str_2
            if len_str_2 == 0:
                return len_str_1
            
            if word1[len_str_1 - 1] == word2[len_str_2 - 1]:
                return dp(len_str_1 - 1, len_str_2 - 1)
            else:
                insert_cost = dp(len_str_1, len_str_2 - 1)
                delete_cost = dp(len_str_1 - 1, len_str_2)
                replace_cost = dp(len_str_1 - 1, len_str_2 - 1)
                
                return min(insert_cost, delete_cost, replace_cost) + 1
        
        return dp(len(word1), len(word2))
