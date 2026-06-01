# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array

from typing import List

class Solution:
    def findMin(self, nums: list[int]) -> int:
        n = len(nums)
        l = 0
        r = n - 1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] < nums[r]:
                r = mid
            else:
                l = mid + 1
        
        return nums[l - 1]
    
    def findMin(self, nums: List[int]) -> int:

        n = len(nums)
        if nums[0] < nums[-1]:
            return nums[0]
        if n == 1:
            return nums[0]
        
        l = 0
        r = n-1
        
        while l < r:
            m = (l+r)//2
            if nums[l] < nums[m] > nums[r]:
                l = m+1
            else:
                r = m
        
        if l < n-1:
            return min(nums[l], nums[l+1])
        return nums[l]

    def findMin2(self, nums: list[int]) -> int:
        n = len(nums)
        l = 0
        r = n - 1

        while r - l > 1:
            m = (l + r) // 2
            if nums[m] > nums[r]:
                l = m
            else:
                r = m
        
        return nums[l] if nums[l] < nums[r] else nums[r]
    
    # i like this version more
    def findMin3(self, nums: list[int]) -> int:
        l = 0
        r = len(nums) - 1
        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        
        return nums[l]
        