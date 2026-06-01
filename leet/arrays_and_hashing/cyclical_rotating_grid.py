# https://leetcode.com/problems/cyclically-rotating-a-grid/

from typing import List

class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:

        n = len(grid)
        m = len(grid[0])

        for layer in range(min(n, m) // 2):
            size = 2 * n + 2 * (m - 2)
            order = [0] * size
            placer_i = 0
            # record order
            for i in range(layer, layer + n):
                order[placer_i] = grid[i][layer]
                placer_i += 1
            for j in range(layer + 1, layer + m - 1):
                order[placer_i] = grid[layer + n - 1][j]
                placer_i += 1
            for i in range(layer + n - 1, layer - 1, -1):
                order[placer_i] = grid[i][layer + m - 1]
                placer_i += 1
            for j in range(layer + m - 2, layer, -1):
                order[placer_i] = grid[layer][j]
                placer_i += 1
            shift = k % size
            # do shift
            new_order = [0] * size
            for i in range(size):
                new_order[(i + shift) % size] = order[i]
            # place down order
            placer_i = 0
            for i in range(layer, layer + n):
                grid[i][layer] = new_order[placer_i]
                placer_i += 1
            for j in range(layer + 1, layer + m - 1):
                grid[layer + n - 1][j] = new_order[placer_i]
                placer_i += 1
            for i in range(layer + n - 1, layer - 1, -1):
                grid[i][layer + m - 1] = new_order[placer_i]
                placer_i += 1
            for j in range(layer + m - 2, layer, -1):
                grid[layer][j] = new_order[placer_i]
                placer_i += 1
            n -= 2
            m -= 2

        return grid