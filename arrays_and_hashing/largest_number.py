import functools

class Solution:
    def largestNumber(self, nums: list[int]) -> str:
        nums = [str(num) for num in nums]

        comparer = lambda x: x * 10

        nums.sort(key=comparer, reverse=True)
        string = ''.join(nums)
        return string if string[0] != 0 else '0'
    
s = Solution()

print(s.largestNumber([999999991,9]))