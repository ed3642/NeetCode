# https://leetcode.com/problems/max-sum-of-a-pair-with-equal-sum-of-digits

from collections import defaultdict
from typing import List

class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        
        def get_digit_sum(num):
            total = 0
            while num > 0:
                total += num % 10
                num //= 10
            return total
        
        def add_num_to_group(num, group):
            if len(group) < 1:
                group.append(num)
                return
            if len(group) < 2:
                group.append(num)
                if group[0] > group[1]:
                    group[0], group[1] = group[1], group[0]
                return
            # already 2
            if num > group[1]:
                # bigger than both
                group[0] = group[1]
                group[1] = num
            elif num > group[0]:
                # bigger than smaller
                group[0] = num

        groups = defaultdict(list)

        for num in nums:
            add_num_to_group(num, groups[get_digit_sum(num)])
        
        biggest = -1
        for group in groups.values():
            if len(group) < 2:
                continue
            biggest = max(group[0] + group[1], biggest)
        
        return biggest