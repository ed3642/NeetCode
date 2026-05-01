# https://leetcode.com/problems/rotate-function

from typing import List

class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        # see explanation in first solution

        n = len(nums)
        prev_f = 0
        s = sum(nums)
        
        for i in range(n):
            prev_f += i * nums[i]
        max_f = prev_f

        for i in range(1, n):
            f = s + prev_f - n * nums[(n - i)]
            max_f = max(f, max_f)
            prev_f = f
        
        return max_f

    def maxRotateFunction(self, nums: List[int]) -> int:
        
        # [4,3,2,6,4,3,2,6]

        # F(k+1) = sum(A_k) + F(k) - (n)A_k[n - 1]
        # F(k) = s + F(k - 1) - (n)A_(k-1)[n - 1]
        # To solve this problem you have to write out the summation relations of F(k + 1) in terms of F(k)

        n = len(nums)
        f = [0] * n
        s = sum(nums)
        
        for i in range(n):
            f[0] += i * nums[i]
        for i in range(1, n):
            f[i] = s + f[i - 1] - n * nums[(n - i)]
        
        return max(f)