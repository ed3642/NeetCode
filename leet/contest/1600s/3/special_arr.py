class Solution:
    def isArraySpecial(self, nums: list[int]) -> bool:
        
        prev_parity = nums[0] % 2
        for i in range(1, len(nums)):
            curr = nums[i] % 2
            if prev_parity == curr:
                return False
            prev_parity = curr
        return True