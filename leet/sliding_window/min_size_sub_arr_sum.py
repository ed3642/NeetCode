# https://leetcode.com/problems/minimum-size-subarray-sum
class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        
        start = 0
        _sum = 0
        min_length = float('inf')
        n = len(nums)

        for end in range(n):
            num = nums[end]
            _sum += num

            # shrink window until it meets constraint
            while _sum >= target:
                min_length = min(end - start + 1, min_length)
                _sum -= nums[start]
                start += 1
        
        return min_length if min_length != float('inf') else 0
    