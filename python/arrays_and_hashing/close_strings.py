from collections import Counter

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # get the frequencies of the frequencies
        # they should be the same
        # also the sets should be the same

        if set(word1) != set(word2):
            return False

        freqs_A = Counter(Counter(word1).values())
        freqs_B = Counter(Counter(word2).values())

        if freqs_A != freqs_B:
            return False

        return True