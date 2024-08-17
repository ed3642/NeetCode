from collections import Counter
from functools import reduce

class Solution:
    def minAnagramLength(self, s: str) -> int:
        def gcd(a, b):
            if a == 0:
                return b
            
            return gcd(b % a, a)
        
        counts = Counter(s)

        # the gcd of all the frequencies, the length of the word that is the basis for s
        times_to_repeat = reduce(gcd, counts.values())

        return len(s) // times_to_repeat
