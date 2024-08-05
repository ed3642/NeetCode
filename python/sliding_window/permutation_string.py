from collections import Counter

class Solution:
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
        



s = Solution()

s1 = "ab"
s2 = "eidboooba"

print(s.checkInclusion(s1,s2))