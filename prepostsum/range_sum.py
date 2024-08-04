import heapq

# https://leetcode.com/problems/range-sum-of-sorted-subarray-sums
# range sum of subarrays
class Solution:
    # O(N^2 log n), better in general
    def rangeSum(self, nums: list[int], n: int, left: int, right: int) -> int:
        # proper use of heap, like each start of a subarray is a LL from this problem
        # https://leetcode.com/problems/merge-k-sorted-lists
        heap = []
        MOD = 10 ** 9 + 7

        heap = [(_sum, i) for i, _sum in enumerate(nums)]
        heapq.heapify(heap)

        total = 0
        skipped = 0
        count = 0
        while heap:
            _sum, i = heapq.heappop(heap)

            if skipped >= left - 1:
                total += _sum
            else:
                # these sums are before left index
                skipped += 1

            count += 1
            if count >= right: # done
                break
            # subarray can still grow
            if i + 1 < n:
                heapq.heappush(heap, (_sum + nums[i + 1], i + 1))

        return total % MOD

    # O(n^2 log n)
    def rangeSum(self, nums: list[int], n: int, left: int, right: int) -> int:
        # tried max heap to section off the array sum, its slower than just sorting
        MOD = 10 ** 9 + 7

        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + nums[i]

        sums = []
        for end in range(n):
            for start in range(end + 1):
                sums.append(prefix_sum[end + 1] - prefix_sum[start]) 

        # want these sums only
        total = 0
        sums.sort()
        for i in range(left - 1, right):
            total += sums[i]

        return total % MOD
    