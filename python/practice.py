# https://leetcode.com/problems/shortest-path-in-binary-matrix
from collections import defaultdict
import heapq
from typing import List

class Solution:
    # we can do A* since we know the start and end nodes
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # f = g + h

        def is_valid(i, j):
            return (i >= 0 and i < MAX_I and
                    j >= 0 and j < MAX_J and
                    grid[i][j] == 0)

        # cherbyshev
        def heuristic(i, j):
            return max(abs((MAX_I - 1) - i), abs((MAX_J - 1) - j))
        
        if grid[0][0] == 1:
            return -1

        MAX_I = len(grid)
        MAX_J = len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        distances = defaultdict(lambda: float('inf'))
        distances[(0, 0)] = 1 # we count the starting node in this problem
        starting_prio = distances[(0, 0)] + heuristic(0, 0)
        heap = [(starting_prio, 0, 0)]

        while heap:
            prio, i, j = heapq.heappop(heap)

            grid[i][j] == 1 # mark visited

            if i == MAX_I - 1 and j == MAX_J - 1:
                return distances[(i, j)]

            for d_i, d_j in directions:
                n_i = i + d_i
                n_j = j + d_j
                if is_valid(n_i, n_j):
                    cand_g = distances[(i, j)] + 1
                    if cand_g < distances[(n_i, n_j)]:
                        distances[(n_i, n_j)] = cand_g
                        f = cand_g + heuristic(n_i, n_j)
                        heapq.heappush(heap, (f, n_i, n_j))

        return -1