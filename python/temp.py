from collections import Counter

class Solution:
    def minimumPushes(self, word: str) -> int:
        # 8 btns that can be mapped to
        # map in order of freq
        counts = sorted(Counter(word).items(), key=lambda x: -x[1])

        pushes = 0
        depth = 1
        mapping_to = 0 # index of button
        for _, f in counts:
            pushes += depth * f
            mapping_to += 1
            if mapping_to == 8:
                depth += 1
                mapping_to = 0
        
        return pushes