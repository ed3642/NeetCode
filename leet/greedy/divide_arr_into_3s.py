# https://leetcode.com/problems/divide-array-into-arrays-with-max-difference

from typing import List

class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        
        # [2,2,2,2,4,5] 2
        # 

        res = []
        nums.sort()

        for i in range(0, len(nums), 3):
            if (nums[i + 2] - nums[i + 1] > k or 
                nums[i + 1] - nums[i] > k or
                nums[i + 2] - nums[i] > k):
                return []
            res.append([nums[i], nums[i + 1], nums[i + 2]])
        
        return res