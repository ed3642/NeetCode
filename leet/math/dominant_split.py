# https://leetcode.com/problems/minimum-index-of-a-valid-split

from collections import Counter
from typing import List

class Solution:

    # O(n) and O(1) memory
    def minimumIndex(self, nums: List[int]) -> int:

        # majority voting 

        dominant = nums[0]
        dominant_count = 1
        for num in nums[1:]:
            if num == dominant:
                dominant_count += 1
            else:
                dominant_count -= 1
                if dominant_count == 0:
                    dominant = num
                    dominant_count = 1
                
        left_has = 0 # dominant count on left split

        # get the actualy dominant count
        dominant_count = 0
        for num in nums:
            if num == dominant:
                dominant_count += 1

        for i in range(len(nums)):
            if nums[i] == dominant:
                left_has += 1
            left_non_dominant = i + 1 - left_has
            left_need = left_non_dominant + 1
            if left_has >= left_need:
                right_has = dominant_count - left_has
                right_non_dominant = len(nums) - 1 - i - right_has
                right_need = right_non_dominant + 1
                if right_has >= right_need:
                    return i
        
        return -1
    
    # O(n) and O(n) memory
    def minimumIndex2(self, nums: List[int]) -> int:
        
        counts = Counter(nums)

        dominant = -float('inf')
        dominant_count = 0
        for num, f in counts.items():
            if f > dominant_count:
                dominant_count = f
                dominant = num
                
        left_has = 0 # dominant count on left split

        for i in range(len(nums)):
            if nums[i] == dominant:
                left_has += 1
            left_non_dominant = i + 1 - left_has
            left_need = left_non_dominant + 1
            if left_has >= left_need:
                right_has = counts[dominant] - left_has
                right_non_dominant = len(nums) - 1 - i - right_has
                right_need = right_non_dominant + 1
                if right_has >= right_need:
                    return i
        
        return -1
    
s = Solution()
print(s.minimumIndex([1,2,1,1]))