from typing import Callable, List, Optional, Any

class SegmentTree:
    def __init__(self, arr: List[Any], function: Callable[[Any, Any], Any]):
        """
        Initialize the segment tree.

        :param arr: The input array for which the segment tree is built.
        :param function: The function to be applied on the range queries. It could be min, max, sum, etc.
        """
        self.n = len(arr)
        self.function = function
        self.tree = [0] * (4 * self.n)
        self.build_tree(arr, 0, self.n - 1, 0)

    def build_tree(self, arr: List[Any], ss: int, se: int, si: int) -> None:
        """
        Build the segment tree from the input array.

        :param arr: The input array.
        :param ss: The start index of the segment of the input array.
        :param se: The end index of the segment of the input array.
        :param si: The current index of the node in the segment tree.
        """
        if ss == se:
            self.tree[si] = arr[ss]
        else:
            mid = (ss + se) // 2
            self.build_tree(arr, ss, mid, 2 * si + 1)
            self.build_tree(arr, mid + 1, se, 2 * si + 2)
            self.tree[si] = self.function(self.tree[2 * si + 1], self.tree[2 * si + 2])

    def range_query(self, qs: int, qe: int) -> Any:
        """
        Perform a range query on the segment tree.

        :param qs: The start index of the query range.
        :param qe: The end index of the query range.
        :return: The result of the function applied on the range [qs, qe].
        """
        def query(ss: int, se: int, si: int) -> Optional[Any]:
            if ss > qe or se < qs:
                return None
            if qs <= ss and qe >= se:
                return self.tree[si]
            mid = (ss + se) // 2
            left = query(ss, mid, 2 * si + 1)
            right = query(mid + 1, se, 2 * si + 2)
            if left is None:
                return right
            if right is None:
                return left
            return self.function(left, right)
        return query(0, self.n - 1, 0)
    
    def update(self, i: int, value: Any) -> None:
        """
        Update the value at index i in the input array and reflect the changes in the segment tree.

        :param i: The index in the input array to be updated.
        :param value: The new value to be updated at index i.
        """
        def update_util(ss: int, se: int, si: int) -> None:
            if i < ss or i > se:
                return
            if ss == se:
                self.tree[si] = value
            else:
                mid = (ss + se) // 2
                update_util(ss, mid, 2 * si + 1)
                update_util(mid + 1, se, 2 * si + 2)
                self.tree[si] = self.function(self.tree[2 * si + 1], self.tree[2 * si + 2])
        update_util(0, self.n - 1, 0)