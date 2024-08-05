# https://leetcode.com/problems/minimum-array-changes-to-make-differences-equal
from collections import defaultdict

class Solution:
    def minChanges(self, nums: list[int], k: int) -> int:
        def calc_need_replace(curr_candidate_diff, abs_min_to_replace):
            need_replaced = 0
            for i in range(n // 2):
                a = nums[i]
                b = nums[n - i - 1]
                diff = abs(a - b)
                if diff != curr_candidate_diff:
                    _min = min(a, b)
                    _max = max(a, b)
                    if (_min + curr_candidate_diff <= k) or (_max - curr_candidate_diff >= 0):
                        need_replaced += 1
                    else:
                        need_replaced += 2
            return min(abs_min_to_replace, need_replaced)

        # greedy?
        n = len(nums)
        diffs = defaultdict(int)

        for i in range(n // 2):
            diff = abs(nums[i] - nums[n - i - 1])
            diffs[diff] += 1

        abs_min_to_replace = float('inf')
        # sort by freq
        diffs = sorted([(diff, f) for diff, f in diffs.items()], key=lambda x: -x[1])

        for diff, f in diffs:
            if ((n // 2) - f) >= abs_min_to_replace: # already found best solution
                break
            abs_min_to_replace = calc_need_replace(diff, abs_min_to_replace)
        
        return abs_min_to_replace
    
s = Solution()
print(s.minChanges(nums = [0,1,2,3,3,6,5,4], k = 6))