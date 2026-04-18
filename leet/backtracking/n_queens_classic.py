# https://leetcode.com/problems/n-queens
from typing import List

class Solution:
    # O(n!)
    def solveNQueens(self, n: int) -> List[List[str]]:
        # place a queen row by row
        
        def bt(cols, diag_down, diag_up, queens: list):
            if len(queens) == n:
                queen_placements.append(queens.copy())
                return
            
            i = len(queens)
            for j in range(n):
                if j in cols:
                    continue
                diag_down_key = get_diag_down_key(i, j)
                if diag_down_key in diag_down:
                    continue
                diag_up_key = get_diag_up_key(i, j) 
                if diag_up_key in diag_up:
                    continue

                queens.append((i, j))
                #rows.add(i)
                cols.add(j)
                diag_down.add(diag_down_key)
                diag_up.add(diag_up_key)
                #bt(rows, cols, diag_down, diag_up, queens)
                bt(cols, diag_down, diag_up, queens)
                queens.pop()
                #rows.remove(i)
                cols.remove(j)
                diag_down.remove(diag_down_key)
                diag_up.remove(diag_up_key)

        def get_diag_down_key(i, j):
            return i - j
        
        def get_diag_up_key(i, j):
            return i + j

        queen_placements = []
        res = []
        #bt(set(), set(), set(), set(), [])
        bt(set(), set(), set(), [])

        for positions in queen_placements:
            board = []
            positions = list(positions)
            positions.sort(key=lambda x: x[0])
            for i, j in positions:
                left = j
                right = n - left - 1
                board.append('.' * left + 'Q' + '.' * right)
            res.append(board)
            
        return res
    