from collections import defaultdict


class neighborSum:

    def __init__(self, grid: list[list[int]]):
        self.value_pos = defaultdict(tuple)
        self.grid = grid.copy()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                self.value_pos[grid[i][j]] = (i, j)

    def is_valid_square(self, i, j):
        return (
            i >= 0 and i < len(self.grid) and
            j >= 0 and j < len(self.grid[0])
        )

    def adjacentSum(self, value: int) -> int:
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        i, j = self.value_pos[value]
        _sum = 0
        for d_i, d_j in directions:
            n_i = i + d_i
            n_j = j + d_j
            if self.is_valid_square(n_i, n_j):
                _sum += self.grid[n_i][n_j]
        return _sum

    def diagonalSum(self, value: int) -> int:
        directions = [(-1, -1), (1, -1), (1, 1), (-1, 1)]
        i, j = self.value_pos[value]
        _sum = 0
        for d_i, d_j in directions:
            n_i = i + d_i
            n_j = j + d_j
            if self.is_valid_square(n_i, n_j):
                _sum += self.grid[n_i][n_j]
        return _sum


# Your neighborSum object will be instantiated and called as such:
# obj = neighborSum(grid)
# param_1 = obj.adjacentSum(value)
# param_2 = obj.diagonalSum(value)