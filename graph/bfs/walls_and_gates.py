from collections import deque

class Solution:
    def wallsAndGates(self, rooms: list[list[int]]) -> None:

        def isValidCoord(i, j):
            return (
                i >= 0 and i < ROWS and
                j >= 0 and j < COLS and
                rooms[i][j] == INF
            )
        
        INF = 2147483647
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        ROWS = len(rooms)
        COLS = len(rooms[0])
        queue = deque()

        # start the queue with the gates
        for i in range(ROWS):
            for j in range(COLS):
                if rooms[i][j] == 0:
                    queue.append((i, j, 1))

        while queue:
            for _ in range(len(queue)):
                i, j, distance = queue.popleft()

                for d_i, d_j in directions:
                    n_i = i + d_i
                    n_j = j + d_j
                    if isValidCoord(n_i, n_j):
                        queue.append((n_i, n_j, distance + 1))
                        rooms[n_i][n_j] = distance