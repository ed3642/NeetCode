class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        A = set(nums1)
        B = set(nums2)
        return [list(A - B), list(B - A)]