class Solution:
    def numberOfSubmatrices(self, grid: list[list[str]]) -> int:
        # this solution seems pretty convoluted
        # last col counts
        x_counts = [0] * len(grid[0])
        y_counts = [0] * len(grid[0])
        xs = 0
        ys = 0

        count = 0
        for i in range(len(grid)):
            next_xs = [0] * len(grid[0])
            next_ys = [0] * len(grid[0])
            for j in range(len(grid[0])):
                if grid[i][j] == 'X':
                    xs += 1
                elif grid[i][j] == 'Y':
                    ys += 1
                next_xs[j] = x_counts[j] + xs
                next_ys[j] = y_counts[j] + ys
                if (xs + x_counts[j]) == (ys + y_counts[j]) and (xs + x_counts[j]) > 0:
                    count += 1
            xs = 0
            ys = 0
            x_counts = next_xs
            y_counts = next_ys
            
        
        return count