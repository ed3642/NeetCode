from functools import lru_cache


class Solution:
    def maxEnergyBoost(self, energyDrinkA: list[int], energyDrinkB: list[int]) -> int:
        
        @lru_cache(maxsize=None)
        def max_energy(i, state):
            if i >= N:
                return 0
            
            continue_drinking = 0
            if state == 0:
                continue_drinking = energyDrinkA[i]
            else:
                continue_drinking = energyDrinkB[i]

            return max(
                max_energy(i + 1, state) + continue_drinking,
                max_energy(i + 1, (state ^ 1)) # change
            )


        N = len(energyDrinkA)
        return max(max_energy(0, 0), max_energy(0, 1))