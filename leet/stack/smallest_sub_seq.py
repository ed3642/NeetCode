# https://leetcode.com/problems/smallest-subsequence-of-distinct-characters

from collections import defaultdict

class Solution:
    def smallestSubsequence(self, s: str) -> str:
        
        N = len(s)
        stack = []
        instack = set()
        last_index = defaultdict(int)

        for i in range(N-1, -1, -1):
            if s[i] not in last_index:
                last_index[s[i]] = i
        
        for i, c in enumerate(s):
            if c not in instack:
                while stack and stack[-1] > c and last_index[stack[-1]] > i:
                    removed = stack.pop()
                    instack.remove(removed)
                stack.append(c)
                instack.add(c)
        
        return ''.join(stack)