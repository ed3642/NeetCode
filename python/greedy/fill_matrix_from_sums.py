class Solution:
    # take the min from row[i] and col[j] and place it. then subtract what we just placed
    def restoreMatrix(self, rowSum: list[int], colSum: list[int]) -> list[list[int]]:
        
        n = len(rowSum)
        m = len(colSum)
        res = [[0 for _ in range(m)] for _ in range(n)]

        for i in range(n):
            # optimization: once our row is 0, we can no longer use it
            if rowSum[i] == 0:
                continue
            for j in range(m):
                if colSum[j] == 0:
                    continue
                min_option = min(rowSum[i], colSum[j])
                res[i][j] = min_option
                # update sums
                rowSum[i] -= min_option
                colSum[j] -= min_option
                if rowSum[i] == 0:
                    break
        
        return res