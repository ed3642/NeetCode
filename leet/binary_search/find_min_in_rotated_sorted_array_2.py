# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii

from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        # O(n)
        # theta(log n)

        n = len(nums)
        l = 0
        r = n-1

        while l < r:
            m = (l+r)//2
            if nums[m] < nums[r]:
                r = m
            elif nums[m] > nums[r]:
                l = m+1
            else:
                # need to check next time m is different than r
                # i think its best to just full search the remaining options
                return min(nums[l:r+1])
                 
        return nums[l]

    def findMin(self, nums: List[int]) -> int:
        
        # informal proof for why O(n) is best we can do
        # assume algo returns min in sorted rotated array by only looking at only half of the array and the solution is at index i and equals x
        # if the input is a list of values x and some value y where y < x where y is not on the half that happens to be inspected then y will be skipped. This is because an input of all values x and an input xs and 1 value can not be distinguished without specifically identifying y.
        # therefore we must inspect all values in the array to garantee correctness.

        # however we can still do average case O(log n)
        return min(nums)