# https://leetcode.com/problems/construct-the-lexicographically-largest-valid-sequence
from typing import List

class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        
        def find_first(seq, options, placer_i):
            nonlocal res

            if not options:
                res = seq.copy()
                return True
            
            if seq[placer_i] != 0:
                return find_first(seq, options, placer_i + 1)

            for _max in sorted(options, reverse=True):
                found = False
                if _max == 1:
                    seq[placer_i] = _max
                    options.remove(_max)
                    found |= find_first(seq, options, placer_i + 1)
                    seq[placer_i] = 0
                    options.add(_max)
                else:
                    if placer_i + _max >= len(seq) or seq[placer_i + _max] != 0:
                        continue
                    seq[placer_i] = _max
                    seq[placer_i + _max] = _max
                    options.remove(_max)
                    found |= find_first(seq, options, placer_i + 1)
                    seq[placer_i] = 0
                    seq[placer_i + _max] = 0
                    options.add(_max)
                if found:
                    return True
            return False

        if n == 1:
            return [1]
        length = (n - 1) * 2 + 1
        options = set([i for i in range(1, n + 1)])
        res = None
        find_first([0] * length, options, 0)
        return res
