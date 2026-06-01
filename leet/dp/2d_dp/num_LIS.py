from typing import List

class Solution:

    # O(n^2)
    def findNumberOfLIS(self, nums: List[int]) -> int:
        # interesting dp problem that required 2 dp arrays instead of a 2d dp

        n = len(nums)
        # lis[i] = LIS up to i
        lis = [1 for _ in range(n)]
        # f[i] = freq of LIS ending at i
        f = [1 for _ in range(n+1)]
        longest_seen = 1

        for r in range(1, n):
            for l in range(r):
                if nums[r] > nums[l]:
                    if lis[l]+1 > lis[r]:
                        lis[r] = lis[l]+1
                        f[r] = f[l]
                        longest_seen = max(lis[r], longest_seen)
                    elif lis[l]+1 == lis[r]:
                        f[r] += f[l]
        
        count = 0
        for i in range(n):
            if lis[i] == longest_seen:
                count += f[i]
        
        return count

    # O(n^3) TLE but all valid dp, good for practice of dp notions
    def findNumberOfLIS(self, nums: List[int]) -> int:
        
        n = len(nums)
        # dp[i][len] = num of LIS size len
        dp = [[0 for _ in range(n + 1)] for _ in range(n)]

        for i in range(n):
            dp[i][1] = 1
        
        for length in range(1, n):
            for r in range(n):
                for l in range(r):
                    if nums[r] > nums[l]:
                        dp[r][length + 1] += dp[l][length]
                    

        longest = 0
        for length in range(n, 0, -1):
            for i in range(n):
                if dp[i][length] > 0:
                    longest = length
                    break
            if longest != 0:
                break
        
        count = 0
        for i in range(n):
            count += dp[i][longest]

        return count

