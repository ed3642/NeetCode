# https://leetcode.com/problems/jump-game-iii

from collections import deque
from typing import List

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        
        n = len(arr)
        if arr[start] == 0:
            return True
        q = deque([start])
        visited = [False] * n
        visited[start] = True

        while q:
            for _ in range(len(q)):
                i = q.popleft()

                l = i - arr[i]
                r = i + arr[i]
                if 0 <= l < n and not visited[l]:
                    if arr[l] == 0:
                        return True
                    q.append(l)
                    visited[l] = True
                if 0 <= r < n and not visited[r]:
                    if arr[r] == 0:
                        return True
                    q.append(r)
                    visited[r] = True
            
        return False

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