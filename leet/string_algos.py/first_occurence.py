# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string 
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

    # O(n + m)
    def strStr(self, haystack: str, needle: str) -> int:
        # kmp
        def matcher(string, pattern):
            N = len(string)
            M = len(pattern)
            lsp = get_lsp(pattern)
            to_match = 0

            for end in range(N):
                # see if we can save a bit of work by not going all the way back to 0
                while to_match > 0 and string[end] != pattern[to_match]:
                    to_match = lsp[to_match - 1]
                if string[end] == pattern[to_match]:
                    to_match += 1
                if to_match == M:
                    return end - M + 1
            
            return -1

        # longest prefix suffix
        def get_lsp(pattern):
            N = len(pattern)
            lsp = [0] * N
            to_match = 0

            for end in range(1, N):
                # see if we can save a bit of work by not going all the way back to 0
                while to_match > 0 and pattern[to_match] != pattern[end]:
                    to_match = lsp[to_match - 1]
                if pattern[to_match] == pattern[end]:
                    to_match += 1
                lsp[end] = to_match
            
            return lsp

        return matcher(haystack, needle)