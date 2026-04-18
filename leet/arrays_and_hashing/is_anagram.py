from collections import Counter

class Solution:
    # frequency dict of each letter
    # O(n)
    def isAnagram(self, s: str, t: str) -> bool:
        dictA = dict()
        dictB = dict()

        for c in s:
            if not dictA.get(c):
                dictA[c] = 1
            else:
                dictA[c] += 1
        
        for c in t:
            if not dictB.get(c):
                dictB[c] = 1
            else:
                dictB[c] += 1
            
        return dictA == dictB
    
    # python way
    # much faster and easier
    def isAnagram2(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
    
s = Solution()

s1 = 'ab'
s2 = 'a'

print(s.isAnagram(s1, s2))