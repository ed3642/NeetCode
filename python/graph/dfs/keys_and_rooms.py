# https://leetcode.com/problems/keys-and-rooms
from typing import List

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        def dfs(node):
            nonlocal nodes_visited
            if visited[node]: return
            visited[node] = True
            nodes_visited += 1
            for nei in rooms[node]:
                dfs(nei)

        N = len(rooms)
        visited = [False] * N
        nodes_visited = 0
        dfs(0)
        return nodes_visited == N

    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:
        # just visit all neighbors and we should have visited n rooms at the end

        def dfs(room):

            visited.add(room)

            for neighbor in rooms[room]:
                if neighbor not in visited:
                    dfs(neighbor)

        visited = set()
        
        dfs(0)

        return len(visited) == len(rooms)
