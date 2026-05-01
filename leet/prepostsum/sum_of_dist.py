# https://leetcode.com/problems/sum-of-distances/

from collections import defaultdict
from typing import List

class Solution:

    def distance(self, nums: List[int]) -> List[int]:
        # could be cleaner and less redundant

        n = len(nums)
        dist_left = defaultdict(int)
        dist_right = defaultdict(int)
        indexes_right = defaultdict(list)
        indexes_left = defaultdict(list)
        res = [0] * n

        for i in range(n - 1, -1, -1):
            num = nums[i]
            if num not in indexes_right:
                indexes_right[num].append(i)
            else:
                part_dist = indexes_right[num][-1] - i
                dist_right[nums[i]] += len(indexes_right[num]) * part_dist
                indexes_right[num].append(i)

        for i, num in enumerate(nums):
            prev_num_i = i
            if num in indexes_left:
                prev_num_i = indexes_left[num][-1]
            part_dist = i - prev_num_i
            dist_right[num] -= len(indexes_right[num]) * part_dist
            dist_left[num] += len(indexes_left[num]) * part_dist
            indexes_left[num].append(i)
            indexes_right[num].pop()

            res[i] = dist_left[num] + dist_right[num]

        return res

    def distance2(self, nums: List[int]) -> List[int]:
        # TLE
        
        n = len(nums)
        indexes = defaultdict(list)

        for i in range(n - 1, -1, -1):
            indexes[nums[i]].append(i)

        res = [0] * n

        for num in nums:
            num_indexes = indexes[num]
            if len(num_indexes) > 1:
                dist = 0
                curr_num_i = num_indexes.pop()
                for i in num_indexes:
                    part = i - curr_num_i
                    dist += part
                    res[i] += part
                res[curr_num_i] += dist
        
        return res
