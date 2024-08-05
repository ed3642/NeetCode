class Solution:
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