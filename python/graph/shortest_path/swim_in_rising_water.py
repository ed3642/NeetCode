import heapq

class Solution:
    # https://leetcode.com/problems/swim-in-rising-water/
    def swimInWater(self, grid: list[list[int]]) -> int:
        # djikstra, distance is how long you have to wait

        def is_valid(i, j):
            return (
                i >= 0 and i < MAX_I and
                j >= 0 and j < MAX_J and
                (i, j) not in visited
            )

        MAX_I = len(grid)
        MAX_J = len(grid[0])
        heap = [(0, 0, 0)] # time_to_wait, i, j, t
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visited = set()
        distances = [[float('inf')] * MAX_J for _ in range(MAX_I)]
        distances[0][0] = 0
        max_dist = grid[0][0] # nodes have to be atleast this


        while heap:
            dist, i, j = heapq.heappop(heap)
            visited.add((i, j))
            max_dist = max(max_dist, dist)

            for d_i, d_j in directions:
                n_i = i + d_i
                n_j = j + d_j
                if is_valid(n_i, n_j):
                    candidate_dist = max(grid[n_i][n_j], max_dist)
                    if candidate_dist < distances[n_i][n_j]:
                        distances[n_i][n_j] = candidate_dist
                        heapq.heappush(heap, (candidate_dist, n_i, n_j))

        return distances[MAX_I - 1][MAX_J - 1]
                    