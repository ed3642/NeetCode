# https://leetcode.com/problems/find-the-safest-path-in-a-grid

from collections import deque
from typing import List

class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:

        # [[3,2,1,f],
        #  [2,3,2,1],
        #  [1,2,3,2],
        #  [f,1,2,3]]

        def works(sf):
            def dfs(i, j):
                nonlocal can_reach
                if can_reach:
                    return
                if i == N-1 and j == M-1:
                    can_reach = True
                    return

                for di, dj in directions:
                    ni, nj = i+di, j+dj
                    if is_in_bounds(ni, nj) and grid[ni][nj] >= sf and not visited[ni][nj]:
                        visited[ni][nj] = True
                        dfs(ni, nj)

            if grid[0][0] < sf:
                return False
            visited = [[False for _ in range(M)] for _ in range(N)]
            visited[0][0] = True
            can_reach = False
            dfs(0, 0)
            return can_reach
        
        def is_in_bounds(i, j):
            return 0 <= i < N and 0 <= j < M

        N = len(grid)
        M = len(grid[0])

        if grid[0][0] == 1 or grid[N-1][M-1] == 1:
            return 0

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        thiefs = []

        for i in range(N):
            for j in range(M):
                if grid[i][j] == 1:
                    thiefs.append([i, j])
                    grid[i][j] = 0
                else:
                    grid[i][j] = float('inf')
        
        # naive way to calc dist to each thief
        # for i in range(N):
        #     for j in range(M):
        #         if grid[i][j] != 0:
        #             for ti, tj in thiefs:
        #                 grid[i][j] = min(grid[i][j], abs(ti-i)+abs(tj-j))

        # better way to get thief dist to cell
        q = deque(thiefs)
        visited = [[False for _ in range(M)] for _ in range(N)]
        for i, j in thiefs:
            visited[i][j] = True
            grid[i][j] = 0

        depth = 1
        while q:
            for _ in range(len(q)):
                i, j = q.popleft()

                for di, dj in directions:
                    ni, nj = i+di, j+dj
                    if is_in_bounds(ni, nj) and not visited[ni][nj]:
                        visited[ni][nj] = True
                        grid[ni][nj] = depth
                        q.append([ni, nj])
            depth += 1
            
        # binary search max safe factor, binary search maximize pattern: r holds biggest valid value
        l = 0
        r = min(N, M)-1

        while l <= r:
            m = (l+r)//2
            if works(m):
                l = m+1
            else:
                r = m-1

        return r