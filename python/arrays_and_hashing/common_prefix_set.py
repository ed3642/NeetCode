# https://leetcode.com/problems/find-the-prefix-common-array-of-two-arrays/
from typing import List

class Solution:
    # NOTE: the arrays are permutations of nums [1..n]

    # O(n) better
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:

        N = len(A)
        seen = set()
        res = [0] * N
        intersection_count = 0

        for i in range(N):
            if A[i] in seen:
                intersection_count += 1
            else:
                seen.add(A[i])
            if B[i] in seen:
                intersection_count += 1
            else:
                seen.add(B[i])
            
            res[i] = intersection_count

        return res

    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        
        N = len(A)
        set_a = set()
        set_b = set()
        res = [0] * N

        for i in range(N):
            set_a.add(A[i])
            set_b.add(B[i])
            intersection = set_a & set_b
            res[i] = len(intersection)
        
        return res