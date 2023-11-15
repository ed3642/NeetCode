class Solution:
    # there is a O(1) space complexity solution with two pointer but this will do
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