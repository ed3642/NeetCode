# https://leetcode.com/problems/minimized-maximum-of-products-distributed-to-any-store/
import math
from typing import List

class Solution:
    # like koko loves bananas
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        
        def can_distribute(skid_size):
            used = 0
            for items in quantities:
                used += math.ceil(items / skid_size)
                if used > n:
                    return False
            return True
        
        total_items = sum(quantities)
        min_skid_size = math.ceil(total_items / n)
        max_skid_size = max(quantities)

        l = min_skid_size
        r = max_skid_size

        while l < r:
            m = (l + r) // 2
            if can_distribute(m):
                r = m
            else:
                l = m + 1
        
        return l
    