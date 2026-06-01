# https://leetcode.com/problems/decode-ways

from functools import lru_cache

class Solution:
    def numDecodings(self, s: str) -> int:

        # 000: -
        # 200: -
        # 022: -
        # 202: 20 2
        # 220: 2 20
        # 223: 2 2 3, 22 3, 2 23

        n = len(s)
        # check inputs are valid
        if n == 0: return 0
        if s[0] == '0': return 0

        # dp[i] num of ways to make arrangements from a str len i
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        #dp[2] = dp[1] + 1 if s[1] != '0' else dp[1]

        # l = length 
        for l in range(2, n + 1):
            if s[l-1] != '0': # 1 digit in range [1, 9]
                dp[l] += dp[l-1]
            if 10 <= int(s[l-2:l]) <= 26: # 2 digits in range [10, 26]
                dp[l] += dp[l-2]

        return dp[n]
    
    def numDecodings(self, s: str) -> int:
        # memory optimization
        if s[0] == '0':
            return 0
        
        mappings = set([str(i) for i in range(1, 27)])
        n = len(s)
        prev_state_1 = 1 # 1 step before
        prev_state_2 = 0 # 2 steps before

        for i in range(1, n + 1):
            state = 0
            group = s[i - 1:i]
            if group in mappings:
                state += prev_state_1
            if i != 1:
                expanded_group = s[i - 2:i]
                if expanded_group in mappings:
                    state += prev_state_2
            prev_state_2 = prev_state_1
            prev_state_1 = state

        return state

    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0
        
        mappings = set([str(i) for i in range(1, 27)])
        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1

        for i in range(1, n + 1):
            group = s[i - 1:i]
            if group in mappings:
                dp[i] += dp[i - 1]
            if i != 1:
                expanded_group = s[i - 2:i]
                if expanded_group in mappings:
                    dp[i] += dp[i - 2]

        return dp[n]
    
    def numDecodings(self, s: str) -> int:
        
        @lru_cache(maxsize=None)
        def dp(start, end):
            
            if end > len(s):
                return 0
            group = s[start:end + 1]
            if group not in mappings:
                return 0
            if end == len(s):
                return 1
            
            take_next = dp(start, end + 1)
            move_forward = dp(end + 1, end + 1)
            return take_next + move_forward

        mappings = set([str(i) for i in range(1, 27)])
        return dp(0, 0)