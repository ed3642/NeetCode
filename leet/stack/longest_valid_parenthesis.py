# https://leetcode.com/problems/longest-valid-parentheses

class Solution:

    def longestValidParentheses(self, s: str) -> int:
        # the interesting paradigm here is that we store the last invalid index
        # as a starting point
        # ())
        
        stack = [-1] # starting point
        max_size = 0

        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                if stack:
                    max_size = max(i - stack[-1], max_size)
                else:
                    stack.append(i)
        
        return max_size

    def longestValidParentheses(self, s: str) -> int:

        # left to right and right to left
        # see if left == right then we have valid brackets
        # ()) only caught by left to right
        # (() only caught by right to left

        l = 0
        r = 0
        max_len = 0
        for c in s:
            if c == '(':
                l += 1
            else:
                r += 1
            if l == r:
                max_len = max(l + r, max_len)
            if r > l: # reset when string can never become valid again ex. ())
                l = 0 
                r = 0
        l = 0
        r = 0
        for c in reversed(s):
            if c == ')':
                r += 1
            else:
                l += 1
            if l == r:
                max_len = max(l + r, max_len)
            if l > r: # reset when string can never become valid again ex. (()
                l = 0
                r = 0

        return max_len
        