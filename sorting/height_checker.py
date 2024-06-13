from collections import Counter

class Solution:
    def heightChecker(self, heights: list[int]) -> int:
        # built in sort -> O(n log n)
        # counting sort -> O(n + k) where k is the range of values
        def count_sort(arr):
            _min = min(arr)
            _max = max(arr)
            freqs = Counter(arr)
            res = []

            for num in range(_min, _max + 1):
                for _ in range(freqs[num]):
                    res.append(num)
            
            return res


        expected = count_sort(heights)
        count = 0

        for i in range(len(heights)):
            if heights[i] != expected[i]:
                count += 1
        
        return count