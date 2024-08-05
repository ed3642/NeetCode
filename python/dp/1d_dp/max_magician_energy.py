from functools import lru_cache

class Solution:
    def maximumEnergy(self, energy: list[int], k: int) -> int:
        
        # we just have to pick the best starting point
        n = len(energy)
        max_e = [-float('inf')] * n

        for i in range(n - 1, -1, -1):
            last_pos = i + k
            last_val = 0
            if last_pos < n:
                last_val = max_e[last_pos]
            
            max_e[i] = energy[i] + last_val
        
        return max(max_e)
