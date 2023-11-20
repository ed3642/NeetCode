from collections import Counter

class Solution:
    # k is like a budget
    # O(n)
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        r = 0
        n = len(s)
        counter = Counter()
        most_common_count = 0
        window_length = 0

        # build window
        while r < n:
            next_char = s[r]
            counter[next_char] += 1
            most_common_count = max(most_common_count, counter[next_char])
            window_length = r - l + 1
            spent = window_length - most_common_count
            if spent > k: # cant afford next char
                counter[s[l]] -= 1
                l += 1
            r += 1

        return window_length # this is the longest the window gets
    
s = Solution()

print(s.characterReplacement("AAABB", 1))