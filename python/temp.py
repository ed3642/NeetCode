# https://leetcode.com/problems/nearest-exit-from-entrance-in-maze
from collections import deque
from typing import List

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        
        def is_in_maze(i, j):
            return (i >= 0 and i < MAX_I and
                    j >= 0 and j < MAX_J)

        MAX_I = len(maze)
        MAX_J = len(maze[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        entrance_i, entrance_j = entrance 
        q = deque([(entrance_i, entrance_j)]) # dist, i, j

        dist = 0
        while q:
            for _ in range(len(q)):
                i, j = q.popleft()

                for d_i, d_j in directions:
                    n_i = i + d_i
                    n_j = j + d_j
                    # escaped
                    in_maze = False
                    if is_in_maze(n_i, n_j): 
                        in_maze = True
                    if not in_maze and not (i == entrance_i and j == entrance_j):
                        return dist
                    if in_maze and maze[n_i][n_j] == '.':
                        maze[n_i][n_j] = '+'
                        q.append((n_i, n_j))
            dist += 1
        
        return -1
