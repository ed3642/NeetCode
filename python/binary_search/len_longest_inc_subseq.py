# https://leetcode.com/problems/longest-increasing-subsequence
class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        # This doesnt build the Actual LLS
        # but it keeps the relative values in order where the seq generated will have the same length as the actual LLS
        
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
    
s = Solution()
print(s.lengthOfLIS([10,9,2,5,3,7,101,18,4]))