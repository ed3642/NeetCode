from typing import List

class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        
        events = []
        OPEN = 0
        ARRIVE = 1
        CLOSE = 2

        for l, r in flowers:
            events.append((l, OPEN))
            events.append((r, CLOSE))
        for i, t in enumerate(people):
            events.append((t, ARRIVE, i)) # keep the index to know where to put it in the res

        events.sort()

        curr_open = 0
        res = [0] * len(people)
        placer_i = 0
        for i in range(len(events)):
            e_type = events[i][1]
            if e_type == OPEN:
                curr_open += 1
            elif e_type == CLOSE:
                curr_open -= 1
            else:
                res[events[i][2]] = curr_open
                placer_i += 1
        
        return res