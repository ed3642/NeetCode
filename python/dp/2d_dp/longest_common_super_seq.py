# https://leetcode.com/problems/shortest-common-supersequence/

from functools import lru_cache

class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        
        # find LCS in str1 and then str2 then build the superseq until the strings are depleted
        # attach the remaining strings if unmatched from shared
        # abac   str1
        # cab    str2
        # ab     (LCS)
        # cabac

        @lru_cache(maxsize=None)
        def LCS(i1, i2):
            if i1 == len(str1) or i2 == len(str2):
                return ''
            
            if str1[i1] == str2[i2]:
                return str1[i1] + LCS(i1 + 1, i2 + 1)

            op1 = LCS(i1, i2 + 1)
            op2 = LCS(i1 + 1, i2)

            if len(op1) > len(op2):
                return op1
            return op2


        shared = LCS(0, 0)

        res = []
        i1 = 0
        i2 = 0

        for c in shared:
            # add mismatches from str1
            while str1[i1] != c:
                res.append(str1[i1])
                i1 += 1

            # add mismatches from str2
            while str2[i2] != c:
                res.append(str2[i2])
                i2 += 1
            
            # add the match itself
            res.append(c)
            # start from the next c from matched
            i1 += 1
            i2 += 1
        
        # add remaining chars
        res.append(str1[i1:])
        res.append(str2[i2:])

        return ''.join(res)
    