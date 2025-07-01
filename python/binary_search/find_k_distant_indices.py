# https://leetcode.com/problems/find-all-k-distant-indices-in-an-array

import bisect
from typing import List

class Solution:

    # O(n log k)
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        
        key_indexes = []

        for i, num in enumerate(nums):
            if num == key:
                key_indexes.append(i)
        
        if not key_indexes:
            return []
        
        res = []
        for i in range(len(nums)):
            is_valid = False
            j = bisect.bisect_left(key_indexes, i)
            if j == 0:
                if key_indexes[0] - i <= k:
                    is_valid = True
            elif j == len(key_indexes):
                if i - key_indexes[-1] <= k:
                    is_valid = True
            else:
                if (i - key_indexes[j - 1] <= k or key_indexes[j] - i <= k):
                    is_valid = True
            if is_valid:
                res.append(i)
        
        return res

    # O(n k)
    def findKDistantIndices2(self, nums: List[int], key: int, k: int) -> List[int]:
        
        key_indexes = []

        for i, num in enumerate(nums):
            if num == key:
                key_indexes.append(i)
        
        res = []
        for i in range(len(nums)):
            is_valid = False
            for j in key_indexes:
                if abs(i - j) <= k:
                    is_valid = True
                    break
            if is_valid:
                res.append(i)
        
        return res
    
s = Solution()
print(s.findKDistantIndices(nums = [2,1,1,1,2], key = 2, k = 1))