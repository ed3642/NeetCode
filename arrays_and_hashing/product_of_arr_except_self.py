class Solution:
    # O(n)
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        leftOfI = [1 for _ in nums]
        rightOfI = [1 for _ in nums]

        for i in range(1, len(nums)):
            leftOfI[i] = leftOfI[i - 1] * nums[i - 1]
            rightOfI[i] = rightOfI[i - 1] * nums[-i]

        return [leftOfI[i] * rightOfI[-(i + 1)] for i in range(len(nums))]
    
s = Solution()

nums = [1,2,3,4]

print(s.productExceptSelf(nums))