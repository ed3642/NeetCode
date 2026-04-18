class Solution:
    def coloredCells(self, n: int) -> int:
        
        # n_i = n_i-1 + 4 * (i - 1)
        # can also get seq formula with further examination

        if n == 1:
            return 1
        
        prev = 1
        curr = 1
        for i in range(2, n + 1):
            curr = prev + 4 * (i - 1)
            prev = curr
        
        return curr
