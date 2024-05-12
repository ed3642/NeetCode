class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        
        l = 0
        r = 0
        budget = k
        curr_len = 0
        max_len = 0
        n = len(nums)

        while r < n:
            adding = nums[r]

            if adding == 1 or budget > 0:
                if adding == 0:
                    budget -= 1
                curr_len += 1
                r += 1
            else:
                leaving = nums[l]
                if leaving == 0:
                    budget += 1
                curr_len -= 1
                l += 1
                
            max_len = max(max_len, curr_len)
        
        return max_len
