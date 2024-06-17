from collections import Counter
from functools import lru_cache

class Solution:

    def maximumTotalDamage(self, power: list[int]) -> int:
        
        freqs = Counter(power)
        spells = sorted(freqs.keys())
        n = len(spells)
        totals = [0] * (n + 1)
        for spell in range(n):
            totals[spell] = spells[spell] * freqs[spells[spell]]
        
        max_dmg = [0] * (n + 1)
        max_dmg[0] = 0
        max_dmg[1] = totals[0]
        for i in range(2, n + 1):
            spell = i - 1 # index is shifted by 1
            this_dmg = totals[spell]

            last_spell = spell - 1
            while (last_spell >= 0 and 
                   (spells[last_spell] == spells[spell] - 1 or
                    spells[last_spell] == spells[spell] - 2)
            ):
                last_spell -= 1
            
            max_dmg[i] = max(
                max_dmg[i - 1],
                max_dmg[last_spell + 1] + this_dmg
            )
        
        return max_dmg[n]
