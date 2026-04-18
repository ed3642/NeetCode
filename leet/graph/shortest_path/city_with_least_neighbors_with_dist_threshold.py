# https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance

from collections import deque
import heapq
from typing import List

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:

        def get_reachable(node):
            heap = [(0, node)]
            distance = [float('inf')] * n
            distance[node] = 0
            visited = [False] * n
            reach_count = 0

            while heap:
                dist, node = heapq.heappop(heap)

                if visited[node]:
                    continue
                visited[node] = True
                reach_count += 1

                for nei, nei_dist in al[node]:
                    cand_dist = dist + nei_dist
                    if cand_dist <= distanceThreshold and cand_dist < distance[nei]:
                        distance[nei] = cand_dist
                        heapq.heappush(heap, (cand_dist, nei))

            return reach_count
        
        al = [[] for _ in range(n)]
        for _from, _to, w in edges:
            al[_from].append((_to, w))
            al[_to].append((_from, w))

        min_city = 0
        min_city_reach = float('inf')

        for city in range(n):
            reach = get_reachable(city)
            if reach <= min_city_reach:
                min_city_reach = reach
                min_city = city

        return min_city

    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:

        def get_reachable(node):
            # SPFA
            q = deque([(0, node)])
            distance = [float('inf')] * n
            distance[node] = 0
            reached = [False] * n
            reached[node] = True
            reach_count = 0

            while q:
                dist, node = q.popleft()

                if not reached[node]:
                    reach_count += 1
                    reached[node] = True

                for nei, nei_dist in al[node]:
                    cand_dist = dist + nei_dist
                    if cand_dist < distance[nei] and cand_dist <= distanceThreshold:
                        distance[nei] = cand_dist
                        q.append((cand_dist, nei))

            return reach_count
        
        al = [[] for _ in range(n)]
        for _from, _to, w in edges:
            al[_from].append((_to, w))
            al[_to].append((_from, w))

        min_city = 0
        min_city_reach = float('inf')

        for city in range(n):
            reach = get_reachable(city)
            if reach <= min_city_reach:
                min_city_reach = reach
                min_city = city

        return min_city
    
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