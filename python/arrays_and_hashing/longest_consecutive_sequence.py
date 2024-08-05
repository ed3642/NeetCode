# https://leetcode.com/problems/longest-consecutive-sequence
class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if len(nums) == 0:
            return 0
        
        opts = set(nums)

        longest_streak = 0
        while len(opts) > 0:
            root = opts.pop()
            left_end = root - 1
            right_end = root + 1
            streak = 1
            while left_end in opts:
                opts.remove(left_end)
                left_end -= 1
                streak += 1
            while right_end in opts:
                opts.remove(right_end)
                right_end += 1
                streak += 1

            longest_streak = max(streak, longest_streak)

        return longest_streak
    
    def longestConsecutive(self, nums: list[int]) -> int:
        maxCount = 0
        hs = set(nums)
        hm = dict() # <num, chainLength>

        while hs:
            num = hs.pop()
            if not num in hm:
                hm[num] = 1
                # check chains to the right
                temp = num + 1
                while temp in hs:
                    hm[num] += 1
                    hs.remove(temp)
                    temp += 1
                # check chains to the left
                temp = num - 1
                while temp in hs:
                    hm[num] += 1
                    hs.remove(temp)
                    temp -= 1
            maxCount = max(maxCount, hm[num])

        return maxCount
             
    
s = Solution()

nums = [0,3,7,2,5,8,4,6,0,1,999999999]

print(s.longestConsecutive(nums))