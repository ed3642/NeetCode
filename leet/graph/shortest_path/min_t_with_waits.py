# https://leetcode.com/problems/find-minimum-time-to-reach-last-room-i

import heapq
from typing import List

class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:

        def is_valid(i, j):
            return 0 <= i < N and 0 <= j < M and not visited[i][j]
        
        N = len(moveTime)
        M = len(moveTime[0])

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        heap = [(0, 0, 0)] # i, j, time
        visited = [[False] * M for _ in range(N)]
        times = [[float('inf')] * M for _ in range(N)]
        times[0][0] = 0

        while heap:
            t, i, j = heapq.heappop(heap)

            if i == N - 1 and j == M - 1:
                return t

            for d_i, d_j in directions:
                n_i = i + d_i
                n_j = j + d_j
                if is_valid(n_i, n_j):
                    if t >= moveTime[n_i][n_j]:
                        visited[n_i][n_j] = True
                        cand_t = t + 1
                        if cand_t < times[n_i][n_j]:
                            heapq.heappush(heap, (cand_t, n_i, n_j))
                    else:
                        visited[n_i][n_j] = True
                        cand_t = moveTime[n_i][n_j] + 1
                        if cand_t < times[n_i][n_j]:
                            heapq.heappush(heap, (cand_t, n_i, n_j))

        return -1