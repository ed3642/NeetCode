class Solution:
    # O(n) time and saves some space
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        
        # add the ones so we dont have to handle edge cases
        n = len(nums)
        res = [1] * n
        
        postfix = 1
        for i in range(n - 1, -1, -1):
            res[i] = postfix
            postfix *= nums[i]

        prefix = 1
        for i in range(n):
            res[i] *= prefix
            prefix *= nums[i]

        return res

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