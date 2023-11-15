class Solution:
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
    
s = Solution()

str = " "

print(s.lengthOfLongestSubstring(str))