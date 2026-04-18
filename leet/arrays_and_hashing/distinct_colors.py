# https://leetcode.com/problems/find-the-number-of-distinct-colors-among-the-balls/
from collections import defaultdict
from typing import List

class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        
        i_to_color = {}
        colors_used = defaultdict(int)
        
        distinct = 0
        res = [0] * len(queries)
        for query_i, (color_i, color) in enumerate(queries):
            if color_i not in i_to_color:
                # new color
                colors_used[color] += 1
                if colors_used[color] == 1:
                    distinct += 1
            elif color_i in i_to_color:
                prev_color = i_to_color[color_i]
                # removed all of a color
                colors_used[prev_color] -= 1
                if colors_used[prev_color] == 0:
                    distinct -= 1
                # new color
                colors_used[color] += 1
                if colors_used[color] == 1:
                    distinct += 1
            i_to_color[color_i] = color
            res[query_i] = distinct
        
        return res
