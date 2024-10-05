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
