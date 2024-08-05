class Solution:
    # thee XOR of a number with itself is 0
    # XOR of number with 0 is the number itself
    # XOR is commutative and associative so order does not matter
    def singleNumber(self, nums: list[int]) -> int:
        res = nums[0]
        for i in range(1, len(nums)):
            res ^= nums[i]
        return res # number without a pair is the result