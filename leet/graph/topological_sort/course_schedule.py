# https://leetcode.com/problems/course-schedule/
from collections import deque
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        in_degrees = [0] * numCourses
        q = deque()
        courses_sorted = 0
        adj_list = [[] for _ in range(numCourses)]

        for _from, _to in prerequisites:
            adj_list[_from].append(_to)
            in_degrees[_to] += 1
        
        for course, count in enumerate(in_degrees):
            if count == 0:
                q.append(course)
                courses_sorted += 1
        
        while q:
            course = q.popleft()

            for nei in adj_list[course]:
                in_degrees[nei] -= 1
                if in_degrees[nei] == 0:
                    courses_sorted += 1
                    q.append(nei)
        
        return numCourses == courses_sorted
    
    # fast
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        
        N = numCourses
        adj_list = [[] for _ in range(N)]
        in_degrees = [0] * N

        for _from, _to in prerequisites:
            adj_list[_from].append(_to)
            in_degrees[_to] += 1

        q = deque()
        completed = 0
        visited = set()
        for node, degree in enumerate(in_degrees):
            if degree == 0 and node not in visited:
                visited.add(node)
                completed += 1
                q.append(node)
        
        while q:
            node = q.popleft()
            for nei_node in adj_list[node]:
                in_degrees[nei_node] -= 1
                if in_degrees[nei_node] == 0 and nei_node not in visited:
                    visited.add(nei_node)
                    completed += 1
                    q.append(nei_node)

        return completed == N

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