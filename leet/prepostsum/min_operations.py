# https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box
from typing import List

class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        
        # [1,1,0]
        # [1,2,2]
        # [0,1,3]

        # [2,1,0]
        # [1,0,0]

        N = len(boxes)
        boxes = [int(num) for num in boxes]
        pref_sum = boxes
        post_sum = boxes.copy()
        for i in range(1, N):
            pref_sum[i] += pref_sum[i - 1]
        moves_left = [0] * N
        for i in range(1, N):
            moves_left[i] += pref_sum[i - 1] + moves_left[i - 1]

        moves_right = [0] * N
        for i in range(N - 2, -1, -1):
            post_sum[i] += post_sum[i + 1]
        for i in range(N - 2, -1, -1):
            moves_right[i] += post_sum[i + 1] + moves_right[i + 1]
        
        res = [0] * N
        for i in range(N):
            res[i] = moves_left[i] + moves_right[i]
        
        return res