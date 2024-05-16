import math
import bisect

class Solution:
    # better
    # bisect left does exactly what bin_search first occurence needs to do
    def successfulPairs(self, spells: list[int], potions: list[int], success: int) -> list[int]:
        potions.sort()
        n = len(spells)
        m = len(potions)
        res = [0] * n

        for i, spell in enumerate(spells):
            need = math.ceil(success / spell)
            if potions[-1] >= need:
                index_of_first_success = bisect.bisect_left(potions, need)
                res[i] = m - index_of_first_success
        
        return res
    
    def successfulPairs2(self, spells: list[int], potions: list[int], success: int) -> list[int]:

        # return first occurence of target or first index that is greater than target
        def binary_search(arr, target):
            l = 0
            r = len(arr) - 1

            while l < r:
                m = (l + r) // 2
                if target > arr[m]:
                    l = m + 1
                else:
                    r = m
            
            if arr[l] < target and l < len(arr) - 1:
                # this is the first occurence greater than target
                # l could be less than the target
                return l + 1 
            return l if arr[l] >= target else len(arr) - 1 # return last index if target not found

        potions.sort()
        n = len(spells)
        m = len(potions)
        res = [0] * n

        for i, spell in enumerate(spells):
            need = math.ceil(success / spell)
            if potions[-1] >= need:
                index_of_first_success = binary_search(potions, need)
                res[i] = m - index_of_first_success
        
        return res