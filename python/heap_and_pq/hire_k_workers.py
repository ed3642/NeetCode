import heapq

class Solution:
    def totalCost(self, costs: list[int], k: int, candidates: int) -> int:
        # 2 heaps
        # if min between the 2 heaps in on the first pool, pop left and add the elem to the right of left half
        # vise versa for the second half but the elem to the left of it
        # keep track of the bounds of the pools with 2 ptrs
        # if they overlap just switch to single heap and get the remaining employees

        def get_remaining_cost(heap, need):
            total = 0
            for _ in range(need):
                if not heap:
                    return total
                total += heapq.heappop(heap)
            return total

        n = len(costs)
        total_cost = 0
        left_end = candidates - 1
        right_start = (n - 1) - (candidates - 1)
        need = k

        # check if their borders touch at the start
        if left_end >= right_start - 1:
            heapq.heapify(costs)
            return get_remaining_cost(costs, need)

        pool1 = costs[:left_end + 1]
        heapq.heapify(pool1)
        pool2 = costs[right_start:]
        heapq.heapify(pool2)

        for _ in range(k):
            # check if their borders touch at the start of each round
            if left_end >= right_start - 1:
                heap = pool1 + pool2
                heapq.heapify(heap)
                return get_remaining_cost(heap, need) + total_cost

            min_pool1 = pool1[0]
            min_pool2 = pool2[0]

            if min_pool1 <= min_pool2: # prio pool1
                total_cost += heapq.heappop(pool1)
                left_end += 1
                heapq.heappush(pool1, costs[left_end])
            else:
                total_cost += heapq.heappop(pool2)
                right_start -= 1
                heapq.heappush(pool2, costs[right_start])

            need -= 1
        
        return total_cost