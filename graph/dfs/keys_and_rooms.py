class Solution:
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
