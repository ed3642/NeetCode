from functools import lru_cache

class Solution:
    # https://leetcode.com/problems/maximize-total-cost-of-alternating-subarrays/description/

    def maximumTotalCost(self, nums: list[int]) -> int:
        
        @lru_cache(maxsize=None)
        def max_val(i, is_positive_state):
            if i >= len(nums):
                return 0

            return max(
                max_val(i + 1, True), # start new subarray
                max_val(i + 1, not is_positive_state) # continue building this subarray
            ) + (nums[i] if is_positive_state else -nums[i]) # add this_value

        return max_val(0, True)

    def maximumTotalCost(self, nums: list[int]) -> int:
        
        @lru_cache(maxsize=None)
        def max_val(i, is_positive_state): # the alternating +-+-
            if i >= len(nums):
                return 0
            
            this_val = nums[i] if is_positive_state else -nums[i]
            
            return max(
                this_val + max_val(i + 1, True), # split
                this_val + max_val(i + 1, not is_positive_state) # continue building subarray
            )
        
        return max_val(0, True)
    
    # voodo solution
    def maximumTotalCost(self, nums: list[int]) -> int:
        yes, no = 0, 0
        
        for x in nums[1:]:
            yes, no = x + no, min(yes, no)
            
        return sum(nums) - 2 * min(yes, no)
    
s = Solution()
print(s.maximumTotalCost([-14,-13,-20]))