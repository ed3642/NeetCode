# https://leetcode.com/problems/maximum-candies-you-can-get-from-boxes

from collections import deque
from typing import List

class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        
        q = deque()
        found = 0
        potential_boxes = set()
        visited = [False] * len(status)

        # add initial open boxes and their keys
        for box in initialBoxes:
            if status[box] == 1:
                q.append(box)
            else:
                potential_boxes.add(box)

        while q:
            box = q.popleft()
            if visited[box]:
                continue
            visited[box] = True
            found += candies[box]
            for key in keys[box]:
                status[key] = 1
                if key in potential_boxes:
                    q.append(key)

            for nei_box in containedBoxes[box]:
                if not visited[nei_box]:
                    if status[nei_box] == 1:
                        q.append(nei_box)
                    else:
                        potential_boxes.add(nei_box)
        
        return found

