# https://leetcode.com/problems/longest-increasing-subsequence
class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        # rare case were building the seq is faster than just counting how long it is
        
        def bisect_left(arr, item):
            l = 0
            r = len(arr)
            while l < r:
                m = (l + r) // 2
                if arr[m] < item:
                    l = m + 1
                else:
                    r = m
            return l

        seq = [nums[0]]

        for num in nums[1:]:
            if seq[-1] < num:
                seq.append(num)
            else:
                insert_index = bisect_left(seq, num)
                seq[insert_index] = num
    
        return len(seq)