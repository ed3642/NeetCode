from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        
        graph = [[] for _ in range(numCourses)]

        indegrees = [0 for _ in range(numCourses)]
        for to, _from in prerequisites:
            graph[_from].append(to)
            indegrees[to] += 1

        res = []
        queue = deque()
        for course in range(len(indegrees)):
            if indegrees[course] == 0:
                queue.append(course)
                res.append(course)

        while queue:
            course = queue.popleft()

            for neighbor_course in graph[course]:
                indegrees[neighbor_course] -= 1
                if indegrees[neighbor_course] == 0:
                    queue.append(neighbor_course)
                    res.append(neighbor_course)
        
        return res if len(res) == numCourses else []
