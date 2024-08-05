from collections import deque

class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        # monotonic stack
        # extend rectangles

        stack = [] # apparently just using an [] is faster than deque(), overhead maybe
        max_area = 0

        for i, h in enumerate(heights):
            last_index = i
            while stack and stack[-1][1] > h:
                # make space
                last_index, last_pop = stack.pop()
                max_area = max((i - last_index) * last_pop, max_area)
            stack.append((last_index, h))
        # empty stack and check missed areas
        while stack:
            last_index, last_pop = stack.pop()
            max_area = max((len(heights) - last_index) * last_pop, max_area)
        
        return max_area
