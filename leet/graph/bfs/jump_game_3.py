# https://leetcode.com/problems/jump-game-iii
from collections import deque
from typing import List

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:

        I_BOUNDARY = len(arr)
        visited = [False] * I_BOUNDARY

        q = deque([start])
        while q:
            for _ in range(len(q)):
                node = q.popleft()

                for nei in [node - arr[node], node + arr[node]]:
                    if 0 <= nei < I_BOUNDARY and not visited[nei]:
                        if arr[nei] == 0:
                            return True
                        q.append(nei)
                        visited[nei] = True
        
        return False