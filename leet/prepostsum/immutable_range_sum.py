# https://leetcode.com/problems/range-sum-query-immutable/

from typing import List

class NumArray:

    def __init__(self, nums: List[int]):
        self.pf = nums
        self.n = len(nums)
        for i in range(1, self.n):
            self.pf[i] += self.pf[i - 1]

    def sumRange(self, left: int, right: int) -> int:
        l = left - 1
        if l < 0:
            return self.pf[right]
        return self.pf[right] - self.pf[l]
    
class NumArray:

    def __init__(self, nums: List[int]):
        self.pf_sum = nums

        for i in range(1, len(nums)):
            self.pf_sum[i] += self.pf_sum[i - 1]

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.pf_sum[right]
        return self.pf_sum[right] - self.pf_sum[left - 1]


class NumArray:

    def __init__(self, nums: list[int]):
        self.prefix_sum = nums.copy()
        for i in range(1, len(nums)):
            self.prefix_sum[i] += self.prefix_sum[i - 1]
        print(self.prefix_sum)

    def sumRange(self, left: int, right: int) -> int:
        if left - 1 < 0:
            return self.prefix_sum[right]
        return self.prefix_sum[right] - self.prefix_sum[left - 1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)