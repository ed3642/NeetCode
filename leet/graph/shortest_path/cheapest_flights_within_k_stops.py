# https://leetcode.com/problems/cheapest-flights-within-k-stops/

from collections import defaultdict, deque
import heapq
from typing import List

class Solution:

    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        # SPFA

        q = deque([(0, 0, src)])
        g = defaultdict(list)
        d = defaultdict(lambda: float('inf'))
        d[src] = 0

        for f, t, w in flights:
            g[f].append((w, t))

        while q:
            w, stops, node = q.popleft()

            for nei_w, nei in g[node]:
                cand_w = w + nei_w
                if cand_w <= d[nei] and stops <= k:
                    q.append((cand_w, stops + 1, nei))
                    d[nei] = cand_w
    
        return d[dst] if d[dst] != float('inf') else -1

    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        # dijikstra

        h = [(0, 0, src)]
        g = defaultdict(list)
        node_stops = defaultdict(lambda: float('inf'))
        node_stops[src] = 0

        for f, t, w in flights:
            g[f].append((w, t))

        while h:
            w, stops, node = heapq.heappop(h)

            if node == dst:
                return w

            if stops > k: continue
            if stops > node_stops[node]: continue
            node_stops[node] = stops

            for nei_w, nei in g[node]:
                cand_w = w + nei_w
                heapq.heappush(h, (cand_w, stops + 1, nei))
    
        return -1
    
    # O(VE)
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        # Bellman ford
        # has an implementation that lets us find SP with edge list
        # normally runs n - 1 times the relaxation check but we only want k + 1 iterations
        # each iteration is "find the shortest path with 'i' edges" 
        d = [float('inf')] * n
        d[src] = 0

        for _ in range(k + 1): # means find the shortest path with k + 1 edges
            temp = d.copy()
            for f, t, w in flights:
                if d[f] != float('inf'):
                    temp[t] = min(d[f] + w, temp[t])
            d = temp

        return d[dst] if d[dst] != float('inf') else -1

    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # SPFA
        
        adj_list = defaultdict(list)

        for _from, _to, p in flights:
            adj_list[_from].append((_to, p))

        NOT_SET = float('inf')
        q = deque([(0, 0, src)])
        price = defaultdict(lambda: NOT_SET)
        max_next_num_stops = k + 1

        while q:
            p, stops, node = q.popleft()

            next_num_stops = stops + 1
            if next_num_stops > max_next_num_stops:
                continue

            for nei, nei_p in adj_list[node]:
                cand_p = p + nei_p
                if cand_p < price[nei]:
                    q.append((p + nei_p, next_num_stops, nei))
                    price[nei] = cand_p
        
        return price[dst] if price[dst] != NOT_SET else -1

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
                # only add if we dont exceed k stops
                if candidate_price < prices[neighbor_node] and stops <= k: 
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
    
    # not as intuitive for this problem as SPFA, both perform the same
    def findCheapestPrice3(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        # modified dijkstra
        # min path with k-stops constraint
            
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