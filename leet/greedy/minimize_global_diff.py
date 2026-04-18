# https://leetcode.com/problems/minimum-difference-between-largest-and-smallest-value-in-three-moves/description/
class Solution:
    def minDifference(self, nums: list[int]) -> int:
        # instead of 3 operations, we can make it k operations
        # [2,3,4,5]
        # [0,1,5,10,14]
        # [0,1,1,4,6,6,6]

        n = len(nums)
        k = 3 # for this question, k is always 3
        if n <= k + 1: # can always make all nums eqaual in this case
            return 0
        
        nums.sort()
        min_diff = float('inf')
        l = 0
        r = n - k - 1
        for i in range(k + 1):
            diff = nums[r + i] - nums[l + i]
            min_diff = min(diff, min_diff)

        return min_diff
    