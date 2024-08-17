from collections import Counter 

class Solution:
    def minimumOperationsToMakeKPeriodic(self, word: str, k: int) -> int:
        # segment the string into chunks size k
        # count freq of chunks
        # sum all the chunks freq less than the max

        n = len(word)
        segments = []

        i = 0
        while i < n:
            segments.append(word[i:i + k])
            i += k

        freqs = Counter(segments)
        most_common = 0
        for freq in freqs.values():
            most_common = max(most_common, freq)

        return len(segments) - most_common


