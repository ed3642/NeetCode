# https://leetcode.com/problems/kth-largest-sum-in-a-binary-tree/
# Definition for a binary tree node.
from collections import deque
from typing import Optional
import heapq

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:

        def partition(l, r, arbitrary_i):
            placer_i = l
            for i in range(l, r):
                if level_sums[i] < level_sums[arbitrary_i]:
                    level_sums[i], level_sums[placer_i] = level_sums[placer_i], level_sums[i]
                    placer_i += 1
            level_sums[r], level_sums[placer_i] = level_sums[placer_i], level_sums[r]
            return placer_i

        def quickselect(l, r):
            nonlocal KTH_BIGGEST_I
            if l == r: return

            pivot_i = partition(l, r, r)

            if KTH_BIGGEST_I < pivot_i:
                quickselect(l, pivot_i - 1)
            elif KTH_BIGGEST_I > pivot_i:
                quickselect(pivot_i + 1, r)
            else:
                return

        q = deque([root])
        level_sums = []
        while q:
            _sum = 0
            for _ in range(len(q)):
                node = q.popleft()
                _sum += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level_sums.append(_sum)

        N = len(level_sums)
        if N < k:
            return -1
        KTH_BIGGEST_I = N - k
        quickselect(0, N - 1)
        return level_sums[KTH_BIGGEST_I]

    # O(n log n)
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        
        q = deque([root])
        level_sums_h = []
        num_levels = 0
        while q:
            _sum = 0
            for _ in range(len(q)):
                node = q.popleft()
                _sum += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if len(level_sums_h) == k:
                if level_sums_h[0] < _sum:
                    heapq.heapreplace(level_sums_h, _sum)
            else:
                heapq.heappush(level_sums_h, _sum)
            num_levels += 1

        if num_levels < k:
            return -1
        return level_sums_h[0]