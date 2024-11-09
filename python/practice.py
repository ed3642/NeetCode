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