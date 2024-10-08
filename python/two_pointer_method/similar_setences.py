# https://leetcode.com/problems/sentence-similarity-iii/
class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        
        words1 = sentence1.split(' ')
        words2 = sentence2.split(' ')
        if len(words1) > len(words2):
            words1, words2 = words2, words1

        l1 = 0
        r1 = len(words1) - 1
        l2 = 0
        r2 = len(words2) - 1

        while l2 <= r2:
            if words1[l1] == words2[l2]:
                l1 += 1
                l2 += 1
            elif words1[r1] == words2[r2]:
                r1 -= 1
                r2 -= 1
            else:
                return False
            if l1 > r1:
                return True
        
        return False
    