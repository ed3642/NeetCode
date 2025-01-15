# https://leetcode.com/problems/minimum-window-substring
from collections import Counter, defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        N = len(s)
        target_counts = Counter(t)
        counts = defaultdict(int)
        need = len(t)
        shortest_str = ''

        l = 0
        for r in range(N):
            # remove the first char that in needed in the window
            while l < r and need == 0:
                if counts[s[l]] == target_counts[s[l]]:
                    need += 1
                counts[s[l]] -= 1
                l += 1

            # keep track of the counts
            if counts[s[r]] < target_counts[s[r]]:
                need -= 1
            counts[s[r]] += 1

            # shrink windown as much as possible
            while l < r and need == 0:
                if counts[s[l]] == target_counts[s[l]]:
                    break # dont remove any that we need
                counts[s[l]] -= 1
                l += 1

            if need == 0:
                if shortest_str == '' or r - l + 1 < len(shortest_str):
                    shortest_str = s[l:r + 1]
            
        return shortest_str
