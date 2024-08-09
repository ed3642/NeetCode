# https://leetcode.com/problems/spiral-matrix-iii
class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> list[list[int]]:
        
        def in_grid(i, j):
            return (
                i < rows and i >= 0 and
                j < cols and j >= 0
            )
        
        magnitude = 1
        turns = 0
        cells_left = rows * cols
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)] # order of directions
        curr_dir = 0
        coords = []
        i = rStart
        j = cStart

        while cells_left > 0:
            # traverse vector
            d_i, d_j = directions[curr_dir]
            for _ in range(magnitude):
                if in_grid(i, j):
                    cells_left -= 1
                    coords.append([i, j])
                i += d_i
                j += d_j
            # update direction
            curr_dir = (curr_dir + 1) % 4
            # check for magnitude increase
            turns = (turns + 1) % 2
            if turns == 0: # made 2 turns
                magnitude += 1

        return coords

