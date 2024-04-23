class Solution:
    # O(n^2), there is a way to do it with also in O(n^2) but slightly better palindrome checking with 2d dp
    def longestPalindrome(self, s: str) -> str:

        def expand(isEvenLenght=False):
            for i in range(n):
                l = i
                r = i if isEvenLenght else i + 1
                while l >= 0 and r < n:
                    length = r - l + 1
                    if s[l] == s[r] and length > self.max_len:
                        bounds[0] = l
                        bounds[1] = r + 1
                        self.max_len = length
                    elif s[l] != s[r]:
                        break
                    l -= 1
                    r += 1

        n = len(s)
        bounds = [0,0]
        self.max_len = 0

        expand()
        expand(True)

        return s[bounds[0]: bounds[1]]
    
    # O(n^2) dp
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[]]
        ...