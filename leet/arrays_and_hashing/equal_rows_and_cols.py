from collections import defaultdict

class Solution:
    def equalPairs(self, grid: list[list[int]]) -> int:
        # compare each row with each col

        rows = defaultdict(int)
        cols = defaultdict(int)

        for row in grid:
            rows[tuple(row)] += 1
        
        for col in zip(*grid):
            cols[tuple(col)] += 1

        total_matches = 0
        for row in rows:
            if row in cols:
                total_matches += rows[row] * cols[row]
        
        return total_matches
