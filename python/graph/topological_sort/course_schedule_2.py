from collections import deque

class Solution:
    # O(V + E)
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        
        indegree = [0] * numCourses
        queue = deque()
        adj_list = [[] for _ in range(numCourses)]

        # set initial indegrees and get neighbors
        for a, b in prerequisites:
            indegree[a] += 1
            adj_list[b].append(a)

        # set initial courses
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        
        course_order = []
        while queue:
            course = queue.popleft()
            course_order.append(course)
            for neighbor in adj_list[course]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        
        return course_order if len(course_order) == numCourses else []