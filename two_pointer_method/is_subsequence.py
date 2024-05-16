class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False
        if len(s) == 0:
            return True

        a = 0
        b = 0

        while b < len(t):
            looking_for = s[a]

            while b < len(t) and t[b] != looking_for:
                b += 1
            
            if b >= len(t):
                return False
            if a >= len(s) - 1:
                return True
            a += 1
            b += 1
        
        return False