from collections import deque

class Solution:
    # topological sort
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        indegree = [0] * numCourses
        queue = deque()
        adj_list = [[] for _ in range(numCourses)]

        # set indegrees and find neighbors
        for a, b in prerequisites:
            indegree[a] += 1
            adj_list[b].append(a)

        # enqueue indegree 0 vertexes
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        curr_pos = 0
        while queue:
            v = queue.popleft()
            curr_pos += 1
            for neighbor in adj_list[v]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        return True if curr_pos == numCourses else False 