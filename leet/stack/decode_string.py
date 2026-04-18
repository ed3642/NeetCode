# https://leetcode.com/problems/decode-string
class Solution:
    def decodeString(self, s: str) -> str:
        
        def parse_digit(i):
            while i < N and s[i].isdigit():
                i += 1
            return i
        
        def parse_alpha(i):
            while i < N and s[i].isalpha():
                i += 1
            return i
        
        def handle_string_appendment(string):
            if stack and not stack[-1].isdigit():
                stack[-1] += string # concat with top of stack alpha string
            else:
                stack.append(string)

        N = len(s)
        stack = []

        i = 0
        while i < N:
            if s[i].isdigit():
                next_i = parse_digit(i)
                stack.append(s[i:next_i])
                i = next_i
            elif s[i].isalpha():
                next_i = parse_alpha(i)
                handle_string_appendment(s[i:next_i])
                i = next_i
            elif s[i] == ']':
                alpha = stack.pop()
                mult = int(stack.pop()) if (stack and stack[-1].isdigit()) else 1
                expanded = alpha * mult
                handle_string_appendment(expanded)
                i += 1
            else: # a [
                i += 1
        
        return ''.join(stack)

    def decodeString(self, s: str) -> str:

        stack = [] # keep track of multiplier and last_builder
        builder = ''
        mult = 0

        for ch in s:
            if ch.isdigit():
                mult = mult * 10 + int(ch)
            elif ch == '[':
                stack.append((mult, builder))
                mult = 0
                builder = ''
            elif ch == ']':
                prev_mult, prev_builder = stack.pop()
                builder = prev_builder + prev_mult * builder
            else:
                builder = builder + ch
        
        return builder

