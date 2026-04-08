# https://leetcode.com/problems/game-of-life

from typing import List

class Solution:

    # O(1) space
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def is_in_bounds(i, j):
            return 0 <= i < I_BOUND and 0 <= j < J_BOUND 
        
        I_BOUND = len(board)
        J_BOUND = len(board[0])
        # less than or eq 0 => dead
        DEAD = 0
        WILL_BORN = -1
        # more than 0 => alive
        ALIVE = 1
        WILL_DIE = 2
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]

        for i in range(I_BOUND):
            for j in range(J_BOUND):
                neis = 0
                for d_i, d_j in directions:
                    n_i = i + d_i
                    n_j = j + d_j
                    if is_in_bounds(n_i, n_j) and board[n_i][n_j] > 0:
                        neis += 1
                if board[i][j] > 0:
                    if neis < 2 or neis > 3:
                        board[i][j] = WILL_DIE
                else: # dead
                    if neis == 3:
                        board[i][j] = WILL_BORN

        for i in range(I_BOUND):
            for j in range(J_BOUND):
                if board[i][j] == WILL_BORN:
                    board[i][j] = 1
                elif board[i][j] == WILL_DIE:
                    board[i][j] = 0

    # O(k) space
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def is_in_bounds(i, j):
            return 0 <= i < I_BOUND and 0 <= j < J_BOUND 
        
        I_BOUND = len(board)
        J_BOUND = len(board[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]
        updates = {}

        for i in range(I_BOUND):
            for j in range(J_BOUND):
                neis = 0
                for d_i, d_j in directions:
                    n_i = i + d_i
                    n_j = j + d_j
                    if is_in_bounds(n_i, n_j) and board[n_i][n_j] == 1:
                        neis += 1
                if board[i][j] == 1: # alive
                    if neis < 2 or neis > 3:
                        updates[(i, j)] = 0
                else: # dead
                    if neis == 3:
                        updates[(i, j)] = 1

        for (i, j), state in updates.items():
            board[i][j] = state