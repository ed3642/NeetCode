# https://leetcode.com/problems/top-k-frequent-elements/
from collections import Counter
import random

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        
        # quick select on the frequencies
        # want top-k freqs

        def partition(l, r, arbitrary_i):
            arbitrary_val = freqs[uniques[arbitrary_i]]

            placer_i = l
            for i in range(l, r):
                curr_val = freqs[uniques[i]]
                if curr_val < arbitrary_val:
                    uniques[i], uniques[placer_i] = uniques[placer_i], uniques[i]
                    placer_i += 1
            
            # put placer in the pivot position
            uniques[r], uniques[placer_i] = uniques[placer_i], uniques[r]

            return placer_i # the pivot
                    

        def quickselect(l, r):
            # base case: 1 elem is always sorted
            if l == r: 
                return
            # we can also do randint(l, r) but i dont see why it matters
            arbitrary_i = r

            pivot_i = partition(l, r, arbitrary_i)

            if pivot_i == KTH_BIGGEST_INDEX:
                return
            elif pivot_i < KTH_BIGGEST_INDEX:
                quickselect(pivot_i + 1, r)
            else:
                quickselect(l, pivot_i - 1)

        freqs = Counter(nums)
        uniques = list(freqs.keys())
        N = len(uniques)
        KTH_BIGGEST_INDEX = N - k
        quickselect(0, N - 1)
        
        return uniques[KTH_BIGGEST_INDEX:]