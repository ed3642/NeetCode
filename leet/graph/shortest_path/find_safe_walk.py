# https://leetcode.com/problems/find-a-safe-walk-through-a-grid

import heapq
from typing import List

class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        
        def is_in_bounds(i, j):
            return 0 <= i < N and 0 <= j < M

        N = len(grid)
        M = len(grid[0])

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        INF = float('inf')
        max_health = [[-INF for _ in range(M)] for _ in range(N)]
        max_health[0][0] = health-grid[0][0]
        visited = [[False for _ in range(M)] for _ in range(N)]

        h = [(-max_health[0][0], 0, 0)]

        while h:
            neg_hp, i, j = heapq.heappop(h)
            hp = -neg_hp

            visited[i][j] = True

            if hp <= 0:
                continue
            
            if i == N-1 and j == M-1:
                return True

            for di, dj in directions:
                ni, nj = i+di, j+dj
                if is_in_bounds(ni, nj) and not visited[ni][nj]:
                    cand_hp = hp-grid[ni][nj]
                    if max_health[ni][nj] < cand_hp:
                        max_health[ni][nj] = cand_hp
                        heapq.heappush(h, (-cand_hp, ni, nj))

        return False

    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        
        def is_in_bounds(i, j):
            return 0 <= i < N and 0 <= j < M

        def dfs(i, j, hp):
            nonlocal works
            if hp <= 0:
                return
            
            if i == N-1 and j == M-1:
                works = True
                return

            for di, dj in directions:
                ni, nj = i+di, j+dj
                if is_in_bounds(ni, nj):
                    cand_hp = hp-grid[ni][nj]
                    if max_health[ni][nj] < cand_hp:
                        max_health[ni][nj] = cand_hp
                        dfs(ni, nj, cand_hp)

        N = len(grid)
        M = len(grid[0])

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        INF = float('inf')
        max_health = [[-INF for _ in range(M)] for _ in range(N)]
        max_health[0][0] = health-grid[0][0]
        works = False
        
        dfs(0, 0, max_health[0][0])

        return works