from functools import lru_cache

class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        # seems like minumum edit distance, but only consider deletion
        # not that fast, trying to prune it causes memory limit exceeded
        # good candidate for tabulation but this is good enough 

        @lru_cache(maxsize=None)
        def dp(w1_i, w2_i) -> int:
            
            # add the sum of the chars we didnt get to and need to delete
            if w1_i >= len(s1):
                return add_ascii(w2_i, s2)
            if w2_i >= len(s2):
                return add_ascii(w1_i, s1)

            if s1[w1_i] == s2[w2_i]:
                return dp(w1_i + 1, w2_i + 1)
            
            delete_from_w1 = dp(w1_i + 1, w2_i) + ord(s1[w1_i])
            delete_from_w2 = dp(w1_i, w2_i + 1) + ord(s2[w2_i])

            return min(delete_from_w1, delete_from_w2)
            
        def add_ascii(start, string):
            total = 0
            for i in range(start, len(string)):
                total += ord(string[i]) # ascii val
            return total
        
        return dp(0, 0)
