class Solution:
    # O(n)
    def repeatedSubstringPattern(self, s: str) -> bool:
        
        # kmp
        def get_lps(pattern):
            N = len(pattern)
            lps = [0] * N
            to_match = 0

            for end in range(1, N):
                while to_match > 0 and pattern[to_match] != pattern[end]:
                    to_match = lps[to_match - 1]
                if pattern[to_match] == pattern[end]:
                    to_match += 1
                lps[end] = to_match

            return lps

        N = len(s)
        lps = get_lps(s)
        print(lps)
        elems_repeated = lps[-1]
        pattern_length = N - elems_repeated
        
        if N % pattern_length != 0 or pattern_length == 0:
            return False
        return True
    
    # O(n)
    def repeatedSubstringPattern(self, s: str) -> bool:

        # string pattern repetition detection
        return s in (s + s)[1:-1]