from collections import deque
import heapq

class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        # SPFA

        # make adj list
        adj_list = [[] for _ in range(n)]
        for v_from, v_to, price in flights:
            adj_list[v_from].append((price, v_to))
        
        queue = deque([(0, 0, src)]) # <price, stops, node>
        prices = [float('inf')] * n
        prices[src] = 0

        while queue:
            price, stops, node = queue.popleft()

            for neighbor in adj_list[node]:
                neighbor_price, neighbor_node = neighbor

                candidate_price = price + neighbor_price
                if candidate_price < prices[neighbor_node] and stops <= k: # only add if we dont exceed k stops
                    prices[neighbor_node] = candidate_price
                    queue.append((prices[neighbor_node], stops + 1, neighbor_node))
        
        return prices[dst] if prices[dst] != float('inf') else -1
    
    def findCheapestPrice2(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        # SPFA

        graph = [[] for _ in range(n)]
        for _from, to, price in flights:
            graph[_from].append((to, price))

        queue = deque([(0, 0, src)]) # <price, num_stops, node>
        #in_queue = set([src]) cant use inqueue in this problem, might miss solution
        prices = [float('inf') for _ in range(n)]
        prices[src] = 0

        while queue:
            price, num_stops, node = queue.popleft()

            if num_stops > k: # these paths are too long
                continue

            for neighbor_node, neighbor_price in graph[node]:
                candidate_price = price + neighbor_price
                if candidate_price < prices[neighbor_node]:
                    prices[neighbor_node] = candidate_price
                    queue.append((candidate_price, num_stops + 1, neighbor_node))

        return prices[dst] if prices[dst] != float('inf') else -1

    def findCheapestPrice3(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        # modified dijkstra
            
        adj_list = [[] for _ in range(n)]
        for v_from, v_to, price in flights:
            adj_list[v_from].append((price, v_to))
        
        heap = [(0, 0, src)] # <price, stops, node>
        stops_arr = [float('inf')] * n
        stops_arr[src] = 0

        while heap:
            price, stops, node = heapq.heappop(heap)

            if stops > stops_arr[node] or stops > k + 1:
                continue
                
            stops_arr[node] = stops

            if node == dst:
                return price

            for neighbor in adj_list[node]:
                neighbor_price, neighbor_node = neighbor
                heapq.heappush(heap, (price + neighbor_price, stops + 1, neighbor_node))

        return -1