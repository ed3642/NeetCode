from collections import defaultdict

class Solution:
    def countCompleteDayPairs(self, hours: list[int]) -> int:
        n  = len(hours)
        seen = defaultdict(int) # count of seen
        for i in range(n):
            hours[i] = hours[i] % 24
        
        pairs = 0
        for hour in hours:
            need = (24 - hour) % 24
            if need in seen:
                pairs += seen[need]
            seen[hour] += 1

        return pairs
    
    def countCompleteDayPairs2(self, hours: list[int]) -> int:
        
        n = len(hours)
        pairs = 0
        for end in range(1, n):
            for start in range(end):
                if (hours[start] + hours[end]) % 24 == 0:
                    pairs += 1
        
        return pairs
    
s = Solution()

print(s.countCompleteDayPairs([72,48,24,3]))