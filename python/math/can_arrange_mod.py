# https://leetcode.com/problems/check-if-array-pairs-are-divisible-by-k/
from typing import List

class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        rems = [0] * k

        for num in arr:
            rems[num % k] += 1
        if rems[0] % 2 != 0:
            return False
        for i in range(1, len(rems) // 2 + 1):
            if rems[i] != rems[k - i]:
                return False
        return True