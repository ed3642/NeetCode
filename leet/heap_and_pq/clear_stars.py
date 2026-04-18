# https://leetcode.com/problems/lexicographically-minimum-string-after-removing-stars

from collections import defaultdict
import heapq

class Solution:
    def clearStars(self, s: str) -> str:
        
        positions = defaultdict(list)
        res = [c for c in s]
        heap = [] # keep track of the smallest c

        for i, c in enumerate(s):
            if c == '*':
                res[i] = ''
                smallest_c = heap[0]
                smallest_i = positions[smallest_c].pop()
                if len(positions[smallest_c]) == 0:
                    heapq.heappop(heap)
                res[smallest_i] = ''
            else:
                if len(positions[c]) == 0:
                    heapq.heappush(heap, c)
                positions[c].append(i)
        
        return ''.join(res)