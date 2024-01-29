class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return 0
        
        