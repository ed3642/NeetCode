# https://leetcode.com/problems/daily-temperatures
from typing import List

class Solution:

    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # dont have to store the temp just the index

        N = len(temperatures)
        res = [0] * N
        stack = []

        for i, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                prev_i = stack.pop()
                res[prev_i] = i - prev_i
            stack.append(i)

        return res
    
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        N = len(temperatures)
        res = [0] * N
        stack = []

        for i, temp in enumerate(temperatures):
            while stack and stack[-1][1] < temp:
                prev_i, t = stack.pop()
                res[prev_i] = i - prev_i
            stack.append((i, temp))

        return res