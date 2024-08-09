class Solution:
    def numMagicSquaresInside(self, grid: list[list[int]]) -> int:
        # 3x3 must have nums in [1,9]

        def is_magic_square(i, j):
            needed = set([i for i in range(1, 10)])
            for it in range(3):
                for it2 in range(3):
                    if 0 < grid[i + it][j + it2] < 10:
                        if grid[i + it][j + it2] in needed:
                            needed.remove(grid[i + it][j + it2])
                    else:
                        return False
            if len(needed) != 0:
                return False
            # rows
            row_sum = grid[i][j] + grid[i][j + 1] + grid[i][j + 2]
            for it in range(1, 3):
                _sum = 0
                for it2 in range(3):
                    _sum += grid[i + it][j + it2]
                if _sum != row_sum:
                    return False
            # cols
            col_sum = grid[i][j] + grid[i + 1][j] + grid[i + 2][j]
            if row_sum != col_sum:
                return False
            for it in range(1, 3):
                _sum = 0
                for it2 in range(3):
                    _sum += grid[i + it2][j + it]
                if _sum != col_sum:
                    return False
            # diagonals
            diag1 = grid[i][j] + grid[i + 1][j + 1] + grid[i + 2][j + 2]
            if row_sum != diag1:
                return False
            diag2 = grid[i + 2][j] + grid[i + 1][j + 1] + grid[i][j + 2]
            if diag1 != diag2:
                return False
            # all clear
            return True

        count = 0
        n = len(grid)
        m = len(grid[0])
        
        for i in range(n - 2):
            for j in range(m - 2):
                if is_magic_square(i, j):
                    count += 1

        return count