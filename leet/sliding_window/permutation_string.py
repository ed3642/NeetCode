# https://leetcode.com/problems/permutation-in-string/description/
from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        countsA = Counter(s1)
        countsB = Counter(s2)

        # check if its possible
        for ch in countsA:
            if countsA[ch] > countsB[ch]:
                return False
        
        # check if it happens
        N = len(s1)
        curr_count = Counter(s2[:N])
        if curr_count == countsA:
            return True
        for end in range(N, len(s2)):
            ch_end = s2[end]
            ch_start = s2[end - N]
            curr_count[ch_end] += 1
            curr_count[ch_start] -= 1
            if curr_count[ch_start] == 0:
                del curr_count[ch_start]
            if curr_count == countsA:
                return True
        
        return False

    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        n1 = len(s1)
        n2 = len(s2)
        target_counter = Counter()
        window_counter = Counter()

        # counter of s1
        for c in s1:
            target_counter[c] += 1

        # build the initial window of size n1 in s2
        l = 0
        r = 0

        while r < n1:
            c = s2[r]
            window_counter[c] += 1
            r += 1

        # slide window along s2 and see if it matches counter1
        while r < n2:
            if target_counter == window_counter: return True

            to_remove = s2[l]
            to_add = s2[r]
            l += 1
            r += 1

            window_counter[to_remove] -= 1
            window_counter[to_add] += 1
        
        return True if target_counter == window_counter else False 
        