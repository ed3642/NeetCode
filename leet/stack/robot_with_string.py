# https://leetcode.com/problems/using-a-robot-to-print-the-lexicographically-smallest-string

from collections import Counter

class Solution:
    def robotWithString(self, s: str) -> str:
        # same as below but with ordinal values

        counts = Counter(s)
        looking_for = ord('a')
        max_lf = ord('a') + 26

        res = []
        stack = []

        n = len(s)
        i = 0
        while i < n:
            while looking_for < max_lf and counts[chr(looking_for)] > 0:
                # have smaller in stack
                while stack and stack[-1] <= chr(looking_for):
                    res.append(stack.pop())
                if s[i] == chr(looking_for):
                    res.append(s[i])
                else:
                    stack.append(s[i])
                counts[s[i]] -= 1
                i += 1
            looking_for += 1

        res.extend(reversed(stack))
        return ''.join(res)

    def robotWithString(self, s: str) -> str:

        counts = Counter(s)
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        looking_for_i = 0

        res = []
        stack = []

        n = len(s)
        i = 0
        while i < n:
            while looking_for_i < len(alphabet) and counts[alphabet[looking_for_i]] > 0:
                # have smaller in stack
                while stack and stack[-1] <= alphabet[looking_for_i]:
                    res.append(stack.pop())
                if s[i] == alphabet[looking_for_i]:
                    res.append(s[i])
                else:
                    stack.append(s[i])
                counts[s[i]] -= 1
                i += 1
            looking_for_i += 1

        res.extend(reversed(stack))
        return ''.join(res)
    