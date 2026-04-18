# https://leetcode.com/problems/put-marbles-in-bags

import heapq
from typing import List

class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        # dont need to get the actual scores just the difference
        # [1,5,1,3,1]
        # [1,3,5,1]
        # [1,1,3,5]

        N = len(weights)

        splits = [0] * (N - 1)
        for i in range(N - 1):
            splits[i] = weights[i] + weights[i + 1]
        splits.sort()

        # score of largest k - 1 splits minus smallest k - 1 splits
        # the difference is the same if we calculated the actual min_score and max_score
        return sum(splits[(N - 1) - (k - 1):]) - sum(splits[:k - 1])

    def putMarbles(self, weights: List[int], k: int) -> int:
        
        # [1,5,1,3,1]
        # [1,3,5,1]
        # [1,1,3,5]

        N = len(weights)
        min_score = 0
        max_score = 0

        splits = [0] * (N - 1)
        for i in range(N - 1):
            splits[i] = (weights[i] + weights[i + 1], i)
        splits.sort(key=lambda x: x[0])

        # get min_score
        prev_i = 0
        for i in range(k - 1):
            split_i = splits[i][1]
            min_score += weights[prev_i] + weights[split_i]
            prev_i = split_i + 1
        min_score += weights[prev_i] + weights[N - 1]
        # get max_score
        prev_i = 0
        for i in range(k - 1):
            split_i = splits[-(i + 1)][1]
            max_score += weights[prev_i] + weights[split_i]
            prev_i = split_i + 1
        max_score += weights[prev_i] + weights[N - 1]
        
        return max_score - min_score

    def putMarbles(self, weights: List[int], k: int) -> int:
        # dont even need a heap
        # [1,5,1,3,1]
        # [1,3,5,1]
        # [1,1,3,5]

        N = len(weights)
        heap = []
        max_heap = []
        min_score = 0
        max_score = 0

        for i in range(N - 1):
            heapq.heappush(heap, (weights[i] + weights[i + 1], i))
            heapq.heappush(max_heap, (-(weights[i] + weights[i + 1]), i))

        # get min_score
        min_splits = [0] * (k - 1)
        for i in range(k - 1):
            score, split_i = heapq.heappop(heap)
            min_splits[i] = split_i
        prev_i = 0
        for i in range(k - 1):
            split_i = min_splits[i]
            min_score += weights[prev_i] + weights[split_i]
            prev_i = split_i + 1
        min_score += weights[prev_i] + weights[N - 1]
        # get max_score
        max_splits = [0] * (k - 1)
        for i in range(k - 1):
            score, split_i = heapq.heappop(max_heap)
            max_splits[i] = split_i
        prev_i = 0
        for i in range(k - 1):
            split_i = max_splits[i]
            max_score += weights[prev_i] + weights[split_i]
            prev_i = split_i + 1
        max_score += weights[prev_i] + weights[N - 1]
        
        return max_score - min_score