# https://leetcode.com/problems/largest-rectangle-in-histogram
from typing import List

class Solution:
    
    # O(n) 1 pass
    def largestRectangleArea(self, heights: List[int]) -> int:

        heights.append(0) # stopper and empty out the mono inc stack at the end
        N = len(heights)
        stack = []
        max_area = 0

        for i in range(N):
            while stack and heights[stack[-1]] >= heights[i]:
                h = heights[stack.pop()]
                if not stack:
                    w = i
                else:
                    w = i - stack[-1] - 1
                max_area = max(h * w, max_area)
            stack.append(i)
        
        return max_area

    # O(n) 3 pass
    def largestRectangleArea2(self, heights: List[int]) -> int:
        # look at next smallest to left and right

        N = len(heights)
        next_smallest_i_left = [-1] * N
        next_smallest_i_right = [N] * N

        stack = []
        for i in range(N):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            
            if stack:
                next_smallest_i_left[i] = stack[-1]
            stack.append(i)
        stack = []
        for i in range(N - 1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            
            if stack:
                next_smallest_i_right[i] = stack[-1]
            stack.append(i)

        global_max_area = 0
        for i in range(N):
            # max area using this bar
            area_left = (i - next_smallest_i_left[i]) * heights[i] # including this bar
            area_right = (next_smallest_i_right[i] - (i + 1)) * heights[i] # to the right of this bar
            max_area = area_left + area_right

            global_max_area = max(max_area, global_max_area)
        
        return global_max_area
    
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

    # TLE
    def largestRectangleArea2(self, heights: List[int]) -> int:
        
        stack = []
        max_area = 0

        for i, h in enumerate(heights):
            last_popped = None
            while stack and stack[-1][1] >= h:
                last_popped = stack.pop()

            if last_popped:
                stack.append((last_popped[0], h))
            else:
                stack.append((i, h))
            
            for prev_i, prev_h in stack:
                max_area = max(min(prev_h, h) * (i - prev_i + 1), max_area)

        return max_area
    

