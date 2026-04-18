# https://leetcode.com/problems/successful-pairs-of-spells-and-potions

import bisect
from collections import Counter
from itertools import accumulate
import math
from typing import List

class Solution:

    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:

        N = len(spells)
        M = len(potions)
        res = [0] * N

        freqs = Counter(potions)
        max_potion_power = max(freqs.keys())
        counts = [0] * (max_potion_power + 1)
        for val, f in freqs.items():
            counts[val] = f
        pf_sum = list(accumulate(counts))

        for i, spell_power in enumerate(spells):
            # equivalent by integer division is better
            min_potion_power = (success + spell_power - 1) // spell_power # math.ceil(success / spell_power)
            if min_potion_power <= max_potion_power:
                if min_potion_power > 0:
                    res[i] = pf_sum[max_potion_power] - pf_sum[min_potion_power - 1]
                else:
                    res[i] = pf_sum[max_potion_power]
        
        return res

    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:

        def bin_search(spell_power):
            
            def is_valid(i):
                return potions[i] * spell_power >= success

            l = 0
            r = M - 1

            if not is_valid(r): # all fail
                return M

            while l < r:
                m = (l + r) // 2
                if is_valid(m):
                    r = m
                else:
                    l = m + 1
            
            return l

        N = len(spells)
        M = len(potions)
        res = [0] * N
        memo = {}

        potions.sort()

        for i in range(N):
            first_valid_i = M
            if spells[i] not in memo:
                first_valid_i = bin_search(spells[i])
            else:
                first_valid_i = memo[spells[i]]
            res[i] = M - first_valid_i

        return res
    
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