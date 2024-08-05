class SegmentTree:
    # static array, cant modify array after tree creation
    # find min in range in O(logn) time
    def __init__(self, arr):
        self.n = len(arr)
        self.arr = arr
        self.tree = [0] * (4 * self.n)
        self.build_tree(0, self.n - 1, 0)

    def build_tree(self, ss, se, si):
        if ss == se:
            self.tree[si] = ss
        else:
            mid = (ss + se) // 2
            self.build_tree(ss, mid, 2 * si + 1)
            self.build_tree(mid + 1, se, 2 * si + 2)
            if self.arr[self.tree[2 * si + 1]] < self.arr[self.tree[2 * si + 2]]:
                self.tree[si] = self.tree[2 * si + 1]
            else:
                self.tree[si] = self.tree[2 * si + 2]

    def range_min_query(self, qs, qe):
        def query(ss, se, si):
            if ss > qe or se < qs:
                return -1
            if qs <= ss and qe >= se:
                return self.tree[si]
            mid = (ss + se) // 2
            left = query(ss, mid, 2 * si + 1)
            right = query(mid + 1, se, 2 * si + 2)
            if left == -1:
                return right
            if right == -1:
                return left
            if self.arr[left] < self.arr[right]:
                return left
            else:
                return right
        return query(0, self.n - 1, 0)

class Solution:
    # O(n logn)
    def largestRectangleArea(self, heights: list[int]) -> int:
        # divide and conquer
        def calc_max(l, r):
            length = r - l + 1
            if length <= 0:
                return 0
            if length == 1:
                return heights[l]

            min_index = segment_tree.range_min_query(l, r)
            flat_area = length * heights[min_index]

            left_sub_prob_end = min_index - 1 if min_index - 1 >= 0 else 0
            right_sub_prob_start = min_index + 1 if min_index + 1 <= r else r


            return (
                max(
                    flat_area,
                    calc_max(l, left_sub_prob_end),
                    calc_max(right_sub_prob_start, r)
                )
            )

        segment_tree = SegmentTree(heights)
        
        return calc_max(0, len(heights) - 1)