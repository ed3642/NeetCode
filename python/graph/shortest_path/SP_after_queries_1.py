from collections import deque
import heapq
# https://leetcode.com/problems/shortest-distance-after-road-addition-queries-i/

class Solution:
    # O(q n^2)
    def shortestDistanceAfterQueries(self, n: int, queries: list[list[int]]) -> list[int]:
        # BFS, update the shortest path to only the nodes affected, not the entire graph

        def bfs(_to):
            q = deque([_to]) # start from the node we just found a shorter path to
            visited = set()
            while q:
                node = q.popleft()
                visited.add(node)

                for nei_node in adj[node]:
                    if nei_node not in visited:
                        candidate_dist = d[node] + 1
                        if candidate_dist < d[nei_node]:
                            d[nei_node] = candidate_dist
                            q.append(nei_node)

        d = [i for i in range(n)] # distances to node 0
        adj = [[i + 1] for i in range(n - 1)]
        adj.append([]) # n - 1 goes nowhere
        shortest = []

        for _from, _to in queries:
            adj[_from].append(_to)

            candidate_dist = d[_from] + 1
            if candidate_dist < d[_to]:
                d[_to] = candidate_dist

                # propagate update only to affected nodes
                bfs(_to)

            shortest.append(d[n - 1])
        
        return shortest

    # O(q n^2 logn)
    def shortestDistanceAfterQueries(self, n: int, queries: list[list[int]]) -> list[int]:

        # run djisktras every query
        # this works but is not that efficient, BFS will do since all edges are weight 1

        def djikstras(node):
            heap = [(0, node)]
            visited = set()
            distances = [float('inf')] * n

            while heap:
                dist, node = heapq.heappop(heap)
                visited.add(node)

                if node == n - 1:
                    return dist

                for nei_node in adj_list[node]:
                    if nei_node not in visited:
                        cand_dist = dist + 1 # +1 to accumulate the distance
                        if cand_dist < distances[nei_node]:
                            distances[nei_node] = cand_dist
                            heapq.heappush(heap, (cand_dist, nei_node))
            return distances[n - 1]

        adj_list = [[i + 1] for i in range(n - 1)]
        adj_list.append([]) # the last node points nowhere

        times = []
        for _from, _to in queries:
            if _to > adj_list[_from][0]:
                adj_list[_from].append(_to)
                times.append(djikstras(0))
        
        return times
    
s = Solution()
print(s.shortestDistanceAfterQueries(n = 6, queries = [[1,4],[0,2]]))