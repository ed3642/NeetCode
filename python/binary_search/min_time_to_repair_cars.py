# https://leetcode.com/problems/minimum-time-to-repair-cars

import math
from typing import List

class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        
        # [1,2,3,4]
        # [2,2,2,4]

        def can_finish(time):
            cars_left = cars
            for r in ranks:
                fixed = int(math.sqrt(time / r))
                cars_left -= fixed
                if cars_left <= 0: 
                    return True
            return False

        l = 1
        r = 100 * (cars ** 2)

        while l < r:
            m = (l + r) // 2
            if can_finish(m):
                r = m
            else:
                l = m + 1
        
        return l
    