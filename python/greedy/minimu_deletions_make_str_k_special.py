# https://leetcode.com/problems/minimum-deletions-to-make-string-k-special

from collections import defaultdict

class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:

        # abbccc 1
        # bbccc
        
        freq = defaultdict(int)
        for c in word:
            freq[c] += 1
        
        min_removed = float('inf')
        for c1 in freq:
            removed = 0
            top_bound = freq[c1] + k
            bot_bound = freq[c1]
            for c2 in freq:
                if c1 != c2:
                    if freq[c2] < bot_bound:
                        removed += freq[c2]
                    elif freq[c2] > top_bound:
                        removed += freq[c2] - top_bound
            min_removed = min(removed, min_removed)

        return min_removed
    