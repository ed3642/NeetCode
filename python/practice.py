class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        def gen_lsp(pattern):
            lsp = [0] * N
            to_match = 0
            for end in range(1, N):
                while to_match > 0 and pattern[end] != pattern[to_match]:
                    to_match = lsp[to_match - 1]
                if pattern[end] == pattern[to_match]:
                    to_match += 1
                lsp[end] = to_match
            return lsp

        N = len(needle)
        lsp = gen_lsp(needle)
        to_match = 0
        for end in range(len(haystack)):
            while to_match > 0 and haystack[end] != needle[to_match]:
                to_match = lsp[to_match - 1]
            if haystack[end] == needle[to_match]:
                to_match += 1
            if to_match == N:
                return end - N + 1
        return -1

