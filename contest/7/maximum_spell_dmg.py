from collections import Counter, defaultdict
from functools import lru_cache

class Solution:

    # nice solution
    def maximumTotalDamage(self, power: list[int]) -> int:
        # like delete and earn but we cant use i-2,i-1,i+1,i+2 when choosing i.
        # like delete and earn problem but we have to find the last valid state with a while loop
        freqs = Counter(power)
        spells = sorted(freqs.keys())
        n = len(spells)
        calc_total = lambda x: spells[x] * freqs[spells[x]]
        totals = list(map(calc_total, range(n)))
        max_dmg = [0] * (n + 1)

        for dp_i in range(1, n + 1):
            spell_i = dp_i - 1
            this_dmg = totals[spell_i]

            # find the last spell that was casted
            last_spell = spell_i - 1
            while (last_spell >= 0 and (
                spells[last_spell] == spells[spell_i] - 1 or
                spells[last_spell] == spells[spell_i] - 2
            )):
                last_spell -= 1
            
            # state transition
            last_spell_dp_i = last_spell + 1
            max_dmg[dp_i] = max(
                max_dmg[last_spell_dp_i] + this_dmg, # take
                max_dmg[dp_i - 1] # leave
            )
        
        return max_dmg[n]

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