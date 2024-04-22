import heapq
from collections import defaultdict
# TODO: some test still fail
class Solution:
    def minimumCost(self, n: int, connections: list[list[int]]) -> int:
        # Prims
        # cities numbered 1..n
        heap = []
        connetions_count = 0 # stop at n - 1
        visited = [False] * (n + 1)
        total_cost = 0
        edges = defaultdict(list)
        starting_city = connections[0][0]

        # choose arbitrary node and heapify its edges
        for connection in connections:
            _from, to, cost = connection
            edges[_from].append((to, cost)) # for easy neighbor access later
            edges[to].append((_from, cost))
            if _from == starting_city or to == starting_city:
                heap.append((cost, _from, to))
        heapq.heapify(heap)

        # pick the smallest edge and go to its "to" city, repeat
        while heap and connetions_count < n - 1:
            cost, _from, to = heapq.heappop(heap)
            if visited[to]: continue
            visited[_from] = True
            total_cost += cost
            connetions_count += 1

            if not visited[to]:
                visited[to] = True
                for edge in edges[to]:
                    edge_to, edge_cost = edge
                    if not visited[edge_to]:
                        heapq.heappush(heap, (edge_cost, to, edge_to))
        
        return total_cost if connetions_count == n - 1 else -1
