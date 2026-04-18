class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        # there is always exaclty 1 cycle in input

        # cycle detection
        a = nums[0]
        b = nums[0]

        while True:
            a = nums[a]
            b = nums[nums[b]]
            if a == b: break

        # find start of cycle
        a = nums[0]
        while a != b:
            a = nums[a]
            b = nums[b]

        return a