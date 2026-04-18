# https://leetcode.com/problems/check-if-grid-can-be-cut-into-sections

from typing import List

class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:

        def check_axis(axis):
            # add artificial open on axis end since we cant split there
            axis.sort()
            current_open = 0
            spaces = 0

            for _, e_type in axis:
                if e_type == OPEN:
                    current_open += 1
                else:
                    current_open -= 1
                if current_open == 0:
                    spaces += 1
                    if spaces >= 3: # can split 
                        return True
            return False
        
        # close before open
        CLOSE = 0
        OPEN = 1

        x_axis = []
        y_axis = []
        for x1, y1, x2, y2 in rectangles:
            x_axis.append((x1, OPEN))
            x_axis.append((x2, CLOSE))
            y_axis.append((y1, OPEN))
            y_axis.append((y2, CLOSE))

        if check_axis(x_axis):
            return True
        if check_axis(y_axis):
            return True
        return False
