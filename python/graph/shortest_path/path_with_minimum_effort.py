from collections import deque
import heapq

class Solution:
    # faster
    def minimumEffortPath(self, heights: list[list[int]]) -> int:
        # djikstras where distance is defined by consecutive cell diff
        # dest is (n, m)

        def is_valid(i, j):
            return (
                i >= 0 and i < n and
                j >= 0 and j < m and
                (i, j) not in visited
            )

        n = len(heights)
        m = len(heights[0])
        heap = [(0, 0, 0)] # effort, i, j

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        efforts = [[float('inf') for _ in range(m)] for _ in range(n)]
        efforts[0][0] = 0
        visited = set()

        while heap:
            effort, i, j = heapq.heappop(heap)
            visited.add((i, j))

            for d_i, d_j in directions:
                n_i = i + d_i
                n_j = j + d_j
                if is_valid(n_i, n_j):
                    candidate_effort = max(effort, abs(heights[n_i][n_j] - heights[i][j]))
                    if candidate_effort < efforts[n_i][n_j]:
                        efforts[n_i][n_j] = candidate_effort
                        heapq.heappush(heap, (candidate_effort, n_i, n_j))

        return efforts[n - 1][m - 1]
    
    # too many edges, djikstra is better
    def minimumEffortPath2(self, heights: list[list[int]]) -> int:
        # SPFA 

        def is_valid(i, j):
            return (
                i >= 0 and i < n and
                j >= 0 and j < m
            )

        n = len(heights)
        m = len(heights[0])
        queue = deque([(0, 0)]) # effort, i, j

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        efforts = [[float('inf') for _ in range(m)] for _ in range(n)]
        efforts[0][0] = 0
        in_queue = set()
        in_queue.add((0, 0))

        while queue:
            i, j = queue.popleft()
            in_queue.remove((i, j))

            for d_i, d_j in directions:
                n_i = i + d_i
                n_j = j + d_j
                if is_valid(n_i, n_j):
                    candidate_effort = max(efforts[i][j], abs(heights[n_i][n_j] - heights[i][j]))
                    if candidate_effort < efforts[n_i][n_j]:
                        efforts[n_i][n_j] = candidate_effort
                        if (n_i, n_j) not in in_queue:
                            queue.append((n_i, n_j))
                            in_queue.add((n_i, n_j))

        return efforts[n - 1][m - 1]