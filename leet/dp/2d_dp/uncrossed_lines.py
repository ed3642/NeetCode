# https://leetcode.com/problems/uncrossed-lines

from typing import List

class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        
        # answer is just LCS?

        n = len(nums1)
        m = len(nums2)
        # lcs[i][j] 
        lcs = [[0 for _ in range(m+1)] for _ in range(n+1)]

        for i in range(n):
            for j in range(m):
                if nums1[i] == nums2[j]:
                    lcs[i+1][j+1] = max(lcs[i][j]+1, lcs[i+1][j+1])
                else:
                    lcs[i+1][j+1] = max(lcs[i][j+1], lcs[i+1][j])
        
        return lcs[n][m]