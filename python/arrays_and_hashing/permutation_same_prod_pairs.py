# https://leetcode.com/problems/tuple-with-same-product/description/
from collections import defaultdict
from typing import List

class Solution:
    # O(n * 2)
    def tupleSameProduct(self, nums: List[int]) -> int:

        # permutations of pairs
        # (a,b)=(c,d) 
        # if (a,b) is chosen -> (a,b) can be placed 2 ways on the left and 2 ways on the right, total 4 ways
        # if we find a matching pair (c,d) every state of (a,b) now has 2 permutations, one where the other side is (c,d) or (d,c)
        # so total (a,b)=(c,d) has 8 ways to arrange the distinct numbers
        
        N = len(nums)
        count = 0
        pairs = defaultdict(int)
        for i in range(N):
            for j in range(i + 1, N):
                prod = nums[i] * nums[j]
                if prod in pairs:
                    count += pairs[prod] * 8
                pairs[prod] += 1

        return count