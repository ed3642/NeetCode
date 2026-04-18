# https://leetcode.com/problems/rotate-array
from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # [1,2,3,4,5,6,7]
        # [4,3,2,1,5,6,7] reverse first N - k elems
        # [4,3,2,1,7,6,5] reverse other part
        # [5,6,7,1,2,3,4] reverse whole array

        def reverse(l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l] 
                l += 1
                r -= 1

        N = len(nums)
        k = k % N

        reverse(0, N - 1 - k)
        reverse(N - k, N - 1)
        reverse(0, N - 1)

    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # first reverse the whole arr then
        # reverse the 2 subarrays split at kth elem 

        def reverse(left, right):
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        
        n = len(nums)
        k = k % n
        if k == 0:
            return
        reverse(0, n - 1)
        reverse(0, k - 1)
        reverse(k, n - 1)