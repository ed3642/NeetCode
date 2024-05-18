import heapq

class Solution:
    def maxScore(self, nums1: list[int], nums2: list[int], k: int) -> int:
        # join the nums and sort dec on nums2
        # keep a heap for nums1 for top-k elems left of curr num2

        n = len(nums1)
        pairs = list(zip(nums2, nums1))
        pairs.sort(reverse=True)
        heap = []
        
        # build init heap
        for i in range(k - 1):
            heapq.heappush(heap, pairs[i][1])

        max_score = -float('inf')
        best_nums1 = sum(heap)
        for i in range(k - 1, n):
            heapq.heappush(heap, pairs[i][1]) # new num from nums1
            best_nums1 += pairs[i][1]

            best_nums2 = pairs[i][0]
            score = best_nums1 * best_nums2
            max_score = max(max_score, score)

            removed = heapq.heappop(heap) # maintain the top k from nums1
            best_nums1 -= removed

        return max_score