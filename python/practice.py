# https://leetcode.com/problems/longest-valid-parentheses

class Solution:
    def longestValidParentheses(self, s: str) -> int:

        # (()()) ( ()
        
        stack = []
        max_len = 0
        last_valid_end = 0
        last_valid_size = 0

        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            elif stack:
                prev_l_i = stack.pop()
                length = i - prev_l_i + 1
                if prev_l_i == last_valid_end + 1:
                    length += last_valid_size
                if length >= max_len:
                    max_len = length
                last_valid_end = i
                last_valid_size = length

        return max_len
    
s = Solution()
print(s.longestValidParentheses("()(())"))