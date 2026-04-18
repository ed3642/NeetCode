# https://leetcode.com/problems/range-sum-query-mutable/description/
class NumArray:
    # fenwich tree bst
    def __init__(self, nums: list[int]):
        self.size = len(nums)
        self.tree = [0] * (self.size + 1)
        self.nums = nums.copy()

        # O(n log n) way of initializing tree
        # for i, num in enumerate(nums):
        #     self.update_tree(i + 1, num)

        # O(n) way of initializing tree
        # put in the values
        for i in range(1, self.size + 1):
            self.tree[i] = self.nums[i - 1]

        # propagate the values up the tree
        for i in range(1, self.size + 1):
            next_i = i + (i & -i)
            if next_i <= self.size:
                self.tree[next_i] += self.tree[i]

    def query(self, index):
        total = 0
        while index > 0:
            total += self.tree[index]
            index -= index & -index
        return total
    
    def update_tree(self, index, delta):
        while index <= self.size:
            self.tree[index] += delta
            index += index & -index

    def update(self, index: int, val: int) -> None:
        delta = val - self.nums[index]
        self.update_tree(index + 1, delta)
        self.nums[index] = val

    def sumRange(self, left: int, right: int) -> int:
        return self.query(right + 1) - self.query(left)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)