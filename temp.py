from collections import defaultdict
from functools import lru_cache

class Solution:
    # topdown -> bottomup from below
    def deleteAndEarn(self, nums: list[int]) -> int:
        _max = 0
        totals = defaultdict(int)
        for num in nums:
            totals[num] += num
            _max = max(_max, num)

        best = [0] * (_max + 1)
        best[1] = totals[1]

        for num in range(2, _max + 1):
            best[num] = max(
                best[num - 2] + totals[num],
                best[num - 1]
            )

        return best[_max]

    # get the max and consider each number from it
    def deleteAndEarn(self, nums: list[int]) -> int:
        
        @lru_cache(maxsize=None)
        def best(num):
            if num == 0:
                return 0
            if num == 1:
                return totals[1]
            
            return max(
                best(num - 2) + totals[num],
                best(num - 1),
            )

        _max = 0
        totals = defaultdict(int)
        for num in nums:
            totals[num] += num
            _max = max(_max, num)

        return best(_max)