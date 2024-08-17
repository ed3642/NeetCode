class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        
        start = 0
        longest = 1
        in_window = set([s[0]])
        
        for end in range(1, len(s)):
            while s[end] in in_window:
                in_window.remove(s[start])
                start += 1
            in_window.add(s[end])
            longest = max(end - start + 1, longest)
        
        return longest

    # sliding window with set
    # O(n)
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        n = len(s)
        hs = set()
        max_length = 0

        while r < n:
            if not s[r] in hs:
                hs.add(s[r])
                r += 1
            else:
                max_length = max(len(hs), max_length)

                # remove elems from hs until r can move up again
                while s[r] in hs:
                    hs.remove(s[l])
                    l += 1
        
        return max(len(hs), max_length)
