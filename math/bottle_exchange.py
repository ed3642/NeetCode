class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        
        drank = 0
        fulls = numBottles
        empties = 0
        drinking = True
        while numBottles >= numExchange:
            if drinking:
                drank += fulls
                empties += fulls
                drinking = False
            else:
                fulls = empties // numExchange
                empties = empties % numExchange
                numBottles = fulls + empties
                drinking = True
        
        return drank + fulls
