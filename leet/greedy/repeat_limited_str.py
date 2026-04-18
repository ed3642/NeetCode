# https://leetcode.com/problems/construct-string-with-repeat-limit
from collections import Counter

class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        
        counts = Counter(s)
        letter_prio = sorted(counts.keys(), reverse=True)
        prio_i = 0
        streak = 0
        res = []

        while True:
            if counts[letter_prio[prio_i]] == 0:
                # will have to do this at most 26 times
                letter_prio.remove(letter_prio[prio_i])
                if not letter_prio:
                    break
                streak = 0
                if prio_i >= len(letter_prio):
                    prio_i -= 1
            if streak >= repeatLimit:
                temp = (prio_i + 1) % len(letter_prio)
                if temp == prio_i:
                    break
                res.append(letter_prio[temp])
                counts[letter_prio[temp]] -= 1
                if counts[letter_prio[temp]] == 0:
                    letter_prio.remove(letter_prio[temp])
                streak = 0
            streak += 1
            c = letter_prio[prio_i]
            counts[letter_prio[prio_i]] -= 1
            res.append(c)
        
        return ''.join(res)
    
s = Solution()
print(s.repeatLimitedString("cczazcc", 3))