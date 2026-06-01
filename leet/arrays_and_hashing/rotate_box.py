# https://leetcode.com/problems/rotating-the-box/
from collections import deque
from typing import List

class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        # could do the shifting of the stones more efficient with 2 pointer instead
        
        STONE = '#'
        WALL = '*'
        EMPTY = '.'
        n = len(boxGrid[0])

        for row in boxGrid:
            stones = 0
            for i in range(n):
                if row[i] == WALL:
                    for j in range(i - 1, i - 1 - stones, -1):
                        row[j] = STONE
                    stones = 0
                elif row[i] == STONE:
                    row[i] = EMPTY
                    stones += 1
            for j in range(n - 1, n - 1 - stones, -1):
                row[j] = STONE
        
        return list(zip(*reversed(boxGrid)))

    # could have just done it with 2 pointers instead of queue
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:

        # rotate matrix 90 degrees clockwise
        res = [list(row) for row in zip(*reversed(box))]

        MAX_I = len(res)
        MAX_J = len(res[0])
        q = deque()

        # make items fall down in each col
        for j in range(MAX_J):
            q.clear()
            for i in range(MAX_I - 1, -1, -1):
                if res[i][j] == '.':
                    q.append(i)
                elif res[i][j] == '#':
                    if not q:
                        # no space for item
                        continue
                    res[i][j] = '.'
                    res[q.popleft()][j] = '#'
                    q.append(i) # this spot is now free
                else: # an obstacle blocks off all prev possibilities
                    q.clear()
    
        return res
    