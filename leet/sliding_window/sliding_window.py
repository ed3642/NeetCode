# https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks

class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        
        N = len(blocks)
        l = 0
        w_count = 0

        for r in range(k):
            if blocks[r] == 'W':
                w_count += 1

        min_w_count = w_count

        for r in range(k, N):
            if blocks[r] == 'W':
                w_count += 1
            if blocks[l] == 'W':
                w_count -= 1
            min_w_count = min(w_count, min_w_count)
            l += 1
        
        return min_w_count