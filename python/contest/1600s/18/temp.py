class Solution:
    def resultsArray(self, nums: list[int], k: int) -> list[int]:

        N = len(nums)
        res = [-1] * (N - (k - 1))

        # size 1 case
        if k == 1:
            return nums

        i = 1
        while i < N:
            # restart streak when it fails
            streak = 1
            start_index = i - 1
            while i < N and nums[i - 1] + 1 == nums[i]:
                streak += 1
                if streak >= k:
                    res[start_index + streak - k] = nums[i]
                i += 1
            else:
                i += 1

        return res