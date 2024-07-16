# https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses
from collections import defaultdict

class Solution:
    # nice solution
    # O(n) wormhole technique
    def reverseParentheses(self, s: str) -> str:
        # link the parenthesis
        # reverse direction when entering wormhole
        # just append to result in order we see

        portals = defaultdict(int)
        lefts = []
        for i, ch in enumerate(s):
            if ch == '(':
                lefts.append(i)
            elif ch == ')':
                last_left = lefts.pop()
                portals[last_left] = i
                portals[i] = last_left

        res = []
        i = 0
        d_i = 1 # direction
        while 0 <= i < len(s):
            ch = s[i]
            if ch == '(' or ch == ')': # reverse teleport and direction
                d_i *= -1
                i = portals[i]
                i += d_i
            else:
                res.append(s[i])
                i += d_i
        
        return ''.join(res)


    # brute force, O(n^2)
    def reverseParentheses2(self, s: str) -> str:
        
        stack = []

        for ch in s:
            if ch != '(' and not stack:
                stack.append([ch])
                continue
            if ch == '(': # start building a new word
                stack.append([])
            elif ch == ')': # close the last word
                word = stack.pop()
                if stack:
                    stack[-1] += list(reversed(word))
                else:
                    stack.append(list(reversed(word)))
            else:
                stack[-1].append(ch)
        
        return ''.join(stack[-1])
    