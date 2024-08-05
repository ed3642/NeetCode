# https://leetcode.com/problems/filling-bookcase-shelves
from functools import lru_cache

class Solution:

    def minHeightShelves(self, books: list[list[int]], shelfWidth: int) -> int:
        
        @lru_cache(maxsize=None)
        def min_height(i, level_h, level_w):

            if i >= len(books): 
                # found an answer, the total height it accumulated by the recursive calls
                return level_h
            
            # have to start new level
            if level_w + books[i][0] > shelfWidth:
                return min_height(i + 1, books[i][1], books[i][0]) + level_h # start new level

            # consider options
            if books[i][1] > level_h:
                return min(
                    min_height(i + 1, books[i][1], books[i][0]) + level_h, # start new level
                    min_height(i + 1, books[i][1], level_w + books[i][0]) # put bigger book in same level
                )
            
            # continue placing books on this level, the level_h doesnt change
            return min_height(i + 1, level_h, level_w + books[i][0])                

        self.min_height_seen = float('inf')

        return min_height(0, 0, 0)