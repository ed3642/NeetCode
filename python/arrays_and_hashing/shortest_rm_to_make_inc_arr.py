# https://leetcode.com/problems/shortest-subarray-to-be-removed-to-make-array-sorted
from typing import List

class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        
        N = len(arr)
        # find end of decreasing arr from right to left
        r = N - 1
        while r > 1 and arr[r - 1] <= arr[r]:
            r -= 1
        right_start = r

        # check what we have to remove from the right array to join it with the left
        longest_join = N - r
        for l in range(right_start):
            while r < N and arr[l] > arr[r]:
                r += 1
            left_len = l + 1
            right_len = N - r
            longest_join = max(left_len + right_len, longest_join)
            if arr[l] > arr[l + 1]:
                break
        
        return N - longest_join
