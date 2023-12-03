
class LargeNumberKey(str):
    def __lt__(a, b):
        return a + b < b + a

class Solution:
    def largestNumber(self, nums: list[int]) -> str:
        nums = [str(num) for num in nums]

        nums.sort(key=LargeNumberKey, reverse=True)

        string = ''.join(nums)
        return string if string[0] != '0' else '0'




    def largestNumber2(self, nums: list[int]) -> str:
        nums = [str(num) for num in nums]

        comparer = lambda x: x * 10

        nums.sort(key=comparer, reverse=True)
        string = ''.join(nums)
        return string if string[0] != 0 else '0'
    
s = Solution()

print(s.largestNumber([999999991,9]))