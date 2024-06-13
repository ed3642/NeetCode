from functools import lru_cache

class Solution:
    
    def canPartition(self, nums: list[int]) -> bool:
        # really strange that putting the recursive calls straight into the return
        # makes this not MLE. If i assign take = ... and leave = ..., this will MLE.
        @lru_cache(maxsize=None)
        def can_partition(i, _sum):
            if _sum == 0:
                return True
            if i >= len(nums) or _sum < 0:
                return False
            
            return (
                can_partition(i + 1, _sum - nums[i]) or # take
                can_partition(i + 1, _sum)) # leave

        total = sum(nums)
        if total % 2 != 0:
            return False
        
        half = total // 2
        nums.sort(reverse=True) # using the biggest numbers first makes us find a solution faster, it will still work even if we dont sort but it is slower.

        return can_partition(0, half)