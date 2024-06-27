from functools import lru_cache

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # at first i had is_valid(i1, i2, i3) but we can just calculate i3 from the other 2 variables
        @lru_cache(maxsize=None)
        def is_valid(i1, i2):
            nonlocal n1, n2, n3
            i3 = i1 + i2
            if i1 == n1 and i2 == n2 and i3 == n3:
                return True
            if i3 >= n3:
                return False
            
            if (i1 < n1 and i2 < n2) and s3[i3] == s1[i1] == s2[i2]:
                return (is_valid(i1 + 1, i2) or # try the letter from s1
                        is_valid(i1, i2 + 1)) # try the letter from s2
            if i1 < n1 and s3[i3] == s1[i1]:
                return is_valid(i1 + 1, i2)
            if i2 < n2 and s3[i3] == s2[i2]:
                return is_valid(i1, i2 + 1)
            
            return False
        
        n1 = len(s1)
        n2 = len(s2)
        n3 = len(s3)

        if n1 + n2 < n3:
            return False
        
        return is_valid(0, 0)
    