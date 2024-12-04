# https://leetcode.com/problems/is-graph-bipartite
from collections import deque
from typing import List

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        
        # see if we can color it with 2 colors where no same colored nodes are adjacent
        # place nodes into sets and alternate each bfs level which set
        N = len(graph)
        visited = [False] * N
        NUM_COLORS = 2
        colors = [set() for _ in range(NUM_COLORS)]
        curr_color = 0

        # since its not single component G, make sure we visit all components
        for start_node in range(N):
            q = deque() # start coloring from an arbitrary node
            if not visited[start_node]:
                q.append(start_node)
                visited[start_node] = True
            while q:
                for _ in range(len(q)):
                    node = q.popleft()
                    colors[curr_color].add(node)

                    for nei in graph[node]:
                        if not visited[nei]:
                            q.append(nei)
                            visited[nei] = True
                        if nei in colors[curr_color]:
                            # node and nei are colored the same
                            return False
                curr_color = (curr_color + 1) % NUM_COLORS
        
        return True