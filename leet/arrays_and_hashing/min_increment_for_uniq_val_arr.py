class Solution:
    def minIncrementForUnique(self, nums: list[int]) -> int:
        
        total = 0
        nums.sort()
        next_min = nums[0] + 1

        for i in range(1, len(nums)):
            if nums[i] < next_min:
                diff = next_min - nums[i]
                nums[i] = next_min
                total += diff
            next_min = nums[i] + 1
        
        return total

s = Solution()
print(s.minIncrementForUnique([1,2,2]))