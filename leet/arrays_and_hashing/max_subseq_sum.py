# https://leetcode.com/problems/find-subsequence-of-length-k-with-the-largest-sum

from collections import Counter
from typing import List

class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:

        enumeration = sorted([(num, i) for i, num in enumerate(nums)], reverse=True, key=lambda x: x[0])[:k]

        enumeration.sort(key=lambda x: x[1])
        return [nums[i] for _, i in enumeration]


    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        
        biggest = Counter(sorted(nums, reverse=True)[:k])
        res = []

        for num in nums:
            if num in biggest and biggest[num] > 0:
                res.append(num)
                biggest[num] -= 1
                if len(res) == k:
                    return res
        return res
