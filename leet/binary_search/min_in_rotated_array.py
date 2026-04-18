class Solution:
    def findMin(self, nums: list[int]) -> int:
        n = len(nums)
        l = 0
        r = n - 1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] < nums[r]:
                r = mid
            else:
                l = mid + 1
        
        return nums[l - 1]

    def findMin2(self, nums: list[int]) -> int:
        n = len(nums)
        l = 0
        r = n - 1

        while r - l > 1:
            m = (l + r) // 2
            if nums[m] > nums[r]:
                l = m
            else:
                r = m
        
        return nums[l] if nums[l] < nums[r] else nums[r]
    
    # i like this version more
    def findMin3(self, nums: list[int]) -> int:
        l = 0
        r = len(nums) - 1
        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        
        return nums[l]
        

s = Solution()

print(s.findMin([2,3,4,5,6,7,8,9,1]))