from collections import Counter

class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        freqs = Counter(arr)
        freqs_set = set()

        for f in freqs.values():
            if f in freqs_set:
                return False
            freqs_set.add(f)
        
        return True