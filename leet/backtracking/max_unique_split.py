# https://leetcode.com/problems/split-a-string-into-the-max-number-of-unique-substrings/
class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        
        def max_split(start, seen: set):
            if start > len(s):
                return 0
            if start == len(s):
                return len(seen)
            
            best = 0
            for end in range(start + 1, len(s) + 1):
                substring = s[start:end]
                if substring not in seen:
                    # take or leave
                    take_seen = seen.copy()
                    take_seen.add(substring)
                    best = max(max_split(end, take_seen), best)
            return best
        
        return max_split(0, set())

    # this doesnt work. There is a case when taking a substr we havnt seen is not optimal
    def maxUniqueSplit(self, s: str) -> int:
        
        substrings = set()
        start = 0
        for end in range(1, len(s) + 1):
            substring = s[start:end]
            if substring not in substrings:
                substrings.add(substring)
                start = end
        return len(substrings)
    
s = Solution()
print(s.maxUniqueSplit("wwwzfvedwfvhsww"))