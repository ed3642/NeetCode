from collections import Counter
import heapq

# https://leetcode.com/problems/sort-an-array
class Solution:
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