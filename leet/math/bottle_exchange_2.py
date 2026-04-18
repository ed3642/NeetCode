# https://leetcode.com/problems/water-bottles-ii

class Solution:

    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        
        drank = 0
        empty = 0

        while numBottles > 0 or (numBottles + empty) > numExchange:
            drank += numBottles
            empty += numBottles

            # exchange bottles
            numBottles = 0
            while empty >= numExchange:
                numBottles += 1
                empty -= numExchange
                numExchange += 1

        return drank