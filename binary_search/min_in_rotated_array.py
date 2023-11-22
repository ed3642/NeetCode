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

s = Solution()

print(s.findMin([2,3,4,5,6,7,8,9,1]))