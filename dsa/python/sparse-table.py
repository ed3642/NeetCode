import math

class SparseTable:
    # query indempotent operation on range in O(1)

    def __init__(self, arr):
        n = len(arr)
        k = math.floor(math.log2(n)) + 1 if n > 0 else 1

        # table[j][i] = result of _merge over arr[i : i + 2^j]
        self.table = [[self._default()] * n for _ in range(k)]
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

    def _default(self):
        # identity/neutral value for your operation:
        # min:          return float('inf')
        # max:          return float('-inf')
        # gcd:          return 0
        # bitwise AND:  return (1 << 31) - 1    (all 1s)
        # bitwise OR:   return 0
        return float('inf')

    def _merge(self, a, b):
        # MUST be idempotent: _merge(x, x) == x (overlap between blocks is safe)
        # min:         return min(a, b)          idempotent ✓
        # max:         return max(a, b)          idempotent ✓
        # gcd:         return math.gcd(a, b)     idempotent ✓
        # bitwise AND: return a & b              idempotent ✓
        # bitwise OR:  return a | b              idempotent ✓
        # sum:         return a + b              idempotent ✗ — use segment tree instead
        return min(a, b)

    def query(self, l, r):
        # O(1) — only works because _merge is idempotent (two blocks can safely overlap)
        # if your operation is NOT idempotent, this overlap produces wrong answers
        k = self.log[r - l + 1]
        return self._merge(
            self.table[k][l],
            self.table[k][r - (1 << k) + 1]
        )
