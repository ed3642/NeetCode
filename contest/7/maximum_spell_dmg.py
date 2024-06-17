from collections import Counter, defaultdict
from functools import lru_cache

class Solution:

    # nice solution
    # like delete and earn but we cant use i-2,i-1,i+1,i+2 when choosing i.
    def maximumTotalDamage(self, power: list[int]) -> int:
        calc_total = lambda i: spells[i] * freqs[spells[i]]

        freqs = Counter(power)
        spells = sorted(freqs.keys())
        n = len(spells)

        # Add an initial state to represent the empty spell
        max_dmg = [0] * (n + 1)
        max_dmg[1] = calc_total(0)

        for i in range(2, n + 1):
            this_dmg = calc_total(i - 1)

            # get the last valid spell
            prev_spell = i - 1
            while (prev_spell > 0 and 
                   (spells[prev_spell - 1] == spells[i - 1] - 1 or
                    spells[prev_spell - 1] == spells[i - 1] - 2)):
                prev_spell -= 1
            
            # transition
            max_dmg[i] = max(
                max_dmg[i - 1],  # leave
                max_dmg[prev_spell] + this_dmg  # take
            )

        return max_dmg[-1]

    # this uses too much memory
    def maximumTotalDamage(self, power: list[int]) -> int:
        
        @lru_cache(maxsize=None)
        def max_power(num):
            if num == 0:
                return 0
            if num == 1:
                return totals[1]
            if num == 2:
                return max(totals[1], totals[2])
            
            return max(
                max_power(num - 3) + totals[num],
                max_power(num - 2),
                max_power(num - 1)
            )

        totals = defaultdict(int)
        _max = 0

        for val in power:
            totals[val] += val
            _max = max(_max, val)

        return max_power(_max)
    
s = Solution()
print(s.maximumTotalDamage([2,1,2,3,3,1,4,4]))