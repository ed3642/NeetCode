class Solution:
    def maxSatisfied(self, customers: list[int], grumpy: list[int], minutes: int) -> int:
        # sliding window, keep track of bonus satisfied customers
        # want window with max bonus satisfied customers

        l = 0
        r = 0
        bonus_satisfied = 0
        total_satisfied = 0

        # build initial windown
        while r < minutes:
            if grumpy[r] == 0:
                total_satisfied += customers[r]
            else:
                bonus_satisfied += customers[r]
            r += 1
        max_bonus = bonus_satisfied
        
        # slide
        while r < len(customers):
            if grumpy[r] == 0:
                total_satisfied += customers[r]
            else:
                bonus_satisfied += customers[r]
            if grumpy[l] == 1: # push out of window
                bonus_satisfied -= customers[l]
            l += 1
            r += 1
            max_bonus = max(max_bonus, bonus_satisfied)
        
        return total_satisfied + max_bonus