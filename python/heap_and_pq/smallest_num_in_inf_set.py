from sortedcontainers import SortedSet # not part of the standard python lib but common and accepted by leetcode

class SmallestInfiniteSet:
    # sorted set of nums up to the biggest num
    def __init__(self):
        self.ordered_set = SortedSet()
        self.current_num = 1

    def popSmallest(self) -> int:
        res = 0
        if len(self.ordered_set):
            res = self.ordered_set[0]
            self.ordered_set.discard(res)
        else:
            res = self.current_num
            self.current_num += 1
        return res

    def addBack(self, num: int) -> None:
        if num >= self.current_num or num in self.ordered_set:
            return
        self.ordered_set.add(num)

import heapq
class SmallestInfiniteSet1:
    # keep a heap up to the bound of the biggest num
    def __init__(self):
        self.heap = []
        self.heap_set = set()
        self.largest_num = 1 # largest reached so far

    def popSmallest(self) -> int:
        res = 0

        if len(self.heap):
            res = heapq.heappop(self.heap)
            self.heap_set.remove(res)
        else:
            res = self.largest_num
            self.largest_num += 1

        return res

    def addBack(self, num: int) -> None:
        if num >= self.largest_num or num in self.heap_set:
            return
        
        heapq.heappush(self.heap, num)
        self.heap_set.add(num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)