# https://leetcode.com/problems/shifting-letters-ii
from typing import List

class FenwickTree:
    def __init__(self, N):
        self.tree = [0] * (N + 1)
        self.N = N

    def update(self, i, delta):
        while i <= self.N:
            self.tree[i] += delta
            i += (i & -i)

    def query(self, i):
        _sum = 0
        while i > 0:
            _sum += self.tree[i]
            i -= (i & -i)
        return _sum

class Solution:

    # O(n + m) n=len(s) m=len(shifts)
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        
        # aggregate all shifts into 1
        # apply the complete shift
        # mark starts as 1 * dir and ends as -1 * dir
        # prefixsum the marked array
        # this acts as a range sum

        N = len(s)
        marked_ends = [0] * (N + 1)

        for start, end, dir in shifts:
            processed_dir = dir if dir == 1 else -1
            marked_ends[start] += processed_dir
            marked_ends[end + 1] -= processed_dir
        
        pf_sum = marked_ends
        for i in range(1, N + 1):
            pf_sum[i] += pf_sum[i - 1]
        
        res = [c for c in s]
        for i in range(N):
            shift = pf_sum[i]
            res[i] = chr(((ord(s[i]) - ord('a') + shift) % 26) + ord('a'))
        
        return ''.join(res)
    
    # O(n log n)
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:

        N = len(s) + 1 # need to add 1 to end's to mark them properly 
        ft_sum = FenwickTree(N)

        for start, end, dir in shifts:
            processed_dir = dir if dir == 1 else -1
            ft_sum.update(start + 1, processed_dir)
            ft_sum.update(end + 2, -processed_dir)
        
        res = [c for c in s]
        for i in range(N - 1):
            shift = ft_sum.query(i + 1)
            res[i] = chr(((ord(s[i]) - ord('a') + shift) % 26) + ord('a'))
        
        return ''.join(res)