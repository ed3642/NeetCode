from collections import Counter
import heapq
import random

# https://leetcode.com/problems/sort-an-array
class Solution:
    # O(n) average but O(n^2) worst
    # quicksort, this fails the problems test cases but its a good impl of quicksort
    def sortArray(self, nums: list[int]) -> list[int]:
        # quicksort with random pivot

        def partition(l, r):
            pivot_i = random.randint(l, r)
            nums[pivot_i], nums[r] = nums[r], nums[pivot_i]
            pivot = nums[r]
            placer_i = l
            for i in range(l, r):
                if nums[i] < pivot:
                    nums[i], nums[placer_i] = nums[placer_i], nums[i]
                    placer_i += 1
            nums[r], nums[placer_i] = nums[placer_i], nums[r]
            return placer_i

        def quicksort(l, r):
            if l < r:
                pivot_i = partition(l, r)
                quicksort(l, pivot_i - 1)
                quicksort(pivot_i + 1, r)
        
        quicksort(0, len(nums) - 1)
        return nums

    # O(n log n)
    # heap sort
    def sortArray(self, nums: list[int]) -> list[int]:
        heapq.heapify(nums)
        res = []
        while nums:
            res.append(heapq.heappop(nums))
        return res

    # O(n + k)
    # counting sort
    def sortArray(self, nums: list[int]) -> list[int]:
        _min = min(nums)
        _max = max(nums)
        counts = Counter(nums)

        i = 0
        for num in range(_min, _max + 1):
            for _ in range(counts[num]):
                nums[i] = num
                i += 1
        
        return nums