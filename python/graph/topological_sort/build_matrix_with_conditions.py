# https://leetcode.com/problems/build-a-matrix-with-conditions/
from collections import deque

class Solution:
    def buildMatrix(self, k: int, rowConditions: list[list[int]], colConditions: list[list[int]]) -> list[list[int]]:
        # we could do this with a list as well, which is slightly faster
        def topological_sort(edges):
            order = {i: -1 for i in range(1, k + 1)} # we can use a dict to easily match with the other order later
            in_degrees = {i: 0 for i in range(1, k + 1)}
            adj_list = {i: [] for i in range(1, k + 1)}

            for _from, _to in edges:
                in_degrees[_to] += 1
                adj_list[_from].append(_to)

            queue = deque()
            for elem, degree in in_degrees.items():
                if degree == 0:
                    queue.append(elem)

            placed = 0
            while queue:
                elem = queue.popleft()
                order[elem] = placed
                placed += 1

                for neighbor in adj_list[elem]:
                    in_degrees[neighbor] -= 1
                    if in_degrees[neighbor] == 0:
                        queue.append(neighbor)
            
            return order if placed == k else None

        
        # topological sort to bind the top-most numbers to and row 
        # and the left-most numbers to a col
        # place them in that order

        matrix = [[0 for _ in range(k)] for _ in range(k)]

        top_most = topological_sort(rowConditions)
        if not top_most:
            return []
        left_most = topological_sort(colConditions)
        if not left_most:
            return []

        # place the elems
        for elem, row in top_most.items():
            col = left_most[elem]
            matrix[row][col] = elem

        return matrix
