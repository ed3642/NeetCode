class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        # KMP
        # aabbaa
        # lps [0,1,0,0,0,1]

        def calc_lps():
            lps = [0] * N
            matcher_i = 0
            for i in range(1, N):
                while matcher_i > 0 and needle[i] != needle[matcher_i]:
                    matcher_i = lps[matcher_i - 1]
                if needle[i] == needle[matcher_i]:
                    matcher_i += 1
                lps[i] = matcher_i
            return lps

        N = len(needle)
        lps = calc_lps()

        matcher_i = 0
        for i in range(len(haystack)):
            while matcher_i > 0 and haystack[i] != needle[matcher_i]:
                matcher_i = lps[matcher_i - 1]
            if haystack[i] == needle[matcher_i]:
                matcher_i += 1
            if matcher_i == N:
                return i - N + 1
        
        return -1

s = Solution()
print(s.strStr(haystack = "baabbaa", needle = "aabbaa"))