class Solution:
    def shortestPalindrome(self, s: str) -> str:

        # kmp 
        # first 1 after the '_' means we found the missing string to make it a palindrome
        pattern = s + '_' + s[::-1]

        N = len(pattern)
        lps = [0] * N
        to_match = 0
        for end in range(1, N):
            while to_match > 0 and pattern[to_match] != pattern[end]:
                to_match = lps[to_match - 1]
            if pattern[to_match] == pattern[end]:
                to_match += 1
            lps[end] = to_match
        
        len_lps = lps[-1]
        missing_part = s[len_lps:][::-1]
        return missing_part + s
