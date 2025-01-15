# https://leetcode.com/problems/word-subsets
from collections import Counter
from typing import List

class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:

        counts1 = [Counter(word) for word in words1]
        words2_super_count = Counter()

        for word2 in words2:
            new_count = Counter(word2)
            for c, count in new_count.items():
                if count > words2_super_count[c]:
                    words2_super_count[c] = count

        res = []
        for i in range(len(words1)):
            is_valid = True
            word1_count = counts1[i]
            for c, count in words2_super_count.items():
                if word1_count[c] < words2_super_count[c]:
                    is_valid = False
                    break
            if is_valid:
                res.append(words1[i])

        return res