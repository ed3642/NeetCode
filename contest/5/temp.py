import bisect
from collections import Counter

class Solution:
    def maximumSumSubsequence(self, nums: list[int], queries: list[list[int]]) -> int:
        sorted_nums = sorted(nums)
        freq = Counter(nums)
        max_sum = sum(sorted_nums[-2:])
        res = 0

        for pos, x in queries:
            old = nums[pos]
            nums[pos] = x

            # update freq and sorted_nums
            freq[old] -= 1
            if freq[old] == 0:
                sorted_nums.remove(old)
            bisect.insort(sorted_nums, x)
            freq[x] += 1

            # update max_sum
            max_sum = sum(sorted_nums[-2:])

            res = (res + max_sum)

        return res % (10**9 + 7)