# https://leetcode.com/problems/find-minimum-diameter-after-merging-two-trees
from collections import deque
from typing import List

class Solution:
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:

        def bfs(adj_list, visited, source):
            q = deque([(source, 0)])
            visited[source] = True
            max_depth = 0
            deepest_node = 0
            while q:
                for _ in range(len(q)):
                    node, depth = q.popleft()
                    if depth > max_depth:
                        max_depth = depth
                        deepest_node = node
                    for nei in adj_list[node]:
                        if not visited[nei]:
                            q.append((nei, depth + 1))
                            visited[nei] = True
            
            return max_depth, deepest_node

        def calc_diameter(edges):
            # diameter of tree can be found with 2 bfs, first finds furthest from arbitrary (A), second finds furthest from A, that distance is the diameter

            N = len(edges) + 1
            adj_list = [[] for _ in range(N)]
            for _from, _to in edges:
                adj_list[_from].append(_to)
                adj_list[_to].append(_from)
            
            # find A
            visited = [False] * N
            _, A = bfs(adj_list, visited, 0) # first bfs from arbitrary

            visited = [False] * N
            max_depth, _ = bfs(adj_list, visited, A) # second from A
            
            return max_depth

        d1 = calc_diameter(edges1)
        d2 = calc_diameter(edges2)
        longest_path_spanning_both_trees = (d1 + 1) // 2 + (d2 + 1) // 2 + 1

        return max(longest_path_spanning_both_trees, d1, d2)