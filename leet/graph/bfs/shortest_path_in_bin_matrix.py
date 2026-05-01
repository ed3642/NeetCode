# https://leetcode.com/problems/shortest-path-in-binary-matrix
from collections import defaultdict, deque
import heapq
from typing import List

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        # astar is basically dijakstras with a heuristic func attached
        # astar heuristic must be admissible and consistent
        # c is the true distance to a node
        # h(a) <= c(a) admissible
        # h(a) <= c(a to b) + h(b) consistent

        def is_in_bounds(i, j):
            return 0 <= i < N and 0 <= j < N
        
        def heu(i, j):
            # octile distance, admissible and consistent in 8 directional grid
            target_i = N - 1
            target_j = N - 1
            return max(target_i - i, target_j - j)
        
        N = len(grid)
        if grid[N - 1][N - 1] == 1 or grid[0][0] == 1:
            return -1

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (-1, 1), (1, -1)]
        distances = [[float('inf')] * N for _ in range(N)]
        distances[0][0] = 1

        h = [(heu(0, 0), 0, 0)]

        while h:
            f, i, j = heapq.heappop(h)

            if i == N - 1 and j == N - 1:
                return distances[N - 1][N - 1]

            for di, dj in directions:
                ni = i + di
                nj = j + dj
                if is_in_bounds(ni, nj) and grid[ni][nj] == 0:
                    cand_dist = distances[i][j] + 1
                    if cand_dist < distances[ni][nj]:
                        f = heu(ni, nj) + cand_dist # f = h + g
                        heapq.heappush(h, (f, ni, nj))
                        distances[ni][nj] = cand_dist

        return -1

    # we can do A* since we know the start and end nodes
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # f = g + h

        def is_valid(i, j):
            return (i >= 0 and i < MAX_I and 
                    j >= 0 and j < MAX_J and
                    grid[i][j] == 0)

        # Chebyshev dist
        # NOTE: manhattan or euclidian dist are not suitable for 8-way neighbors
        def heuristic(i, j): 
            #return abs((MAX_I - 1) - i) + abs((MAX_J - 1) - j)
            #return (abs((MAX_I - 1) - i) ** 2 + abs((MAX_J - 1) - j) ** 2) ** 0.5
            return max(abs((MAX_I - 1) - i), abs((MAX_J - 1) - j))

        if grid[0][0] == 1:
            return -1
        
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        MAX_I = len(grid)
        MAX_J = len(grid[0])

        distances = defaultdict(lambda: float('inf'))
        distances[(0, 0)] = 1 # we count the starting cell as a step as well
        start_prio = distances[(0, 0)] + heuristic(0, 0)
        heap = [(start_prio, 0, 0)] # <prio, i, j>

        while heap:
            prio, i, j = heapq.heappop(heap)

            grid[i][j] == 1 # mark visited

            if i == MAX_I - 1 and j == MAX_J - 1:
                return distances[(i, j)]

            for d_i, d_j in directions:
                n_i = i + d_i
                n_j = j + d_j
                if is_valid(n_i, n_j):
                    cand_g = distances[(i, j)] + 1
                    if cand_g < distances[(n_i, n_j)]:
                        distances[(n_i, n_j)] = cand_g
                        f = cand_g + heuristic(n_i, n_j)
                        heapq.heappush(heap, (f, n_i, n_j))
        
        return -1
    
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        def is_in_bounds(i, j):
            return 0 <= i < N and 0 <= j < N
        
        N = len(grid)
        if grid[N - 1][N - 1] == 1 or grid[0][0] == 1:
            return -1

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (-1, 1), (1, -1)]

        q = deque([(0, 0)])
        depth = 0

        while q:
            depth += 1
            for _ in range(len(q)):
                i, j = q.popleft()

                if i == N - 1 and j == N - 1:
                    return depth

                for di, dj in directions:
                    ni = i + di
                    nj = j + dj
                    if is_in_bounds(ni, nj) and grid[ni][nj] == 0:
                        q.append((ni, nj))
                        grid[ni][nj] = 1

        return -1
    
    # bfs is good but astar is better
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        def is_valid(i, j):
            return (i >= 0 and i < MAX_I and 
                    j >= 0 and j < MAX_J and
                    grid[i][j] == 0)

        if grid[0][0] == 1:
            return -1

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        MAX_I = len(grid)
        MAX_J = len(grid[0])
        q = deque([(0, 0)])

        dist = 1
        while q:
            for _ in range(len(q)):
                i, j = q.popleft()

                if i == MAX_I - 1 and j == MAX_J - 1:
                    return dist

                for d_i, d_j in directions:
                    n_i = i + d_i
                    n_j = j + d_j
                    if is_valid(n_i, n_j):
                        grid[n_i][n_j] = 1
                        q.append((n_i, n_j))
            dist += 1

        return -1

    # not the best
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        def is_in_bounds(i, j):
            return 0 <= i < N and 0 <= j < N
        
        N = len(grid)
        if grid[N - 1][N - 1] == 1 or grid[0][0] == 1:
            return -1

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (-1, 1), (1, -1)]
        distances = [[float('inf')] * N for _ in range(N)]
        distances[0][0] = 1

        q = deque([(0, 0)])

        while q:
            for _ in range(len(q)):
                i, j = q.popleft()

                for d_i, d_j in directions:
                    n_i = i + d_i
                    n_j = j + d_j
                    if is_in_bounds(n_i, n_j):
                        cand_dist = distances[i][j] + 1
                        if grid[n_i][n_j] == 0 and distances[n_i][n_j] == float('inf'):
                            q.append((n_i, n_j))
                        if distances[n_i][n_j] > cand_dist:
                            distances[n_i][n_j] = cand_dist

        return distances[N - 1][N - 1] if distances[N - 1][N - 1] != float('inf') else -1