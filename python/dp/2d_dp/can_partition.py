from functools import lru_cache

class Solution:
    # first time i see the topdown solution be faster than the bottom up
    def canPartition(self, nums: list[int]) -> bool:
        
        @lru_cache(maxsize=None)
        def can_partition(i, _sum):

            if _sum == 0:
                return True
            if i >= len(nums) or _sum < 0: # prune the search
                return False

            return (
                can_partition(i + 1, _sum - nums[i]) or # take
                can_partition(i + 1, _sum) # leave
            )
            
        total = sum(nums)
        if total % 2 != 0:
            return False
        nums.sort(reverse=True) # using the biggest numbers first gets us a solution faster, not sorting still works but is slower
        half = total // 2 
        return can_partition(0, half)

    def canPartition(self, nums: list[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        nums.sort(reverse=True)
        half = total // 2
        n = len(nums)
        # can_par[index][_sum] -> up to index, can we find subseq that sums to _sum
        can_par = [[False for _ in range(half + 1)] for _ in range(n + 1)]
        for i in range(n + 1):
            can_par[i][0] = True

        for end in range(1, n + 1):
            num = nums[end - 1]
            for _sum in range(half + 1):
                if num <= _sum:
                    can_par[end][_sum] = (
                        can_par[end - 1][_sum - num] or
                        can_par[end - 1][_sum]
                    )
                else:
                    can_par[end][_sum] = can_par[end - 1][_sum]

        return can_par[n][half]
