# https://leetcode.com/problems/find-minimum-time-to-reach-last-room-ii

import heapq
from typing import List

class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        
        def is_valid(i, j):
            return 0 <= i < N and 0 <= j < M and times[i][j] == float('inf')
        
        def calc_cost(parity):
            return 1 if parity == 0 else 2

        N = len(moveTime)
        M = len(moveTime[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        heap = [(0, 0, 0, 0)] # time, i, j, parity
        times = [[float('inf')] * M for _ in range(N)]
        times[0][0] = 0

        while heap:
            t, i, j, parity = heapq.heappop(heap)

            if i == N - 1 and j == M - 1:
                return t

            for d_i, d_j in directions:
                n_i = i + d_i
                n_j = j + d_j
                if is_valid(n_i, n_j):
                    cost = calc_cost(parity)
                    if t >= moveTime[n_i][n_j]:
                        cand_cost = t + cost
                    else:
                        cand_cost = moveTime[n_i][n_j] + cost
                    if cand_cost < times[n_i][n_j]:
                        times[n_i][n_j] = cand_cost
                        heapq.heappush(heap, (cand_cost, n_i, n_j, parity ^ 1))

        return -1