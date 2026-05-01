# https://leetcode.com/problems/cut-off-trees-for-golf-event/

from collections import deque
import heapq
from typing import List

class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        
        def astar(i, j, target_i, target_j):
            def heu(i, j):
                # manhattan dist
                return abs(target_i - i) + abs(target_j - j)

            if i == target_i and j == target_j:
                return 0

            h = [(heu(i, j), i, j)]
            distances = [[float('inf')] * M for _ in range(N)] # building the whole grid is faster than a dictionary of a subset of the nodes
            distances[i][j] = 0

            while h:
                _, i, j = heapq.heappop(h)
                if (i, j) == (target_i, target_j):
                    return distances[i][j]

                for di, dj in directions:
                    ni = i + di
                    nj = j + dj
                    if is_in_bounds(ni, nj) and forest[ni][nj] > 0:
                        cand_dist = distances[i][j] + 1
                        if cand_dist < distances[ni][nj]:
                            f = heu(ni, nj) + cand_dist
                            heapq.heappush(h, (f, ni, nj))
                            distances[ni][nj] = cand_dist
            
            return -1 # no path found
        
        def is_in_bounds(i, j):
            return 0 <= i < N and 0 <= j < M

        N = len(forest)
        M = len(forest[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        order = [(0, 0, 0)] # starting node

        for i in range(N):
            for j in range(M):
                if forest[i][j] > 1:
                    order.append((forest[i][j], i, j))
        
        order.sort(key=lambda x: x[0])

        total_dist = 0
        for i in range(1, len(order)):
            dist = astar(order[i][1], order[i][2], order[i - 1][1], order[i - 1][2])
            if dist == -1:
                return -1
            total_dist += dist

        return total_dist

    def cutOffTree(self, forest: List[List[int]]) -> int:
        
        def bfs(i, j, target_i, target_j):
            if i == target_i and j == target_j:
                return 0

            q = deque([(i, j)])
            visited = set([(i, j)])

            dist = 0

            while q:
                dist += 1
                for _ in range(len(q)):
                    i, j = q.popleft()

                    for di, dj in directions:
                        ni = i + di
                        nj = j + dj
                        if is_in_bounds(ni, nj) and forest[ni][nj] > 0 and (ni, nj) not in visited:
                            if (ni, nj) == (target_i, target_j):
                                return dist
                            visited.add((ni, nj))
                            q.append((ni, nj))
            
            return -1 # no path found
        
        def is_in_bounds(i, j):
            return 0 <= i < N and 0 <= j < M

        N = len(forest)
        M = len(forest[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        order = [(0, 0, 0)] # starting node

        for i in range(N):
            for j in range(M):
                if forest[i][j] > 1:
                    order.append((forest[i][j], i, j))
        
        order.sort(key=lambda x: x[0])

        total_dist = 0
        for i in range(1, len(order)):
            dist = bfs(order[i][1], order[i][2], order[i - 1][1], order[i - 1][2])
            if dist == -1:
                return -1
            total_dist += dist

        return total_dist

    def cutOffTree(self, forest: List[List[int]]) -> int:
        
        def astar(i, j, i_final, j_final):
            if i == i_final and j == j_final:
                return 0
            
            heap = [(0, 0, i, j)]
            visited = [[False] * J_BOUND for _ in range(I_BOUND)]
            visited[i][j] = True

            while heap:
                _, steps, i, j = heapq.heappop(heap)

                for d_i, d_j in directions:
                    n_i = i + d_i
                    n_j = j + d_j

                    if n_i == i_final and n_j == j_final:
                        return steps + 1
                    if is_in_bounds(n_i, n_j) and forest[n_i][n_j] > 0 and not visited[n_i][n_j]:
                        visited[n_i][n_j] = True
                        f = heuristic(n_i, n_j, i_final, j_final) + steps # g => steps
                        heapq.heappush(heap, (f, steps + 1, n_i, n_j))
            return 0 # shouldnt happen
        
        def heuristic(i, j, i_final, j_final):
            # manhattan dist
            return abs(i - i_final) + abs(j - j_final)

        def dfs(i, j, visited):
            if forest[i][j] > 1:
                trees.append((forest[i][j], i, j))

            for d_i, d_j in directions:
                n_i = i + d_i
                n_j = j + d_j
                if is_in_bounds(n_i, n_j) and forest[n_i][n_j] > 0 and not visited[n_i][n_j]:
                    visited[n_i][n_j] = True
                    dfs(n_i, n_j, visited)


        def is_in_bounds(i, j):
            return 0 <= i < I_BOUND and 0 <= j < J_BOUND

        I_BOUND = len(forest)
        J_BOUND = len(forest[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        steps = 0
        trees = []

        # check if can reach all trees
        total_trees = 0
        for i in range(I_BOUND):
            for j in range(J_BOUND):
                if forest[i][j] > 1:
                    total_trees += 1
        
        dfs_visited = [[False] * J_BOUND for _ in range(I_BOUND)]
        dfs_visited[0][0] = True
        dfs(0, 0, dfs_visited)

        if total_trees != len(trees):
            return -1

        # count steps needed
        trees.sort(key=lambda x: x[0])
        prev_i = 0
        prev_j = 0
        for height, i, j in trees:
            steps += astar(i, j, prev_i, prev_j)
            prev_i = i
            prev_j = j

        return steps

    def cutOffTree(self, forest: List[List[int]]) -> int:
        
        def bfs(i, j, i_final, j_final):
            if i == i_final and j == j_final:
                return 0
            
            q = deque([(i, j)])
            visited = [[False] * J_BOUND for _ in range(I_BOUND)]
            visited[i][j] = True
            steps = 1

            while q:
                for _ in range(len(q)):
                    i, j = q.popleft()

                    for d_i, d_j in directions:
                        n_i = i + d_i
                        n_j = j + d_j

                        if n_i == i_final and n_j == j_final:
                            return steps
                        if is_in_bounds(n_i, n_j) and forest[n_i][n_j] > 0 and not visited[n_i][n_j]:
                            visited[n_i][n_j] = True
                            q.append((n_i, n_j))
                steps += 1
            return 0 # shouldnt happen

        def dfs(i, j, visited):
            if forest[i][j] > 1:
                trees.append((forest[i][j], i, j))

            for d_i, d_j in directions:
                n_i = i + d_i
                n_j = j + d_j
                if is_in_bounds(n_i, n_j) and forest[n_i][n_j] > 0 and not visited[n_i][n_j]:
                    visited[n_i][n_j] = True
                    dfs(n_i, n_j, visited)


        def is_in_bounds(i, j):
            return 0 <= i < I_BOUND and 0 <= j < J_BOUND

        I_BOUND = len(forest)
        J_BOUND = len(forest[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        steps = 0
        trees = []

        # check if can reach all trees
        total_trees = 0
        for i in range(I_BOUND):
            for j in range(J_BOUND):
                if forest[i][j] > 1:
                    total_trees += 1
        
        dfs_visited = [[False] * J_BOUND for _ in range(I_BOUND)]
        dfs_visited[0][0] = True
        dfs(0, 0, dfs_visited)

        if total_trees != len(trees):
            return -1

        # count steps needed
        trees.sort(key=lambda x: x[0])
        prev_i = 0
        prev_j = 0
        for height, i, j in trees:
            steps += bfs(i, j, prev_i, prev_j)
            prev_i = i
            prev_j = j

        return steps
