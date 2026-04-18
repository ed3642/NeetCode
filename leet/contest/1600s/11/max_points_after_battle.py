# https://leetcode.com/contest/biweekly-contest-134/problems/maximum-points-after-enemy-battles/
class Solution:
    def maximumPoints(self, enemyEnergies: list[int], currentEnergy: int) -> int:
        # must be a greedy algo
        n = len(enemyEnergies)
        l = 0
        r = n - 1

        enemyEnergies.sort()
        points = 0
        budget = currentEnergy
        while l <= r:
            if budget >= enemyEnergies[l]:
                farmed = budget // enemyEnergies[l]
                budget -= (enemyEnergies[l] * farmed)
                points += farmed
            elif points > 0:
                budget += enemyEnergies[r]
                r -= 1
            else:
                return points
        return points