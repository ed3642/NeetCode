# https://leetcode.com/problems/count-and-say

class Solution:
    def countAndSay(self, n: int) -> str:

        # 11121

        def rle(string: str):
            if len(string) == 1:
                return '1' + string
            if string in memo:
                return memo[string]
            
            string = string + '#' # act as stopper
            N = len(string)
            i = 0
            prev_i = 0
            res = []
            while i < N - 1:
                while i < N and string[i] == string[i + 1]:
                    i += 1
                res.append(str(i - prev_i + 1))
                res.append(str(string[prev_i]))
                i += 1
                prev_i = i
            memo[string] = ''.join(res)
            return memo[string]
        
        def cas(num):
            if num == 1:
                return '1'
            
            return rle(cas(num - 1))
        
        memo = {}
        
        return ''.join(cas(n))
    