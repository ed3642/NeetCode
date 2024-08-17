class Solution:
    def minFlips(self, grid: list[list[int]]) -> int:
        
        def min_to_make_pal(arr):
            count = 0
            l = 0
            r = len(arr) - 1

            while l < r:
                if arr[l] != arr[r]:
                    count += 1
                l += 1
                r -= 1
            return count

        rows_fix = 0
        cols_fix = 0

        for i in range(len(grid)):
            rows_fix += min_to_make_pal(grid[i])

        for i in range(len(grid[0])):
            col = []
            for j in range(len(grid)):
                col.append(grid[j][i])
            cols_fix += min_to_make_pal(col)

        return min(rows_fix, cols_fix)
    
s = Solution()
