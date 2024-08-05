class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return 0
        
        l = 0
        r = len(nums) - 1
        while l < r:
            m = (l + r) // 2
            if nums[m] < nums[m + 1]:
                l = m + 1
            else:
                r = m
        
        return l
    
    def findPeakElement2(self, nums: list[int]) -> int:
        l = 0
        r = len(nums) - 1

        if len(nums) <= 2:
            _max = max(nums)
            return nums.index(_max)

        while l < r:
            m = (l + r) // 2
            if nums[m - 1] < nums[m] > nums[m + 1]:
                return m
            elif nums[m - 1] < nums[m] < nums[m + 1]:
                l = m + 1
            else:
                r = m
        
        return l
    
    def findPeakElement3(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return 0
        
        l = 0
        r = len(nums) - 1
        while l + 1 < r:
            m = (l + r) // 2
            if nums[m] < nums[m + 1]:
                l = m
            else:
                r = m

        # its l when theres only 2 elems in nums else its always l + 1
        return l if nums[l] > nums[l + 1] else l + 1