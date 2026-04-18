# https://leetcode.com/problems/number-of-sub-arrays-with-odd-sum/
from typing import List

class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        
        # [1,2,3,4,5,6,7]
        # [1,1,0,0,1,1,0] parity of pf sum
        # [1,2,2,2,3,4,4] num odd pf sums
        # [1,1,2,3,3,3,4] num even pf sums

        MOD = 10 ** 9 + 7

        num_even = 1 # 0 sum array is even
        num_odd = 0
        total_odd_sub_arr = 0
        pf_sum = 0

        for num in arr:
            pf_sum += num
            if pf_sum % 2 == 0:
                total_odd_sub_arr += num_odd
                num_even += 1
            else:
                total_odd_sub_arr += num_even
                num_odd += 1

        return total_odd_sub_arr % MOD
            