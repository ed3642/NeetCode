# https://leetcode.com/problems/number-of-flowers-in-full-bloom/
from collections import defaultdict

class Solution:
    def fullBloomFlowers(self, flowers: list[list[int]], people: list[int]) -> list[int]:
        # classic line sweep problem

        OPEN = 0
        VIEW = 1
        CLOSE = 2
        N = len(people)
        res = [0] * N
        events = []

        for start, end in flowers:
            events.append((start, OPEN))
            events.append((end, CLOSE))
        for time in people:
            events.append((time, VIEW))

        events.sort()
        in_bloom = 0
        positions = defaultdict(int)

        for time, type in events:
            if type == OPEN:
                in_bloom += 1
            elif type == CLOSE:
                in_bloom -= 1
            else: # view
                positions[time] = in_bloom
        
        for i, time in enumerate(people):
            res[i] = positions[time]
        
        return res
