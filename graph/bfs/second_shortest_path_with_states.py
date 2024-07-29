# https://leetcode.com/problems/second-minimum-time-to-reach-destination/
from collections import defaultdict, deque

class Solution:
    def secondMinimum(self, n: int, edges: list[list[int]], time: int, change: int) -> int:
        # can do bfs for shortest path since weights are all the same
        # NOTE: shows how to record more than just the shortests path, e.g second shortest
        # also deals with stop and go states with the time

        adj_list = defaultdict(list)

        for _from, _to in edges:
            adj_list[_from].append(_to)
            adj_list[_to].append(_from)

        queue = deque([(0, 1)]) # time taken, node
        times = defaultdict(set) # to store the first 2 shortest distances
        times[1] = set([0])

        while queue:
            curr_time, node = queue.popleft()

            if len(times[n]) == 2: # we found what we wanted
                break

            # calc candidate time
            state = (curr_time // change) % 2 # 0 -> go, 1 -> stop
            cand_time = curr_time
            if state == 0: # go
                cand_time = curr_time + time
            else: # stop
                cand_time = ((curr_time // change) + 1) * change + time # next multiple of change

            for nei in adj_list[node]:
                if len(times[nei]) < 2:
                    times[nei].add(cand_time)
                    queue.append((cand_time, nei))
            
        return max(times[n]) # has 2 times in it, fastest, and second fastest
    
