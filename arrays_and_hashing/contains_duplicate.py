class Solution:
    # O(n)
    def containsDuplicate(self, nums: list[int]) -> bool:
        return not len(set(nums)) == len(nums)