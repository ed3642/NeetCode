class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        def expand(i, is_even=False):
            if is_even:
                l = i
                r = i + 1
            else:
                l = i - 1
                r = i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l + 1: r]

        longest = ''
        for i in range(len(s)):
            candidate = expand(i)
            if len(longest) < len(candidate):
                longest = candidate
        for i in range(len(s)):
            candidate = expand(i, True)
            if len(longest) < len(candidate):
                longest = candidate
        
        return longest

    def longestPalindrome(self, s: str) -> str:
        
        def expand(i, reach=0, look_for_even=False):
            nonlocal longest

            l = i - reach
            r = i + reach + (1 if look_for_even else 0) 
            if l < 0 or r >= len(s):
                return
            
            if s[l] == s[r]:
                curr_max_len = longest[1] - longest[0] + 1
                curr_len = r - l + 1
                if curr_max_len < curr_len:
                    longest = (l, r)
                expand(i, reach + 1, look_for_even)
            return

        # start and end of longest
        longest = (0, 0)
        for i in range(len(s)):
            expand(i, 0, False)
            expand(i, 0, True)
        
        start = longest[0]
        end = longest[1]
        return s[start: end + 1]

    # O(n^2), there is a way to do it with also in O(n^2) but slightly better palindrome checking with 2d dp
    # O (1) space, DP method uses O(n^2) space
    def longestPalindrome2(self, s: str) -> str:

        def expand(is_even_length=False):
            for i in range(n):
                l = i
                r = i if is_even_length else i + 1
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
    def longestPalindrome3(self, s: str) -> str:
        # start at endpoints and check if its pal with dp
        # dp[i][j] = s[i] == s[j] and (dp[i + 1][j - 1] or length < 2)

        n = len(s)
        dp = [[False] * n for _ in range(n)] # True if dp[i][j] is pal
        for i in range(n):
            dp[i][i] = True
        
        longest = s[0]
        # weird iteration order to guarantee that dp[i + 1][j - 1] is calculated before dp[i][j]
        # for the i you need to be coming from the right (dependency [i + 1])
        # for the j you need to be coming from the left (dependency [j - 1])
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                length = j - i + 1
                dp[i][j] = s[i] == s[j] and (dp[i + 1][j - 1] or length <= 2)
                if dp[i][j] and length > len(longest):
                    longest = s[i:j + 1]
        
        return longest