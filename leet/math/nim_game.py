# https://leetcode.com/problems/nim-game/

class Solution:
    def canWinNim(self, n: int) -> bool:
        # i go first

        if n % 4 == 0:
            return False

        return True
        
