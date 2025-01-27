# https://leetcode.com/problems/next-permutation
from typing import List

class Solution:
    
    # clever solution
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def reverse_subarr(l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l] 
                l += 1
                r -= 1

        N = len(nums)

        if N == 1:
            return

        i = N - 2
        while i >= 0:
            if nums[i] < nums[i + 1]:
                # swap i with next bigger num in [i + 1, N - 1]
                next_bigger_i = i + 1
                while next_bigger_i < N - 1:
                    if nums[next_bigger_i + 1] > nums[i]:
                        next_bigger_i += 1
                    else:
                        break
                if nums[N - 1] > nums[i]:
                    next_bigger_i = N - 1
                nums[i], nums[next_bigger_i] = nums[next_bigger_i], nums[i]
                # reverse to right of i
                reverse_subarr(i + 1, N - 1)
                return
            i -= 1

        # whole arr is dec, reverse the whole thing
        reverse_subarr(0, N - 1)
