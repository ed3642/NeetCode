class FenwickTree:
    # 1 based indexing, 0th elem is ignored
    # inclusive ranges
    def __init__(self, size): # size is max(nums) + 1
        self.size = size
        self.tree = [0] * (size + 1)

    def update(self, i, delta):
        if i == 0:  # add this line
            return
        while i <= self.size:
            self.tree[i] += delta
            i += i & -i

    def query(self, i):
        total = 0
        while i > 0:
            total += self.tree[i]
            i -= i & -i
        return total

    def range_query(self, i, j):
        return self.query(j) - self.query(i - 1)

class Solution: # NOTE: fenwich tree solution unfinished
    def specialArray(self, nums: list[int]) -> int:
        
        n = len(nums)
        tree_size = max(nums) + 1
        bst_tree = FenwickTree(tree_size)

        for num in nums:
            fen_index = num
            bst_tree.update(fen_index, 1) # +1 the freq of num
        
        # candidates
        for i in range(n + 1):
            nums_greater_than_i = bst_tree.query(tree_size - 1) - bst_tree.query(i)
            if i == nums_greater_than_i:
                return i
        return -1

from collections import Counter

# brute force, done
class Solution:
    def specialArray(self, nums: list[int]) -> int:

        freqs = Counter(nums)
        n = len(nums)

        for i in range(1, n + 1):
            count = 0
            for key, f in freqs.items():
                if key >= i:
                    count += f
            if count == i:
                return i
        
        return -1