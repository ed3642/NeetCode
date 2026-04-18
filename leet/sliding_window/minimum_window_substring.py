# https://leetcode.com/problems/minimum-window-substring
from collections import Counter, defaultdict

class Solution:
    # O(n + m)
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

    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t): return ''

        substring_counter = Counter(t)
        temp_counter = substring_counter.copy()
        counter = Counter()
        n = len(s)
        l = 0
        r = 0
        min_length = float('inf')
        min_string = ''

        # slide start to first encounter of 't' char
        while l < n and not s[l] in substring_counter:
            l += 1
        r = l
        if r == n:
            return ''

        # build window until all chars are in
        while temp_counter and r < n:
            char = s[r]
            counter[char] += 1
            if char in temp_counter:
                temp_counter[char] -= 1
                if temp_counter[char] == 0:
                    del temp_counter[char]
            r += 1
        r -= 1
        if r == n - 1 and temp_counter:
            return ''
        min_length = min(r - l + 1, min_length)
        min_string = s[l:r + 1]

        keep_search = True
        while keep_search:
            last_char = s[l]
            if r < n and counter[last_char] <= substring_counter[last_char]: # cant afford to drop last char
                r += 1
                while r < n:
                    counter[s[r]] += 1
                    if s[r] == last_char:
                        break
                    r += 1
                if r == n: # could not find replacement so min window is set
                    keep_search = False 
                    break
            # slide back of window up until another 't' char is met
            counter[last_char] -= 1
            l += 1
            while not s[l] in substring_counter:
                counter[l] -= 1
                l += 1
            if r - l + 1< min_length:
                min_length = r - l + 1
                min_string = s[l:r + 1]
            
        return min_string
    
    # written by copilot based on my code
    def minWindow(s: str, t: str) -> str:
        if len(s) < len(t): return ''

        substring_counter = Counter(t)
        counter = Counter()
        l = r = 0
        min_length = float('inf')
        min_string = ''

        for r, c in enumerate(s):
            if c in substring_counter:
                counter[c] += 1
            while counter & substring_counter == substring_counter:
                if r - l + 1 < min_length:
                    min_length = r - l + 1
                    min_string = s[l:r+1]
                d = s[l]
                if d in substring_counter:
                    counter[d] -= 1
                l += 1

        return min_string if min_length <= len(s) else ''


s = Solution()

print(s.minWindow("a", "a"))