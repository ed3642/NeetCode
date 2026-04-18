# https://leetcode.com/problems/count-servers-that-communicate
from typing import List

class Solution:
    def countServers(self, grid: List[List[int]]) -> int:

        def dfs(i, j):
            grid[i][j] = 0
            row_nei[i].discard(j)
            col_nei[j].discard(i)
            num_nodes = 1
            while row_nei[i]:
                num_nodes += dfs(i, row_nei[i].pop())
            while col_nei[j]:
                num_nodes += dfs(col_nei[j].pop(), j)
            return num_nodes

        I_BOUNDARY = len(grid)
        J_BOUNDARY = len(grid[0])
        network_size = 0
        row_nei = [set() for _ in range(I_BOUNDARY)]
        col_nei = [set() for _ in range(J_BOUNDARY)]

        for i in range(I_BOUNDARY):
            for j in range(J_BOUNDARY):
                if grid[i][j] == 1:
                    row_nei[i].add(j)
                    col_nei[j].add(i)

        for i in range(I_BOUNDARY):
            for j in range(J_BOUNDARY):
                if grid[i][j] == 1:
                    devices = dfs(i, j)
                    network_size += devices if devices > 1 else 0
        
        return network_size
