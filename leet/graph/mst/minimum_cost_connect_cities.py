import heapq
from collections import defaultdict

# https://leetcode.com/problems/connecting-cities-with-minimum-cost/description/
class Solution:
    def minimumCost(self, n: int, connections: list[list[int]]) -> int:
        # Prims
        # cities numbered 1..n
        heap = []
        visited = set()
        total_cost = 0
        graph = defaultdict(list)

        # build adj list
        for _from, to, cost in connections:
            graph[_from].append((to, cost))
            graph[to].append((_from, cost))
        
        heap = [(0, 1)] # city 1 with cost 0

        # pick the smallest edge and go to its neighbor city, repeat
        while heap and len(visited) < n:
            cost, curr_node = heapq.heappop(heap)
            if curr_node in visited:
                continue
            
            # process city
            visited.add(curr_node)
            total_cost += cost

            for neighbor_node, neighbor_cost in graph[curr_node]:
                if neighbor_node not in visited:
                    heapq.heappush(heap, (neighbor_cost, neighbor_node))
            
        return total_cost if len(visited) == n else -1