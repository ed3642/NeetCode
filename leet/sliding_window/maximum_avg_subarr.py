class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        l = 0
        r = k
        curr_sum = sum(nums[:k]) 
        max_avg = curr_sum / k # starting window
        n = len(nums)

        for i in range(k, n):
            curr_sum = curr_sum + nums[r] - nums[l]
            max_avg = max(max_avg, curr_sum / k)
            r += 1
            l += 1
        
        return max_avg