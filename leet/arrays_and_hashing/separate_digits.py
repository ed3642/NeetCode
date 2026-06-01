# https://leetcode.com/problems/separate-the-digits-in-an-array

from typing import List

class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        
        def spread(n):
            digits = []

            while n > 0:
                d = n % 10
                digits.append(d)
                n //= 10
            
            for i in range(len(digits) - 1, -1, -1):
                res.append(digits[i])

        res = []
        for num in nums:
            spread(num)
        return res