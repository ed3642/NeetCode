from collections import deque

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        # kind of simulate the voting
        
        radiants = deque()
        dires = deque()

        order = 0 # keep track of voting order
        for vote in senate:
            if vote == 'R':
                radiants.append(order)
            else:
                dires.append(order)
            order += 1
        
        n = len(senate) # to keep track of rounds
        while radiants and dires:
            r_rep = radiants.popleft()
            d_rep = dires.popleft()
            if r_rep < d_rep:
                radiants.append(r_rep + n) # + n since itll be the next round
            else:
                dires.append(d_rep + n)
        
        return 'Radiant' if not dires else 'Dire'
            
