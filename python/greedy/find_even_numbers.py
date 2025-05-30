# https://leetcode.com/problems/finding-3-digit-even-numbers

from collections import Counter
from typing import List

class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        # the constraints are so small that all possile optioins are in [100, 999]
        # a good solution is to just check that space

        counts = Counter(digits)
        res = []

        for n in range(100, 1000, 2):
            # check if we can make n
            third = n % 10
            second = (n // 10) % 10
            first = (n // 100) % 10

            uniques = set([first, second, third])

            if len(uniques) == 1:
                if counts[first] >= 3:
                    res.append(n)
            elif len(uniques) == 2:
                if ((first == second and counts[first] >= 2 and counts[third] >= 1) or
                    (first == third and counts[first] >= 2 and counts[second] >= 1) or
                    (second == third and counts[second] >= 2 and counts[first] >= 1)):
                    res.append(n)
            else: # len 3
                if counts[first] >= 1 and counts[second] >= 1 and counts[third] >= 1:
                    res.append(n)
        
        return res

    def findEvenNumbers2(self, digits: List[int]) -> List[int]:
        N = len(digits)
        possible = set()

        for i in range(N):
            if digits[i] == 0:
                continue
            for j in range(N):
                if i == j:
                    continue
                for k in range(N):
                    if j == k or i == k:
                        continue
                    if digits[k] % 2 != 0:
                        continue
                    possible.add(int(digits[i] * 100 + digits[j] * 10 + digits[k]))
        
        return sorted(possible)
    