import heapq
from collections import deque

class Solution:
    # NOTE: nodes go from 1..n
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        # dijkstra

        # make adjacency list
        adj_list = [[] for _ in range(n + 1)]
        for edge in times:
            v_from, v_to, distance = edge
            adj_list[v_from].append((distance, v_to))
        
        # initialize
        visited = [False] * (n + 1)
        distances = [float('inf')] * (n + 1)

        heap = [(0, k)]
        distances[k] = 0
        distances[0] = 0 # this node does not exist since we start from 1

        # greedy explore 
        while heap:
            dist, node = heapq.heappop(heap)
            visited[node] = True

            for neighbor in adj_list[node]:
                neighbor_dist, neighbor_node = neighbor
                if not visited[neighbor_node]:
                    candidate_distance = dist + neighbor_dist
                    if distances[neighbor_node] > candidate_distance:
                        distances[neighbor_node] = candidate_distance
                        heapq.heappush(heap, (distances[neighbor_node], neighbor_node))

        max_distance = max(distances)
        
        return -1 if max_distance == float('inf') else max_distance
    
    def networkDelayTime2(self, times: list[list[int]], n: int, k: int) -> int:
        # SFPA with in_queue improvement

        # make adjacency list
        adj_list = [[] for _ in range(n + 1)]
        for edge in times:
            v_from, v_to, distance = edge
            adj_list[v_from].append((distance, v_to))

        queue = deque([(0, k)])
        distances = [float('inf')] * (n + 1)
        distances[k] = 0
        distances[0] = 0 # does not exist in problem
        in_queue = [False] * (n + 1)
        in_queue[k] = True

        while queue:
            dist, node = queue.popleft()
            in_queue[node] = False

            for neighbor in adj_list[node]:
                neighbor_dist, neighbor_node = neighbor

                candidate_dist = dist + neighbor_dist
                if candidate_dist < distances[neighbor_node]:
                    distances[neighbor_node] = candidate_dist
                    if not in_queue[neighbor_node]:
                        queue.append((distances[neighbor_node], neighbor_node))
                        in_queue[k] = True
        
        max_distance = max(distances)
        return max_distance if max_distance != float('inf') else -1