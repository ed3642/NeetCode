# https://leetcode.com/problems/check-if-number-is-a-sum-of-powers-of-three

class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        # like building the binary represention of a number but in base 3

        while n > 0:
            if n % 3 >= 2: # need 2 or more of this digit base 3 (only 0 or 1)
                return False
            n //= 3
        return True

    def checkPowersOfThree(self, n: int) -> bool:
        # pick out the biggest power of 3 

        threes = []
        num = 1
        while num <= n:
            threes.append(num)
            num *= 3
        
        i = len(threes) - 1
        while n > 0 and i >= 0:
            if threes[i] <= n:
                n -= threes[i]
            i -= 1
        
        return n == 0