class Solution:
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