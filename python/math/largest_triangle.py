# https://leetcode.com/problems/largest-triangle-area

from typing import List

class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        # cleaned up shoelace formula for triangle

        N = len(points)

        max_area = 0

        for i in range(N - 2):
            x1, y1 = points[i]
            for j in range(i + 1, N - 1):
                x2, y2 = points[j]
                for k in range(j + 1, N):
                    x3, y3 = points[k]
                    max_area = max(abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)), max_area)
        
        return max_area / 2 # only divide at the end to save computation

    def largestTriangleArea(self, points: List[List[int]]) -> float:

        def calc_area(p1, p2, p3):
            # shoelace formula for polygon with triangle case
            x1, y1 = points[p1]
            x2, y2 = points[p2]
            x3, y3 = points[p3]
            return 0.5 * abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))

        N = len(points)

        max_area = 0

        for i in range(N - 2):
            for j in range(i + 1, N - 1):
                for k in range(j + 1, N):
                    max_area = max(calc_area(i, j, k), max_area)
        
        return max_area
    
    def largestTriangleArea(self, points: List[List[int]]) -> float:

        def calc_area(p1, p2, p3):
            # general shoelace formula
            x1, y1 = points[p1]
            x2, y2 = points[p2]
            x3, y3 = points[p3]
            return 0.5 * abs((x1 * y2 - x2 * y1) + (x2 * y3 - x3 * y2) + (x3 * y1 - x1 * y3))

        N = len(points)

        max_area = 0

        for i in range(N - 2):
            for j in range(i + 1, N - 1):
                for k in range(j + 1, N):
                    max_area = max(calc_area(i, j, k), max_area)
        
        return max_area

    def largestTriangleArea(self, points: List[List[int]]) -> float:

        def calc_area(p1, p2, p3):
            # semi perimeter triangle area
            x1, y1 = points[p1]
            x2, y2 = points[p2]
            x3, y3 = points[p3]
            a = (abs((x1 - x2) ** 2 + (y1 - y2) ** 2)) ** 0.5
            b = (abs((x1 - x3) ** 2 + (y1 - y3) ** 2)) ** 0.5
            c = (abs((x3 - x2) ** 2 + (y3 - y2) ** 2)) ** 0.5
            s = (a + b + c) / 2
            return (abs(s * (s - a) * (s - b) * (s - c))) ** 0.5

        N = len(points)

        max_area = 0

        for i in range(N - 2):
            for j in range(i + 1, N - 1):
                for k in range(j + 1, N):
                    max_area = max(calc_area(i, j, k), max_area)
        
        return max_area