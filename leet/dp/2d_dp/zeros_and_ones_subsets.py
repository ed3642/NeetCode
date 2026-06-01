# https://leetcode.com/problems/ones-and-zeroes

from collections import Counter, defaultdict
from typing import List

class Solution:
    def findMaxForm(self, strs: List[str], n: int, m: int) -> int:
        # good problem make sure we iterate over the right directions
        
        # dp[i][j] = sets that have atleast i zeros and j ones 
        num_strs = len(strs)
        dp = [[0 for _ in range(m+1)] for _ in range(n+1)]

        zeros = defaultdict(int)
        ones = defaultdict(int)

        for i, s in enumerate(strs):
            counts = Counter(s)
            zeros[i] = counts['0']
            ones[i] = counts['1']
        
        for k in range(num_strs): # propagates valid states using first k strings
            # iterate only though valid states hence the n-zeros[k] and m-ones[k]
            for i in range(n-zeros[k], -1, -1):
                for j in range(m-ones[k], -1, -1):
                    nexti = i+zeros[k]
                    nextj = j+ones[k]
                    dp[nexti][nextj] = max(dp[i][j]+1, dp[nexti][nextj])
        
        return dp[n][m]
