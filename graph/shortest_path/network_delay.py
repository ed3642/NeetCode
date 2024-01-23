import heapq

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