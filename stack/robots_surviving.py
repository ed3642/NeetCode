# https://leetcode.com/problems/robot-collisions/description/
class Solution:
    def survivedRobotsHealths(self, positions: list[int], healths: list[int], directions: str) -> list[int]:

        def faceOf(r1, r2):
            if healths[r1] > healths[r2]:
                if healths[r1] == 1:
                    return None
                healths[r1] -= 1
                return r1
            elif healths[r1] < healths[r2]:
                if healths[r2] == 1:
                    return None
                healths[r2] -= 1
                return r2
            return None
        
        n = len(positions)
        robots = list(map(list, zip(positions, range(n)))) # last is the robots index
        robots.sort(key=lambda x: x[0]) # sort by positions

        stack = []
        winners = []
        for _, i in robots:
            if directions[i] == 'R':
                stack.append(i)
            else: # robot going left
                while stack:
                    winner = faceOf(stack[-1], i)
                    if winner == None: # both die
                        stack.pop() 
                        break 
                    elif winner == stack[-1]: # look for next left-going
                        break
                    else: # robot going left wins, next oponent
                        stack.pop()
                else: # no opponent, will go untouched to the left
                    winners.append([i, healths[i]])
        
        for winner in stack:
            winners.append([winner, healths[winner]])
        
        winners.sort(key=lambda x: x[0])
        return [winner[1] for winner in winners]
    