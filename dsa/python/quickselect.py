import random
from typing import List

class QuickSelect:
    # get the kth elem from the arr if it was sorted in avg(n) and O(n^2)
    def __init__(self, arr: List[int], k: int):
        self.arr = arr
        self.k = k

        self.quickselect(0, len(arr)-1) # kth elem is now in right place

    def partition(self, l, r):
        pivot_i = random.randint(l, r)
        self.arr[pivot_i], self.arr[r] = self.arr[r], self.arr[pivot_i]
        pivot = self.arr[r][0]
        placer_i = l

        for i in range(l, r):
            if self.arr[i][0] <= pivot:
                self.arr[placer_i], self.arr[i] = self.arr[i], self.arr[placer_i]
                placer_i += 1
        
        self.arr[placer_i], self.arr[r] = self.arr[r], self.arr[placer_i]

        return placer_i

    def quickselect(self, l, r):
        if l >= r:
            return
        
        pivot_i = self.partition(l, r)
        if pivot_i == self.k:
            return
        elif pivot_i < self.k:
            self.quickselect(pivot_i + 1, r)
        else:
            self.quickselect(l, pivot_i - 1)