# https://leetcode.com/problems/top-k-frequent-elements
import heapq
from collections import Counter
import random
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # perfect use of quickselect, used for getting kth or top k elems

        def partition(l, r):
            pivot_i = random.randint(l, r)
            elems[pivot_i], elems[r] = elems[r], elems[pivot_i]
            pivot = elems[r][0]
            placer_i = l

            for i in range(l, r):
                if elems[i][0] <= pivot:
                    elems[placer_i], elems[i] = elems[i], elems[placer_i]
                    placer_i += 1
            
            elems[placer_i], elems[r] = elems[r], elems[placer_i]

            return placer_i

        def quickselect(l, r):
            if l >= r:
                return
            
            pivot_i = partition(l, r)
            if pivot_i == kth_elem_i:
                return
            elif pivot_i < kth_elem_i:
                quickselect(pivot_i + 1, r)
            else:
                quickselect(l, pivot_i - 1)
            
        freqs = Counter(nums)
        elems = [(f, num) for num, f in freqs.items()]
        kth_elem_i = len(freqs) - k
        quickselect(0, len(elems) - 1)

        return [num for _, num in elems[kth_elem_i:]]

    # there is an Average(n) solution: quickselect, though O(n)
    # quickselect can be used to solve top-k type problems instead of heap
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = Counter(nums)
        h = []

        for num, f in freq.items():
            if len(h) < k:
                heapq.heappush(h, (f, num))
            else:
                heapq.heappushpop(h, (f, num))
        
        return [num for _, num in h]

    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        counter = Counter(nums)

        heap = []

        for num in counter:
            heapq.heappush(heap, (-counter[num], num))

        res = []
        for _ in range(k):
            _, num = heapq.heappop(heap)
            res.append(num)
        
        return res