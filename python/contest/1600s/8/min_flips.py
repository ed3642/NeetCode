class Solution:
    def minOperations(self, nums: list[int]) -> int:
        # sliding window flip them until it turns into a 1 and rear
        # if last 3 elems are not all the same its impossible

        def flip(l):
            for i in range(3):
                nums[l + i] = 1 - nums[l + i] 

        n = len(nums)
        count = 0
        # try to flip em
        for i in range(n - 2): 
            if nums[i] == 0: 
                flip(i)
                count += 1

        # we missed one
        if any(num == 0 for num in nums):
            return -1
        
        return count

s = Solution()
print(s.minOperations([1,0,0,1,1,0,1,1,1,0,0,0,1,0,1]))