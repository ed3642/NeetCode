class Solution:
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