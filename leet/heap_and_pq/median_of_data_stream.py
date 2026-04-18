# https://leetcode.com/problems/find-median-from-data-stream

import heapq

class MedianFinder:

    # [2,3] [4] 1
    # [1,2] [3,4]

    # [1,2] [3] 4
    # [1,2] [3,4]

    # [-1] []
    # [-2] [-1]

    def __init__(self):
        self.left_heap = []
        self.right_heap = []
        self.parity = 1

    def addNum(self, num: int) -> None:
        if not self.left_heap:
            heapq.heappush(self.left_heap, -num)
        elif not self.right_heap:
            top_left = -self.left_heap[0]
            if top_left > num:
                heapq.heapreplace(self.left_heap, -num)
                heapq.heappush(self.right_heap, top_left)
            else:
                heapq.heappush(self.right_heap, num)
        else:
            top_left = -self.left_heap[0]
            if self.parity == 0:
                # making total size even
                if num < top_left:
                    heapq.heapreplace(self.left_heap, -num)
                    heapq.heappush(self.right_heap, top_left)
                else:
                    heapq.heappush(self.right_heap, num)
            else:
                # making total size odd
                if num < top_left:
                    heapq.heappush(self.left_heap, -num)
                else:
                    top_right = self.right_heap[0]
                    if num <= top_right:
                        heapq.heappush(self.left_heap, -num)
                    else:
                        heapq.heapreplace(self.right_heap, num)
                        heapq.heappush(self.left_heap, -top_right)
        self.parity = (self.parity + 1) % 2

    def findMedian(self) -> float:
        if self.parity == 1:
            # is currently even size
            top_left = -self.left_heap[0]
            top_right = self.right_heap[0]
            return (top_left + top_right) / 2
        else:
            # is currently odd size
            return -self.left_heap[0]
