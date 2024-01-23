import heapq

class Solution:
    # returns the distance and previous node link that forms the shortest path
    def dijkstra(self, edges: list[list[int]], n: int, source_node: int) -> int:

        # make adjacency list
        adj_list = [[] for _ in range(n)]
        for edge in edges:
            v_from, v_to, distance = edge
            adj_list[v_from].append((distance, v_to))
        
        # initialize
        visited = [False] * n
        distances = [float('inf')] * n
        previous = [None] * n

        heap = [(0, source_node)]
        distances[source_node] = 0

        while heap:
            dist, node = heapq.heappop(heap)
            visited[node] = True

            for neighbor in adj_list[node]:
                neighbor_dist, neighbor_node = neighbor

                if not visited[neighbor_node]:
                    candidate_dist = dist + neighbor_dist
                    if candidate_dist < distances[neighbor_node]:
                        previous[neighbor_node] = node
                        distances[neighbor_node] = candidate_dist
                        heapq.heappush(heap, (distances[neighbor_node], neighbor_node))
        
        return list(zip(distances, previous))
