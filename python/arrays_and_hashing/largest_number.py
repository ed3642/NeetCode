
from functools import cmp_to_key
from typing import List


class LargeNumberKey(str):
    def __lt__(a, b):
        return a + b < b + a

class Solution:
    def largestNumber(self, nums: list[int]) -> str:
        nums = [str(num) for num in nums]

        nums.sort(key=LargeNumberKey, reverse=True)

        string = ''.join(nums)
        return string if string[0] != '0' else '0'
    
    def largestNumber(self, nums: List[int]) -> str:
        
        def comparer(a, b):
            p_a = 0
            p_b = 0
            n = len(a)
            m = len(b)

            while True:
                if a[p_a] > b[p_b]:
                    return -1
                elif a[p_a] < b[p_b]:
                    return 1
                else:
                    if p_a == n - 1 and p_b == m - 1: # they are equal
                        return 0
                    p_a = (p_a + 1) % n
                    p_b = (p_b + 1) % m
        
        nums = list(map(str, nums))
        nums.sort(key=cmp_to_key(comparer))
        res = ''.join(nums)
        return res if res[0] != '0' else '0'


    def largestNumber2(self, nums: list[int]) -> str:
        nums = [str(num) for num in nums]

        comparer = lambda x: x * 10

        nums.sort(key=comparer, reverse=True)
        string = ''.join(nums)
        return string if string[0] != 0 else '0'
    
s = Solution()

print(s.largestNumber([999999991,9]))