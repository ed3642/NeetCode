# https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/
from collections import deque
import heapq

class Solution:
    # O(n log n)
    def longestSubarray(self, nums: list[int], limit: int) -> int:
        # bruh this is hard
        # like max_sliding_window
        # keep track min and max in the window
        # expand the window while conditions are valid
        # move rear up to make the conditions valid again

        def remove_elems_from_heaps(num):
            while max_heap[0][1] < num:
                heapq.heappop(max_heap)
            while min_heap[0][1] < num:
                heapq.heappop(min_heap)
        
        max_length = 1
        min_heap = []
        max_heap = []
        n = len(nums)

        start = 0
        for end in range(n):
            # need to store the 'end' index so we know when it gets left behind by the window
            heapq.heappush(min_heap, (nums[end], end))
            heapq.heappush(max_heap, (-nums[end], end))

            # if window is invalid, slide rear up
            while start < end and -max_heap[0][0] - min_heap[0][0] > limit:
                # point to most problematic elem + 1
                start = min(max_heap[0][1], min_heap[0][1]) + 1

                remove_elems_from_heaps(start)
                
            length = end - start + 1
            max_length = max(length, max_length)

        return max_length
    
    # optimal solution from editorial
    # O (n)
    def longestSubarray(self, nums: list[int], limit: int) -> int:
        max_deque = deque()
        min_deque = deque()
        left = 0
        max_length = 0

        for right in range(len(nums)):
            # Maintain the max_deque in decreasing order
            while max_deque and max_deque[-1] < nums[right]:
                max_deque.pop()
            max_deque.append(nums[right])

            # Maintain the min_deque in increasing order
            while min_deque and min_deque[-1] > nums[right]:
                min_deque.pop()
            min_deque.append(nums[right])

            # Check if the current window exceeds the limit
            while max_deque[0] - min_deque[0] > limit:
                # Remove the elements that are out of the current window
                if max_deque[0] == nums[left]:
                    max_deque.popleft()
                if min_deque[0] == nums[left]:
                    min_deque.popleft()
                left += 1

            max_length = max(max_length, right - left + 1)

        return max_length
    