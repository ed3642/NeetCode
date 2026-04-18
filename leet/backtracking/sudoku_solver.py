from collections import deque 

class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def is_valid(i, j, num):
            valid_row = num not in rows[i]
            valid_col = num not in cols[j]
            square = squares[get_square_index(i, j)]
            valid_square = num not in square
            return (valid_row and valid_col and valid_square)

        def get_square_index(i, j):
            # Calculate the index of the 3x3 square
            square_index = (i // 3) * 3 + (j // 3)
            return square_index

        def backtrack():
            if not missing_vals:
                return True
            
            i, j = missing_vals.pop()

            for num in range(1, 10):
                num = str(num)
                if is_valid(i, j, num):
                    # place the number
                    rows[i].add(num)
                    cols[j].add(num)
                    squares[get_square_index(i, j)].add(num)
                    board[i][j] = str(num)

                    if backtrack():
                        return True
                    # remove the number
                    board[i][j] = '.'
                    rows[i].remove(num)
                    cols[j].remove(num)
                    squares[get_square_index(i, j)].remove(num)
            
            # add it back after we have tried all numbers from 1-9 for this cell
            missing_vals.append((i, j))
            return False

        n = len(board)
        rows = [set() for _ in range(n)]
        cols = [set() for _ in range(n)]
        squares = [set() for _ in range(n)]
        missing_vals = []

        # fill in the sets
        for i in range(n):
            for j in range(n):
                if board[i][j] == '.':
                    missing_vals.append((i, j))
                else:
                    rows[i].add(board[i][j])
                    cols[j].add(board[i][j])
                    squares[get_square_index(i, j)].add(board[i][j])

        backtrack()