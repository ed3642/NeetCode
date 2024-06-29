# https://leetcode.com/problems/hand-of-straights
from collections import Counter
class Solution:
    def isNStraightHand(self, hand: list[int], groupSize: int) -> bool:
        # each card must be in a hand so we can greedily build the hands from smallest to biggest

        # case where we can never build the hands
        n = len(hand)
        if n % groupSize != 0:
            return False
        
        counts = Counter(hand)
        cards = sorted(counts.keys())

        for card in cards:
            while counts[card] > 0: # move onto next card when depleted
                # build hand by reducing count by 1
                for i in range(groupSize):
                    pos = card + i
                    if counts[pos] <= 0:
                        return False
                    counts[pos] -= 1
        return True

    def isNStraightHand(self, hand: list[int], groupSize: int) -> bool:
        # look at each group 
        n = len(hand)
        if n % groupSize != 0:
            return False

        hm = dict()
        hand.sort()

        for val in hand:
            if val not in hm:
                hm[val] = 1
            else:
                hm[val] += 1
        
        for lowest, count in hm.items():
            if count <= 0:
                continue
            for i in range(groupSize):
                num_needed = lowest + i
                if num_needed not in hm:
                    return False
                hm[num_needed] -= count
                if hm[num_needed] < 0:
                    return False

        return True