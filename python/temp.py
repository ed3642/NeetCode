from collections import deque
from typing import List
import heapq

class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        # NOTE: interestingly, we dont need a visited set for this djisktras since there are no edges that go further away from the target in this problem and its a DAG and target is always guarantee reachable
        # Djikstras from node _from after each query to update SP

        def djikstras(start_node):
            heap = [(dist[start_node], start_node)]
            while heap:
                curr_dist, node = heapq.heappop(heap)

                for nei in adj_list[node]:
                        cand_dist = curr_dist + 1
                        if cand_dist < dist[nei]:
                            dist[nei] = cand_dist
                            heapq.heappush(heap, (cand_dist, nei))
                        if nei == n - 1:
                            return

        adj_list = [[node + 1] for node in range(n)]
        adj_list[n - 1].clear() # this points to nothing
        dist = [i for i in range(n)]
        res = []

        for _from, _to in queries:
            adj_list[_from].append(_to)
            
            djikstras(_from) # update SPs

            res.append(dist[n - 1])
        
        return res
    
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        
        # BFS from node _from after each query to update SP

        def bfs(start_node):
            q = deque([start_node])
            while q:
                for _ in range(len(q)):
                    node = q.popleft()

                    for nei in adj_list[node]:
                            cand_dist = dist[node] + 1
                            if cand_dist < dist[nei]:
                                dist[nei] = cand_dist
                                q.append(nei)
                            if nei == n - 1:
                                return

        adj_list = [[node + 1] for node in range(n)]
        adj_list[n - 1].clear() # this points to nothing
        dist = [i for i in range(n)]
        res = []

        for _from, _to in queries:
            adj_list[_from].append(_to)
            
            bfs(_from) # update SPs

            res.append(dist[n - 1])
        
        return res
    