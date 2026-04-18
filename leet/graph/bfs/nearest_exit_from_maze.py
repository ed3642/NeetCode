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

    def nearestExit(self, maze: list[list[str]], entrance: list[int]) -> int:
        # bfs from starting pos
        # keep track of steps taken until at first exit
        def is_exit(i, j):
            return (
                i == 0 or i == n - 1 or
                j == 0 or j == m - 1
            )
        
        def is_valid(i, j):
            return (
                (i, j) not in visited and
                i >= 0 and i < n and
                j >= 0 and j < m and
                maze[i][j] == '.'
            )

        n = len(maze)
        m = len(maze[0])
        queue = deque([(entrance[0], entrance[1])]) # starting pos
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        visited = set([(entrance[0], entrance[1])])

        steps = 0
        while queue:
            for _ in range(len(queue)):
                i, j = queue.popleft()
                for d_i, d_j in directions:
                    n_i = i + d_i
                    n_j = j + d_j
                    if is_valid(n_i, n_j):
                        if is_exit(n_i, n_j):
                            return steps + 1
                        visited.add((n_i, n_j))
                        queue.append((n_i, n_j))
            steps += 1
        
        return -1

