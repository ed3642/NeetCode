class Solution:
    # O(n + m)
    def strStr(self, haystack: str, needle: str) -> int:
        # kmp
        def matcher(string, pattern):
            M = len(pattern)
            if M == 0:
                return 0
            lps = get_lps(pattern)
            matches = 0
            for i in range(len(string)):
                while matches > 0 and pattern[matches] != string[i]:
                    matches = lps[matches - 1]
                if pattern[matches] == string[i]:
                    matches += 1
                if matches == M:
                    return i - M + 1 # could append instead of returning to get a list of all occurences
                    #matches = lsp[matches] for getting the list of all occurences
            return -1

        def get_lps(pattern):
            lps = [0] * len(pattern)
            matched = 0
            for i in range(1, len(pattern)):
                while matched > 0 and pattern[matched] != pattern[i]:
                    matched = lps[matched - 1]
                if pattern[matched] == pattern[i]:
                    matched += 1
                lps[i] = matched
            return lps

        return matcher(haystack, needle)