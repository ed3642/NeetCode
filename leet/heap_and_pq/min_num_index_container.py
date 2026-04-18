# https://leetcode.com/problems/design-a-number-container-system
from collections import defaultdict
import heapq

class NumberContainers:

    def __init__(self):
        self.i_to_num = {}
        self.num_i_heap = defaultdict(list)

    def change(self, index: int, number: int) -> None:
        if index in self.i_to_num and self.i_to_num[index] == number:
            return # no need to put same number in same spot
        self.i_to_num[index] = number
        heap = self.num_i_heap[number]
        heapq.heappush(heap, index)

    def find(self, number: int) -> int:
        heap = self.num_i_heap[number]
        while heap and self.i_to_num[heap[0]] != number:
            heapq.heappop(heap) # this number has already been replaced
        if not heap: return -1
        return heap[0]

# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)