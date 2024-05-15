class Solution:
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

