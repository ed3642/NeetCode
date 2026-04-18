# https://leetcode.com/problems/course-schedule-iv

from collections import deque
from typing import List

class Solution:
    
    # optimal
    # this updates prereq in O(1)
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:

        prereq_of = [0 for _ in range(numCourses)]
        adj_list = [[] for _ in range(numCourses)]
        in_degree = [0] * numCourses

        for _from, _to in prerequisites:
            adj_list[_from].append(_to)
            in_degree[_to] += 1

        stack = [] 
        for node in range(numCourses):
            if in_degree[node] == 0:
                stack.append(node)

        while stack:
            node = stack.pop()

            for nei in adj_list[node]:
                prereq_of[nei] = prereq_of[nei] | (1 << node) # node itself
                prereq_of[nei] = prereq_of[nei] | prereq_of[node] # parent path
                in_degree[nei] -= 1
                if in_degree[nei] == 0:
                    stack.append(nei)
        
        res = [False] * len(queries)
        for i, (possible_prereq, node) in enumerate(queries):
            res[i] = (prereq_of[node] & (1 << possible_prereq)) != 0
        
        return res

    # can also use bitmask to keep track of paths
    # this update prereq paths in O(k) where k is the avg prereq path lenght
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:

        prereq_of = [set() for _ in range(numCourses)]
        adj_list = [[] for _ in range(numCourses)]
        in_degree = [0] * numCourses

        for _from, _to in prerequisites:
            adj_list[_from].append(_to)
            in_degree[_to] += 1

        stack = [] 
        for node in range(numCourses):
            if in_degree[node] == 0:
                stack.append(node)

        while stack:
            node = stack.pop()

            for nei in adj_list[node]:
                prereq_of[nei].add(node) # parent itself
                prereq_of[nei].update(prereq_of[node]) # parent path
                in_degree[nei] -= 1
                if in_degree[nei] == 0:
                    stack.append(nei)
        
        res = [False] * len(queries)
        for i, (possible_prereq, node) in enumerate(queries):
            res[i] = possible_prereq in prereq_of[node]
        
        return res

    # TLE
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        def dfs(node, path: set):
            for nei in adj_list[node]:
                if nei not in path:
                    path.add(nei)
                    for path_node in path:
                        prereq_of[nei].add(path_node)
                    dfs(nei, path)
                    path.remove(nei)

        prereq_of = [set() for _ in range(numCourses)]
        adj_list = [[] for _ in range(numCourses)]

        for _from, _to in prerequisites:
            adj_list[_from].append(_to)

        for node in range(numCourses):
            dfs(node, set([node]))
        
        res = [False] * len(queries)
        for i, (possible_prereq, node) in enumerate(queries):
            res[i] = possible_prereq in prereq_of[node]
        
        return res
    