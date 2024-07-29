# https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/
import heapq

class Solution:
    def findTheCity(self, n: int, edges: list[list[int]], distanceThreshold: int) -> int:
        
        def djikstra(root):
            heap = [(0, root)]
            distances = [float('inf')] * n
            distances[root] = 0
            visited = set([root])
            valid_cities = set()
            while heap:
                dist, node = heapq.heappop(heap)
                if dist > distanceThreshold:
                    # early stop, we will never see closer cities at this point
                    return len(valid_cities)
                visited.add(node)
                for neighbor_node, neighbor_dist in adj_list[node]:
                    if neighbor_node not in visited:
                        candidate_dist = dist + neighbor_dist
                        if candidate_dist < distances[neighbor_node]:
                            distances[neighbor_node] = candidate_dist
                            heapq.heappush(heap, (candidate_dist, neighbor_node))
                            # Check if the city is close enough
                            if candidate_dist <= distanceThreshold:
                                valid_cities.add(neighbor_node)

            return len(valid_cities)

        # build adj_list
        adj_list = [[] for _ in range(n)]
        for _from, _to, weight in edges:
            adj_list[_from].append((_to, weight))
            adj_list[_to].append((_from, weight))

        # see which one has the least num of valid neighbors
        best_city = 0
        best_city_neighbor_count = float('inf')
        for city_id in range(n):
            curr_count = djikstra(city_id)
            if best_city_neighbor_count >= curr_count:
                best_city_neighbor_count = curr_count
                best_city = city_id
        
        return best_city