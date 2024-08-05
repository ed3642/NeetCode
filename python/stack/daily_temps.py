from collections import deque

class Solution:

    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        
        stack = [] # mono dec stack from left
        res = [0] * len(temperatures)

        for i in range(len(temperatures) - 1, -1, -1):
            temp = temperatures[i]

            while stack and temp >= temperatures[stack[-1]]:
                stack.pop()
            # record days until next warmer
            if stack:
                res[i] = stack[-1] - i

            stack.append(i)

        return res

    # monotonic decreasing stack from left to right
    def dailyTemperatures2(self, temperatures: list[int]) -> list[int]:
        n = len(temperatures)
        stack = deque()
        res = [0] * n
        i = 0

        while i < n:
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev_i = stack.pop()
                res[prev_i] = i - prev_i
            stack.append(i)
            i += 1

        return res
    

