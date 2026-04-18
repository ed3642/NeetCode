# https://leetcode.com/problems/minimum-cost-to-make-at-least-one-valid-path-in-a-grid/
from collections import deque
import heapq
from typing import List

class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        # can do 0-1 bfs and exploring 0 cost paths first
        # we need costs array since each cell can have multiple states, we dont know the optimal choice without comparing it with the costs we have so far.
        
        def is_in_bounds(i, j):
            return 0 <= i < I_BOUNDARY and 0 <= j < J_BOUNDARY
        
        def get_cell_cost(i, j, d_i, d_j):
            direction = grid[i][j]

            if direction == RIGHT and d_j == 1:
                return 0
            if direction == LEFT and d_j == -1:
                return 0
            if direction == DOWN and d_i == 1:
                return 0
            if direction == UP and d_i == -1:
                return 0
            return 1
        
        I_BOUNDARY = len(grid)
        J_BOUNDARY = len(grid[0])

        RIGHT = 1
        LEFT = 2
        DOWN = 3
        UP = 4
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        q = deque([(0, 0, 0)]) # cost, i, j
        costs = [[float('inf')] * J_BOUNDARY for _ in range(I_BOUNDARY)]
        while q:
            cost, i, j = q.popleft()

            if i == I_BOUNDARY - 1 and j == J_BOUNDARY - 1:
                return cost
            
            for d_i, d_j in directions:
                n_i = i + d_i
                n_j = j + d_j
                
                cell_cost = get_cell_cost(i, j, d_i, d_j) # check if the cell arrow points the way were going
                if is_in_bounds(n_i, n_j):
                    cand_cost = cost + cell_cost

                    if cand_cost < costs[n_i][n_j]:
                        costs[n_i][n_j] = cand_cost
                        if cell_cost == 1:
                            q.append((costs[n_i][n_j], n_i, n_j))
                        else:
                            # prio 0 cost
                            q.appendleft((costs[n_i][n_j], n_i, n_j))

        return -1 # shouldnt happen

    def minCost2(self, grid: List[List[int]]) -> int:
        # Djikstras with costs
        
        def is_in_bounds(i, j):
            return 0 <= i < I_BOUNDARY and 0 <= j < J_BOUNDARY
        
        def get_cell_cost(i, j, d_i, d_j):
            direction = grid[i][j]

            if direction == RIGHT and d_j == 1:
                return 0
            if direction == LEFT and d_j == -1:
                return 0
            if direction == DOWN and d_i == 1:
                return 0
            if direction == UP and d_i == -1:
                return 0
            return 1
        
        I_BOUNDARY = len(grid)
        J_BOUNDARY = len(grid[0])

        RIGHT = 1
        LEFT = 2
        DOWN = 3
        UP = 4
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        heap = [(0, 0, 0)] # cost, i, j
        visited = [[False] * J_BOUNDARY for _ in range(I_BOUNDARY)]
        costs = [[float('inf')] * J_BOUNDARY for _ in range(I_BOUNDARY)]
        while heap:
            cost, i, j = heapq.heappop(heap)
            visited[i][j] = True

            if i == I_BOUNDARY - 1 and j == J_BOUNDARY - 1:
                return cost

            for d_i, d_j in directions:
                n_i = i + d_i
                n_j = j + d_j
                
                cell_cost = get_cell_cost(i, j, d_i, d_j) # check if the cell arrow points the way were going
                if is_in_bounds(n_i, n_j) and not visited[n_i][n_j]:
                    cand_cost = cost + cell_cost
                    if cand_cost < costs[n_i][n_j]:
                        costs[n_i][n_j] = cand_cost
                        heapq.heappush(heap, (costs[n_i][n_j], n_i, n_j))
        
        return -1 # shouldnt happen

s = Solution()
print(s.minCost(grid = [[1,1,3],[3,2,2],[1,1,4]]))