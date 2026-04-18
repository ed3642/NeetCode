from collections import Counter

class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        
        substrings = 0

        for end in range(1, len(s) + 1):
            for start in range(end):
                sub_s = s[start:end]
                counts = Counter(sub_s)
                if counts['0'] <= k or counts['1'] <= k:
                    substrings += 1

        return substrings
    