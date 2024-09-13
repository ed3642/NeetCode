# NOTE: no need for bst in this problem since we dont need to perform any updates
# a prefix array of xor values will do.

from typing import List

class BST:
    def __init__(self, elems):
        self.N = len(elems)
        self.elems = [0] * (self.N + 1)

        # populate tree
        # for i, val in enumerate(elems):
        #     self.update(i + 1, val)
        for i in range(1, self.N + 1):
            self.elems[i] = elems[i - 1]
        for i in range(1, self.N + 1):
            next_i = i + (i & -i)
            if next_i <= self.N:
                self.elems[next_i] ^= self.elems[i]

    def update(self, i, delta):
        while i <= self.N:
            self.elems[i] ^= delta
            i += i & -i

    def query(self, i):
        total = 0
        while i > 0:
            total ^= self.elems[i]
            i -= i & -i
        return total

    def range_query(self, start, end):
        return self.query(end) ^ self.query(start - 1)

class Solution:
    # with prefix O(n + queries)
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        
        N = len(arr)
        prefix_xor = [0] * (N + 1)
        for i in range(1, N + 1):
            prefix_xor[i] = arr[i - 1]
        for i in range(1, N + 1):
            prefix_xor[i] ^= prefix_xor[i - 1]

        res = [0] * len(queries)
        for i, (start, end) in enumerate(queries):
            res[i] = prefix_xor[end + 1] ^ prefix_xor[start]

        return res

    # with BST O((n + queries) log n)
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        
        bst = BST(arr)
        res = [0] * len(queries)

        for i, (start, end) in enumerate(queries):
            res[i] = bst.range_query(start + 1, end + 1)

        return res