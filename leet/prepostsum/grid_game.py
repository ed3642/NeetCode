# https://leetcode.com/problems/grid-game
from typing import List

class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        
        # note maximizing robot1s path does not minimize robots2 path
        # think of it as path1 splits the grid and now we have to minimize the top right and bot left group sums
        # [0,0,0,0,x1,x2,x3...]
        # [y1,y2,y3...,0,0,0]
        # where positon of last y = pos of first x - 2 
        # [0  , 0, 100]
        # [100, 0, 0  ]

        J_BOUNDARY = len(grid[0])
        top_right_sum = sum(grid[0])
        bot_left_sum = 0
        robot_2_max = float('inf')

        for j in range(J_BOUNDARY):
            top_right_sum -= grid[0][j]
            robot_2_max = min(max(top_right_sum, bot_left_sum), robot_2_max)
            bot_left_sum += grid[1][j]

        return robot_2_max
    