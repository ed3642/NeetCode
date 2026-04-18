# https://leetcode.com/problems/count-number-of-teams/
class FenwickTree:
    # 1 based indexing, 0th elem is ignored
    # inclusive ranges
    # useful for freq range queries
    def __init__(self, size): # size is max(nums) + 1
        self.size = size
        self.tree = [0] * (size + 1)

    def update(self, index, delta):
        while index <= self.size:
            self.tree[index] += delta
            index += index & -index

    def query(self, index):
        total = 0
        while index > 0:
            total += self.tree[index]
            index -= index & -index
        return total

    def range_query(self, start, end):
        return self.query(end) - self.query(start - 1)

    def less_than(self, value, max_index):
        return self.query(min(value - 1, max_index))

    def greater_than(self, value, max_index):
        return self.query(max_index) - self.query(min(value, max_index))

class Solution:
    # O(n log _max)
    def numTeams(self, rating: list[int]) -> int:
        n = len(rating)
        count = 0
        _max = max(rating)

        bit_right = FenwickTree(_max)
        bit_left = FenwickTree(_max)

        count_smaller_to_left = [0] * n
        count_bigger_to_left = [0] * n
        count_smaller_to_right = [0] * n
        count_bigger_to_right = [0] * n

        # populate bit_left and keep track of whats to the left
        for i in range(n):
            count_smaller_to_left[i] = bit_left.less_than(rating[i], _max)
            count_bigger_to_left[i] = bit_left.greater_than(rating[i], _max)
            bit_left.update(rating[i], 1)

        # populate bit_right and keep track of whats to the right
        for i in range(n - 1, -1, -1):
            count_smaller_to_right[i] = bit_right.less_than(rating[i], _max)
            count_bigger_to_right[i] = bit_right.greater_than(rating[i], _max)
            bit_right.update(rating[i], 1)
        
        # calculate value triples
        for i in range(n):
            count += count_smaller_to_left[i] * count_bigger_to_right[i]
            count += count_bigger_to_left[i] * count_smaller_to_right[i]

        return count

s = Solution()
print(s.numTeams(rating=[2, 5, 3, 4, 1]))