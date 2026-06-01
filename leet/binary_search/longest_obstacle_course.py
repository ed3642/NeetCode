# https://leetcode.com/problems/find-the-longest-valid-obstacle-course-at-each-position

from bisect import bisect_right
from typing import List

class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        
        n = len(obstacles)
        res = [1] * n
        lis = []

        for i in range(n):
            placer_i = bisect_right(lis, obstacles[i])
            if placer_i == len(lis):
                lis.append(obstacles[i])
            else:
                lis[placer_i] = obstacles[i]
            res[i] = placer_i+1

        return res