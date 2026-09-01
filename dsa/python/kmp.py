# O(n + m)
def kmp(self, elems: str, looking_for: str) -> int:
    # kmp
    def matcher(string, pattern):
        N = len(string)
        M = len(pattern)
        lsp = get_lsp(pattern)
        to_match = 0

        for end in range(N):
            while to_match > 0 and string[end] != pattern[to_match]:
                to_match = lsp[to_match - 1]
            if string[end] == pattern[to_match]:
                to_match += 1
            if to_match == M:
                return end - M + 1
        
        return -1

    def get_lsp(pattern):
        N = len(pattern)
        lsp = [0] * N
        to_match = 0

        for end in range(1, N):
            while to_match > 0 and pattern[to_match] != pattern[end]:
                to_match = lsp[to_match - 1]
            if pattern[to_match] == pattern[end]:
                to_match += 1
            lsp[end] = to_match
        
        return lsp

    return matcher(elems, looking_for)