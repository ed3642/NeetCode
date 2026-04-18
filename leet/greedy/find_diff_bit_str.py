# https://leetcode.com/problems/find-unique-binary-string
from typing import List

class Solution:
    # O(n)
    # make sure each one each string differs by atleast one bit
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        res = []
        for i in range(len(nums)):
            res.append('1' if nums[i][i] == '0' else '0')
        return ''.join(res)

    # O(n log n)
    # get the next expected one
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        
        N = len(nums[0])
        nums.sort()
        expected = 0
        for num in nums:
            curr = int(num, 2)
            if expected != curr:
                bits = bin(expected)[2:]
                len_diff = N - len(bits)
                bits = ('0' * len_diff) + bits
                return bits
            expected += 1
        
        # the missing one is after the entire nums
        bits = bin(expected)[2:]
        len_diff = N - len(bits)
        bits = ('0' * len_diff) + bits
        return bits