# https://leetcode.com/problems/n-queens-ii

class Solution:
    # uses a grid to keep track of valid squares, is slower than using sets
    def totalNQueens(self, n: int) -> int:
        # famous backtracking problem
        # need place_queen, remove_queen, is_valid_square
        grid = [[0 for _ in range(n)] for _ in range(n)]

        def is_on_board(i, j):
            return (i >= 0 and i < n and
                    j >= 0 and j < n)

        def is_valid_square(i, j):
            return (grid[i][j] == 0)
            
        def move_queen(i, j, delta): # +1 delta to add, -1 to remove 
            # row and col
            for it in range(n):
                grid[i][it] += delta
                grid[it][j] += delta
            # diagonals
            directions = [(1, 1), (-1, 1), (1, -1), (-1, -1)]
            for dx, dy in directions:
                it = 1
                curr_i = i + it * dx
                curr_j = j + it * dy
                while is_on_board(curr_i, curr_j):
                    grid[curr_i][curr_j] += delta
                    curr_i = i + it * dx
                    curr_j = j + it * dy
                    it += 1

        def backtrack(i): # <row, count>
            for j in range(n):
                if is_valid_square(i, j):
                    move_queen(i, j, 1) # add queen
                    if i == n - 1: # filled all the rows
                        self.solution_count += 1
                    else:
                        backtrack(i + 1)
                    move_queen(i, j, -1) # remove queen
        
        self.solution_count = 0
        backtrack(0)
        return self.solution_count

    # uses sets to keep track of valid squares, is faster
    def totalNQueens(self, n):
        def backtrack(row, diagonals, anti_diagonals, cols):
            # Base case - N queens have been placed
            if row == n:
                return 1

            solutions = 0
            for col in range(n):
                curr_diagonal = row - col
                curr_anti_diagonal = row + col
                # If the queen is not placeable
                if (col in cols 
                      or curr_diagonal in diagonals 
                      or curr_anti_diagonal in anti_diagonals):
                    continue

                # "Add" the queen to the board
                cols.add(col)
                diagonals.add(curr_diagonal)
                anti_diagonals.add(curr_anti_diagonal)

                # Move on to the next row with the updated board state
                solutions += backtrack(row + 1, diagonals, anti_diagonals, cols)

                # "Remove" the queen from the board since we have already
                # explored all valid paths using the above function call
                cols.remove(col)
                diagonals.remove(curr_diagonal)
                anti_diagonals.remove(curr_anti_diagonal)

            return solutions

        return backtrack(0, set(), set(), set())