from collections import defaultdict
import heapq
from typing import List

class Solution:
    # https://leetcode.com/problems/reconstruct-itinerary/
    # i think this is more efficient
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        def dfs(node):
            
            while adj_list[node]:
                nei = heapq.heappop(adj_list[node])
                dfs(nei)
            path.append(node)

        adj_list = defaultdict(list)
        for _from, _to in tickets:
            heapq.heappush(adj_list[_from], _to)

        path = []
        dfs('JFK')
        return reversed(path)

    def findItinerary(self, tickets: list[list[str]]) -> list[str]:
        # dfs variation (hierholzer algorithm)
        # eulerian path
        # problem guarantees that verticies have correct outdegrees and starting node JFK is a valid starting point

        # to ensure our nodes are visited by min lexilogical order we sort the adj lists
        # This can be done by sorting the edge list first (next solution)

        # build graph
        adj_list = defaultdict(list)
        for _from, to in tickets:
            adj_list[_from].append(to)

        for lst in adj_list.values():
            lst.sort(reverse=True)

        # Hierholzer's algorithm: finds eurilian path if G requirements are met
        def dfs(node):
            while adj_list[node]:
                dfs(adj_list[node].pop())
            path.append(node)

        path = []
        dfs("JFK")

        return path[::-1]

    # sort edge list first
    def findItinerary2(self, tickets: list[list[str]]) -> list[str]:

        # sort edges
        tickets.sort(reverse=True)

        # build graph
        adj_list = defaultdict(list)
        for _from, to in tickets:
            adj_list[_from].append(to)

        # Hierholzer's algorithm
        def dfs(node):
            while adj_list[node]:
                dfs(adj_list[node].pop())
            path.append(node)

        path = []
        dfs("JFK")

        return path[::-1]