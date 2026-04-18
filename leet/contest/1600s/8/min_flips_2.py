class Solution:
    def minOperations(self, nums: list[int]) -> int:
        # we start with a desired state of 1
        # transition the desired state when we flip a bit since all bits after it are flipped as well
        count = 0
        desired_state = 1

        for num in nums:
            if num != desired_state:
                desired_state = num
                count += 1
            
        return count

s = Solution()
print(s.minOperations([0,1,1,0,1]))