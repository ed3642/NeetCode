import heapq
from collections import Counter
from collections import defaultdict

class Solution:
    # can improve space complexity
    def leastInterval(self, tasks: list[str], n: int) -> int:
        def fill_heap():
            task_types = list(hm_types.keys())
            for task_type in task_types:
                heapq.heappush(heap, task_type)
                hm_types[task_type] -= 1
                if hm_types[task_type] == 0:
                    del hm_types[task_type]

        heap = []
        idle_time = 0

        hm_types = defaultdict(int)
        for t in tasks:
            hm_types[t] += 1

        while len(hm_types) > 0:
            fill_heap()
            for i in range(n + 1):
                if heap:
                    heapq.heappop(heap)
                else:
                    if len(hm_types) > 0:
                        idle_time += 1

        return len(tasks) + idle_time
    
    # better space complexity
    def leastInterval2(self, tasks: list[str], n: int) -> int:
        tasks_types = Counter(tasks)
        heap = [-count for count in tasks_types.values()]
        heapq.heapify(heap)
        idle_time = 0

        while heap:
            next_tasks = [] # tasks to put back in the heap
            for _ in range(n + 1):
                if heap:
                    cycles = -heapq.heappop(heap) # most frequent task
                    if cycles > 1:
                        next_tasks.append(-(cycles - 1)) # cycles remaining
                elif next_tasks:
                    idle_time += 1
                elif not heap and not next_tasks:
                    break
            for task_cycles_rem in next_tasks:
                heapq.heappush(heap, task_cycles_rem)

        return len(tasks) + idle_time
    
    # voodo greedy algorithm
    def leastInterval(self, tasks: list[str], n: int) -> int:
        counter = Counter(tasks)
        max_count = max(counter.values())
        min_time = (
                (max_count - 1) * (n + 1) + 
                sum(map(lambda count: count == max_count, counter.values())))
    
        return max(min_time, len(tasks))