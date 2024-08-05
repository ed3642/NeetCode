from collections import defaultdict

class Solution:
    def beautifulSubsets(self, nums: list[int], k: int) -> int:
        # gen subsets and prune the search
        # keep a running dict of the path so far

        def backtrack(start, path_num_freq):
            nonlocal res

            for i in range(start, len(nums)):
                op_1 = nums[i] + k
                op_2 = nums[i] - k
                # valid path if we dont have these
                if path_num_freq[op_1] == 0 and path_num_freq[op_2] == 0:
                    res += 1
                    path_num_freq[nums[i]] += 1
                    backtrack(i + 1, path_num_freq)
                    path_num_freq[nums[i]] -= 1

        res = 0
        backtrack(0, defaultdict(int))
        return res