# https://leetcode.com/problems/container-with-most-water

from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        N = len(height)
        l = 0
        r = N - 1

        max_a = 0

        while l < r:
            max_a = max(min(height[l], height[r]) * (r - l), max_a)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        
        return max_a
    
    def maxArea(self, heights: list[int]) -> int:
        max_area = 0
        area = 0
        l = 0
        r = len(heights) - 1

        while l < r:
            area = (r - l) * min(heights[l], heights[r])
            max_area = max(max_area, area)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return max_area
    
    def maxArea2(self, height: list[int]) -> int:
        def calc_area(l, r):
            return (r - l) * min(height[l], height[r])
        
        l = 0
        r = len(height) - 1

        max_area = 0

        while l < r:
            max_area = max(max_area, calc_area(l, r))

            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        
        return max_area