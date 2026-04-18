
class Solution:
    def countSubstrings(self, s: str) -> int:
        # like longest pal problem
        # but instead of keeping track of the max, keep a count
        
        def expand(i, reach=0, look_for_even=False):
            nonlocal count

            l = i - reach
            r = i + reach + (1 if look_for_even else 0) 
            if l < 0 or r >= len(s):
                return
            
            if s[l] == s[r]:
                count += 1
                expand(i, reach + 1, look_for_even)
            return

        count = 0
        for i in range(len(s)):
            expand(i, 0, False)
            expand(i, 0, True)
        
        return count