from collections import deque

class Solution:

    # monotonic decreasing stack from left to right
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
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
