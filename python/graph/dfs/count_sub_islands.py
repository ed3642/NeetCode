# https://leetcode.com/problems/count-sub-islands/description/
class Solution:
    def countSubIslands(self, grid1: list[list[int]], grid2: list[list[int]]) -> int:
        
        # explore islands in grid2, disqualify if missing cell in grid1

        def dfs(i, j):
            all_valid = True
            for d_i, d_j in directions:
                n_i = i + d_i
                n_j = j + d_j
                if is_valid(n_i, n_j):
                    grid2[n_i][n_j] = 0
                    all_valid = dfs(n_i, n_j) and all_valid
            return all_valid if grid1[i][j] == 1 else False

        def is_valid(i, j):
            return (
                i >= 0 and i < MAX_I and
                j >= 0 and j < MAX_J and
                grid2[i][j] == 1
            )

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        MAX_I = len(grid1)
        MAX_J = len(grid1[0])
        count = 0

        for i in range(MAX_I):
            for j in range(MAX_J):
                if is_valid(i, j) and grid1[i][j] == 1:
                    grid2[i][j] = 0
                    if dfs(i, j):
                        count += 1
        
        return count