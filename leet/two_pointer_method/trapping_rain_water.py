# https://leetcode.com/problems/trapping-rain-water/
from typing import List

class Solution:

    # O(1) space solution
    def trap(self, height: List[int]) -> int:
        # fix one of the maxes by finding the global peak and exploring each side
        N = len(height)
        peak_i = 0

        for i in range(1, N):
            if height[i] > height[peak_i]:
                peak_i = i
        
        water_area = 0

        # left side
        max_left_i = 0
        for i in range(peak_i):
            if height[i] > height[max_left_i]:
                max_left_i = i
            water_area += height[max_left_i] - height[i] # same formula as below solution but we know height[max_left_i] <= height[peak_i]

        # right side
        max_right_i = N - 1
        for i in range(N - 1, peak_i, -1):
            if height[i] > height[max_right_i]:
                max_right_i = i
            water_area += height[max_right_i] - height[i]
        
        return water_area

    def trap(self, height: List[int]) -> int:
        
        N = len(height)
        max_to_left = [0] * N
        max_to_left[0] = height[0]
        max_to_right = [0] * N
        max_to_right[N - 1] = height[N - 1]

        for i in range(1, N):
            max_to_left[i] = max(max_to_left[i - 1], height[i])
        for i in range(N - 2, -1, -1):
            max_to_right[i] = max(max_to_right[i + 1], height[i])

        water_area = 0
        for i in range(1, N - 1):
            water_area += min(max_to_left[i], max_to_right[i]) - height[i]

        return water_area
    
    # O(n) time O(1) space
    def trap(self, height: list[int]) -> int:
        
        # area = min(max_to_left[i], max_to_right[i]) - height[i]
        # 2 ptr approach, point to the min between each end

        l = 0
        max_from_left = height[l]
        r = len(height) - 1
        max_from_right = height[r]

        total = 0
        while l < r:
            if max_from_left <= max_from_right:
                total += max_from_left - height[l]
                l += 1
                max_from_left = max(height[l], max_from_left)
            else:
                total += max_from_right - height[r]
                r -= 1
                max_from_right = max(height[r], max_from_right)
        
        return total
    
    def trap(self, height: list[int]) -> int:
        
        # area = min(max_to_left[i], max_to_right[i]) - height[i]

        n = len(height)
        max_to_left = height.copy()
        max_to_right = height.copy()

        for i in range(1, n):
            if max_to_left[i-1] < height[i]:
                max_to_left[i] = height[i]
            else:
                max_to_left[i] = max_to_left[i-1]

        for i in range(n - 2, -1, -1):
            if max_to_right[i+1] < height[i]:
                max_to_right[i] = height[i]
            else:
                max_to_right[i] = max_to_right[i+1]

        return sum(
            min(max_to_left[i], max_to_right[i]) - height[i]
            for i in range(n)
        )

    def trap(self, height: list[int]) -> int:
        n = len(height)
        tallest_left = [0] * n
        tallest_right = [0] * n
        temp_tallest = 0
        accumulation = 0

        for i in range(n):
            tallest_left[i] = temp_tallest
            temp_tallest = max(height[i], temp_tallest)

        temp_tallest = 0
        for i in range(n - 1, -1, -1):
            tallest_right[i] = temp_tallest
            temp_tallest = max(height[i], temp_tallest)

        for i in range(len(height)):
            water = min(tallest_left[i], tallest_right[i]) - height[i]
            accumulation += water if water > 0 else 0

        return accumulation
    
s = Solution()

nums = height = [0,1,0,2,1,0,1,3,2,1,2,1]

print(s.trap(nums))