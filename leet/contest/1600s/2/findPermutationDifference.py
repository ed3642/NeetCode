from collections import defaultdict

class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        
        dict_s = defaultdict(int)
        dict_t = defaultdict(int)

        for i in range(len(s)):
            ch = s[i]
            dict_s[ch] = i
        
        for i in range(len(t)):
            ch = t[i]
            dict_t[ch] = i

        total = 0
        for ch in s:
            total += abs(dict_s[ch] - dict_t[ch])

        return total