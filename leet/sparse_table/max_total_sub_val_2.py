# https://leetcode.com/problems/maximum-total-subarray-value-ii

from typing import List
import math
import heapq

class SparseTable:
    def __init__(self, arr, is_min):
        n = len(arr)
        k = math.floor(math.log2(n)) + 1 if n > 0 else 1

        # table[j][i] = result of _merge over arr[i : i + 2^j]
        self.is_min = is_min
        default = -float('inf')
        if is_min:
            default = float('inf')
        self.table = [[default] * n for _ in range(k)]
        self.table[0] = arr[:]

        for j in range(1, k):
            for i in range(n - (1 << j) + 1):
                self.table[j][i] = self._merge(
                    self.table[j-1][i],
                    self.table[j-1][i + (1 << (j-1))]
                )

        self.log = [0] * (n + 1)
        for i in range(2, n + 1):
            self.log[i] = self.log[i // 2] + 1

    def _merge(self, a, b):
        # MUST be idempotent: _merge(x, x) == x (overlap between blocks is safe)
        # min:         return min(a, b)          idempotent ✓
        # max:         return max(a, b)          idempotent ✓
        # gcd:         return math.gcd(a, b)     idempotent ✓
        # bitwise AND: return a & b              idempotent ✓
        # bitwise OR:  return a | b              idempotent ✓
        # sum:         return a + b              idempotent ✗ — use segment tree instead
        if self.is_min:
            return min(a, b)
        return max(a, b)

    def query(self, l, r):
        # O(1) — only works because _merge is idempotent (two blocks can safely overlap)
        # if your operation is NOT idempotent, this overlap produces wrong answers
        k = self.log[r - l + 1]
        return self._merge(
            self.table[k][l],
            self.table[k][r - (1 << k) + 1]
        )

class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:

        def consider(l, r):
            if (l, r) not in seen_ranges:
                seen_ranges.add((l, r))
                val = max_st.query(l, r) - min_st.query(l, r)
                heapq.heappush(h, (-val, l, r))
        
        n = len(nums)
        min_st = SparseTable(nums, True)
        max_st = SparseTable(nums, False)

        h = [(-(max_st.query(0, n-1) - min_st.query(0, n-1)), 0, n-1)]
        seen_ranges = set()
        total = 0
        count = 0

        while count < k:
            nval, l, r = heapq.heappop(h)
            total += -nval
            if l < r:
                consider(l+1, r)
                consider(l, r-1)
            count += 1
        
        return total