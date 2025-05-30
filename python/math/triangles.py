from collections import Counter
from typing import List

class Solution:
    def triangleType(self, nums: List[int]) -> str:
        # triangle inequality theorem
        # a + b > c 
        nums.sort()

        a = nums[0]
        b = nums[1]
        c = nums[2]

        if a + b <= c or b + c <= a or c + a <= b:
            return 'none'
        elif a == b and b == c:
            return 'equilateral'
        elif a != b and b != c:
            return 'scalene'
        return 'isosceles'

    def triangleType(self, nums: List[int]) -> str:
        # triangle inequality theorem
        # a + b > c 
        uniques = Counter(nums)
        n = len(uniques)

        if n == 1:
            return 'equilateral'
        elif n == 2:
            common = uniques.most_common(2)
            equal = common[0][0]
            other = common[1][0]
            if equal * 2 <= other:
                return 'none'
            return 'isosceles'
        # with smallest sides
        sorted_uniques = sorted(uniques.keys())
        small1 = sorted_uniques[0]
        small2 = sorted_uniques[1]
        big = sorted_uniques[2]
        if small1 + small2 <= big:
            return 'none'
        return 'scalene'
    
s = Solution()
print(s.triangleType([1,1,2]))