from collections import Counter 

class Solution:
    # O(n k)
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:

        counts = dict()

        for s in strs:
            sorted_char_counts = [0] * 26
            for c in s:
                sorted_char_counts[ord(c) - ord('a')] += 1
            hash = tuple(sorted_char_counts)
            if hash in counts:
                counts[hash].append(s)
            else:
                counts[hash] = [s]

        return list(counts.values())

    # O(n k log k)
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        sets = dict()

        for str in strs:
            tokens = tuple(sorted(str))
            if tokens in sets:
                sets[tokens].append(str)
            else:
                sets[tokens] = [str]

        return list(sets.values())
        
    # O(n k), top one is still better than this in practice due to overhead
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        
        counts = dict()

        for s in strs:
            hash = frozenset([(key, val) for key, val in Counter(s).items()])

            if hash not in counts:
                counts[hash] = [s]
            else:
                counts[hash].append(s)
        
        return list(counts.values())