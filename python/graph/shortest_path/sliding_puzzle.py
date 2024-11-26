# https://leetcode.com/problems/sliding-puzzle/
from collections import deque
from typing import List

class Solution:
    # NOTE: not mine but example of optimized BFS solution
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        q = deque([])
        final_state = '123450'
        cur_state = ''
        for row in board:
            for v in row:
                cur_state += str(v)
    
        can_move_to = {
            0: [1, 3],
            1: [0, 2, 4],
            2: [1, 5],
            3: [0, 4],
            4: [1, 3, 5],
            5: [2, 4]
        }
        visited = set()
        q.append((cur_state, 0, cur_state.index('0'))) # cur_state, steps, zero_pos
        while q:
            cur_state, steps, zero_pos = q.popleft()
            if cur_state == final_state:
                return steps

            
            for available_space in can_move_to[zero_pos]:
                new_state = list(cur_state)
                new_state[zero_pos], new_state[available_space] = new_state[available_space], new_state[zero_pos]
                new_state = ''.join(new_state)
                if new_state not in visited:
                    visited.add(new_state)
                    q.append((new_state, steps + 1, available_space))
        return -1 


    # BFS, there are a lot of optimizations and different approaches for this problem
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        
        def matrix_to_tuple(matrix):
            return tuple(val for arr in matrix for val in arr)
        
        def tuple_to_matrix(_tuple):
            matrix = [[0] * MAX_J for _ in range(MAX_I)]
            for index, num in enumerate(_tuple):
                i = index // MAX_J
                j = index % MAX_J
                matrix[i][j] = num
            return matrix
        
        def is_in_bounds(i, j):
            return 0 <= i < MAX_I and 0 <= j < MAX_J

        # search for solution with SP
        MAX_I = len(board)
        MAX_J = len(board[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        start = matrix_to_tuple(board)
        goal = (1, 2, 3, 4, 5, 0)

        if start == goal:
            return 0

        q = deque([start])
        visited = set(start)
        depth = 1
        while q:
            for _ in range(len(q)):
                _tuple = q.popleft()
                matrix = tuple_to_matrix(_tuple)

                for i in range(MAX_I):
                    for j in range(MAX_J):
                        if matrix[i][j] == 0:
                            # gen neighbors
                            for d_i, d_j in directions:
                                n_i = i + d_i
                                n_j = j + d_j
                                if is_in_bounds(n_i, n_j):
                                    # make swap
                                    matrix[i][j], matrix[n_i][n_j] = matrix[n_i][n_j], matrix[i][j]
                                    n_tuple = matrix_to_tuple(matrix)
                                    # swap back for next exploration
                                    matrix[i][j], matrix[n_i][n_j] = matrix[n_i][n_j], matrix[i][j]
                                    if n_tuple == goal:
                                        return depth
                                    if n_tuple not in visited:
                                        q.append(n_tuple)
                                        visited.add(n_tuple)
            depth += 1
        
        return -1
    