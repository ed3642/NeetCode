# https://leetcode.com/problems/minimum-cost-to-convert-string-i
from collections import defaultdict
import heapq

class Solution:
    def minimumCost(self, source: str, target: str, original: list[str], changed: list[str], cost: list[int]) -> int:

        def djikstra(root):
            heap = [(0, root)]
            visited = set([root])
            distances = defaultdict(lambda: float('inf'))
            distances[root] = 0

            while heap:
                dist, node = heapq.heappop(heap)
                visited.add(node)

                # record what we need
                if (root, node) in min_cost and dist < min_cost[(root, node)]:
                    min_cost[(root, node)] = dist

                for neighbor_dist, neighbor_node in adj_list[node]:
                    if neighbor_node not in visited:
                        candidate_dist = dist + neighbor_dist
                        if candidate_dist < distances[neighbor_node]:
                            distances[neighbor_node] = candidate_dist
                            heapq.heappush(heap, (candidate_dist, neighbor_node))
            
        n = len(source)
        min_cost = defaultdict(int)
        total_cost = 0
        adj_list = defaultdict(list)

        # see what we need to calculate
        for i in range(n):
            if source[i] != target[i] and (source[i], target[i]) not in min_cost:
                min_cost[(source[i], target[i])] = float('inf')
        
        # build adj_list
        for i in range(len(cost)):
            _from = original[i]
            adj_list[_from].append((cost[i], changed[i]))
        
        # calculate the min_cost for all needed mappings
        for _from, _to in min_cost.keys():
            if min_cost[(_from, _to)] == float('inf'):
                djikstra(_from)
            # if this min_cost still equals, inf then we cant make this transformation
            if min_cost[(_from, _to)] == float('inf'):
                return -1

        # sum up the costs
        for i in range(n):
            if source[i] != target[i]:
                total_cost += min_cost[(source[i], target[i])]

        return total_cost