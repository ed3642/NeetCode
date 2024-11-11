# https://leetcode.com/problems/course-schedule-ii
from collections import deque
from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        in_degrees = [0] * numCourses
        adj_list = [[] for _ in range(numCourses)]

        # for some reason the problem makes [v1, v2] mean that v1 depends on v2
        for _to, _from in prerequisites:
            in_degrees[_to] += 1
            adj_list[_from].append(_to)
        
        q = deque()
        for course, count in enumerate(in_degrees):
            if count == 0:
                q.append(course)
        
        order = []
        while q:
            course = q.popleft()
            order.append(course)

            for nei in adj_list[course]:
                in_degrees[nei] -= 1
                if in_degrees[nei] == 0:
                    q.append(nei)

        return order if len(order) == numCourses else []
    
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