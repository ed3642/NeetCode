from collections import Counter

class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        
        # count non-matching pairs
        # apply the base cases to them

        n = len(s1)
        total = 0
        x_y = 0 # x in s1 and y in s2, count
        y_x = 0 # vice versa

        for i in range(n):
            c1 = s1[i]
            c2 = s2[i]
            if c1 == c2:
                continue
            
            if c1 == 'x' and c2 == 'y':
                x_y += 1
            else:
                y_x += 1
        
        # can think of it as using up the height of 2 towers now
        tower1, tower2 = x_y, y_x

        # apply cheapest case (1) as many times
        # from tower1
        available = tower1 // 2
        total += available
        tower1 -= available * 2
        # from tower2
        available = tower2 // 2
        total += available
        tower2 -= available * 2
        
        # if one of the towers is not 1 or 0 tall
        if tower1 != tower2:
            return -1
        
        # apply case 2, remaining tower height
        if tower1 == 1:
            total += 2

        return total


