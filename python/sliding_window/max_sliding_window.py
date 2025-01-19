from collections import defaultdict, deque
import heapq
from typing import List

class Solution:

    # O(n) best, can also use this logic for min in window
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # mono dec q to keep track of max in window, popleft index that are out of bounds

        def add_next(i):
            while q and nums[q[-1]] <= nums[i]:
                q.pop()
            q.append(i)

        def remove_last(i):
            while q and q[0] <= i:
                q.popleft()

        N = len(nums)
        res = [0] * (N - (k - 1))
        q = deque() # mono dec queue, store index

        # initial window
        for i in range(k):
            add_next(i)
        res[0] = nums[q[0]]

        for i in range(k, N):
            remove_last(i - k)
            add_next(i)

            res[i - k + 1] = nums[q[0]]

        return res

    # O(n log k)
    def maxSlidingWindow2(self, nums: List[int], k: int) -> List[int]:
        
        N = len(nums)
        res = [0] * (N - (k - 1))
        max_heap = []
        counts = defaultdict(int)
        # initial window
        for i in range(k):
            heapq.heappush(max_heap, -nums[i])
            counts[nums[i]] += 1
        res[0] = -max_heap[0]

        # slide
        for i in range(k, N):
            # add next
            heapq.heappush(max_heap, -nums[i])
            counts[nums[i]] += 1

            # remove
            removed = nums[i - k]
            counts[removed] -= 1 # should never be less than 0

            # check if the biggest has been pushed out already
            while counts[-max_heap[0]] == 0:
                heapq.heappop(max_heap)
            res[i - k + 1] = -max_heap[0]

        return res
    
    # heap
    # O(n log k)
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        # returns largest in window
        def add_to_heap(heap, val, i) -> int:
            while heap and heap[0][1] < i + 1 - k:
                heapq.heappop(heap)
            heapq.heappush(heap, (-val, i))
            return -heap[0][0] # max
            
        # need clever way to keep track of max in window
        r = 0 # right end of window
        res = []
        heap = []
        largest = -float('inf')
    
        # initial window
        for _ in range(k):
            largest = add_to_heap(heap, nums[r], r)
            r += 1
        res.append(largest)

        while r < len(nums):
            largest = add_to_heap(heap, nums[r], r)
            r += 1
            res.append(largest)
        
        return res

    # monotonic dec queue
    # O(n), since each elem is only ever push into and pop out of the queue (2n)
    def maxSlidingWindow2(self, nums: list[int], k: int) -> list[int]:
        def add_to_window(window, i):
            val = nums[i]
            while window and window[-1][0] <= val:
                window.pop()
            window.append((val, i))

        window = deque()
        res = []
        r = 0 # right index of window

        # inital window
        for _ in range(k):
            add_to_window(window, r)
            r += 1
        res.append(window[0][0])

        # slide
        while r < len(nums):
            l = r - k # left index of window - 1, (item to remove)
            if window[0][1] == l: # tail of queue is the item to remove
                window.popleft()
            add_to_window(window, r)
            res.append(window[0][0])
            r += 1
        
        return res
    