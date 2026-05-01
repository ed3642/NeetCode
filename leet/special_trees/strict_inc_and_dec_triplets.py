# https://leetcode.com/problems/count-number-of-teams/
from collections import defaultdict
from typing import List

class Solution:
    def numTeams(self, rating: List[int]) -> int:

        # we can do this bc all ratings are unique otherwise the tree wouldnt be able to keep track of the lt gt

        def make_tree():
            return [0] * (MAX_RATING + 1)

        def query(tree, i):
            count = 0
            while i > 0:
                count += tree[i]
                i -= i & -i
            return count

        def update(tree, i, delta):
            while i <= MAX_RATING:
                tree[i] += delta
                i += i & -i

        def query_lt(tree, x):
            return query(tree, x - 1)

        def query_gt(tree, x):
            return query(tree, MAX_RATING) - query(tree, x)

        MAX_RATING = max(rating)
        n = len(rating)
        left_tree = make_tree()
        right_tree = make_tree()
        count = 0

        # for i in range(n - 1, 0, -1):
        #     update(right_tree, rating[i], 1)
        # start the tree efficiently, above is the easy way, builds tree in O(m) instead of O(m log m)
        for i in range(1, n):
            right_tree[rating[i]] = 1
        for i in range(1, MAX_RATING + 1):
            j = i + (i & -i)
            if j <= MAX_RATING:
                right_tree[j] += right_tree[i]
        
        update(left_tree, rating[0], 1)
        for i in range(1, n - 1):
            update(right_tree, rating[i], -1)

            left_lt = query_lt(left_tree, rating[i])
            left_gt = query_gt(left_tree, rating[i])
            right_lt = query_lt(right_tree, rating[i])
            right_gt = query_gt(right_tree, rating[i])

            count += left_lt * right_gt + left_gt * right_lt

            update(left_tree, rating[i], 1)
        
        return count

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
    
    # O(n^2)
    def numTeams(self, rating: List[int]) -> int:

        def find_triplets(nums):
            n = len(nums)
            pf_gt = defaultdict(lambda: [0] * n)
            pf_lt = defaultdict(lambda: [0] * n)

            for r in nums:
                for i, curr_r in enumerate(nums):
                    prev_i = i - 1 if i > 0 else 0
                    pf_gt[r][i] = pf_gt[r][prev_i]
                    pf_lt[r][i] = pf_lt[r][prev_i]
                    if curr_r > r:
                        pf_gt[r][i] += 1
                    elif curr_r < r:
                        pf_lt[r][i] += 1
            
            total = 0
            for i in range(n - 2):
                left = nums[i]
                for j in range(i + 2, n):
                    if nums[i] < nums[j]:
                        right = nums[j]
                        gt_right = pf_gt[right][j - 1] - pf_gt[right][i]
                        lt_left = pf_lt[left][j - 1] - pf_lt[left][i]
                        size = j - i - 1 # elems in middle
                        total += size - gt_right - lt_left
            
            return total

        return find_triplets(rating) + find_triplets(rating[::-1])

s = Solution()
print(s.numTeams(rating=[2, 5, 3, 4, 1]))