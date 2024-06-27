from collections import deque
import heapq

class Solution:
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
    
s = Solution()
print(s.maxSlidingWindow2(nums = [1,3,-1,-3,5,3,6,7], k = 3))