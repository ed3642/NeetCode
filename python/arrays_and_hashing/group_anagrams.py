class Solution:
    # O(n)
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        sets = dict()

        for str in strs:
            tokens = tuple(sorted(str))
            if tokens in sets:
                sets[tokens].append(str)
            else:
                sets[tokens] = [str]

        return list(sets.values())
        