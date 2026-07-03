# https://leetcode.com/problems/number-of-substrings-containing-all-three-characters

from collections import defaultdict

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        # keep track of the starting position of the latest valid substring
        # all substrs before it are also valid
        latest_i = {}
        valid_strs = 0

        for i, c in enumerate(s):
            latest_i[c] = i

            if len(latest_i) == 3:
                valid_strs += min(latest_i.values()) + 1
        
        return valid_strs
    
    def numberOfSubstrings(self, s: str) -> int:

        # abcabc
        # 4+3+2+1
        
        N = len(s)
        f = defaultdict(int)
        count = 0
        
        l = 0
        for r in range(N):
            right_c = s[r]
            f[right_c] += 1
            while len(f) == 3:
                c = s[l]
                f[c] -= 1
                if f[c] == 0:
                    del f[c]
                count += N-r
                l += 1
        
        return count

    def numberOfSubstrings(self, s: str) -> int:
        
        N = len(s)
        l = 0
        counts = defaultdict(int)
        valid_strs = 0
        for r in range(N):
            counts[s[r]] += 1

            # shrink to invalid
            while l < r and len(counts) == 3:
                # valid substrings to the right
                valid_strs += N - r

                counts[s[l]] -= 1
                if counts[s[l]] == 0:
                    del counts[s[l]]

                l += 1
            
        return valid_strs
