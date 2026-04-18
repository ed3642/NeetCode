# https://leetcode.com/problems/find-the-punishment-number-of-an-integer/
class Solution:
    def punishmentNumber(self, n: int) -> int:
        
        def can_partition(sqr, num, start):
            if start == len(sqr) and num == 0:
                return True
            if num < 0 or start >= len(sqr):
                return False
            
            for i in range(start, len(sqr)):
               # partition from [start:i)
               if can_partition(sqr, num - int(sqr[start:i + 1]), i + 1):
                   return True

            return False

        punish_num = 0
        for i in range(1, n + 1):
            sqr = i * i
            # number theory prune with the modulos and bt
            # casting out nines modulo property
            if (i % 9 == 0 or i % 9 == 1) and can_partition(str(sqr), i, 0):
                punish_num += sqr
        
        return punish_num
    