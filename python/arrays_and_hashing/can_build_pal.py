# https://leetcode.com/problems/construct-k-palindrome-strings
from collections import Counter

class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        
        if len(s) < k:
            return False 
        
        counts = Counter(s)

        even_pairs = 0
        even_pair_count = 0
        # all evens can be canceled out
        odds = 0
        for c in counts:
            mod_count = counts[c] % 2
            even_pair_count += counts[c] // 2
            if mod_count == 0:
                even_pairs += 1
            else:
                odds += 1
            counts[c] = mod_count

        if odds > k:
            return False
        # how many pals if we use excess even pairs to make more odds
        need = k - (even_pair_count * 2 + odds)
        if need > 0:
            return False

        return True
