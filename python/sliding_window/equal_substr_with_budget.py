class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        
        l = 0
        r = 0
        n = len(s)
        budget = maxCost
        max_len = 0
        costs = [0] * n

        for i in range(len(costs)):
            if s[i] != t[i]:
                costs[i] = abs(ord(s[i]) - ord(t[i]))

        while r < n:
            cost = costs[r]
            if budget >= cost:
                budget -= cost
                length = r - l + 1
                max_len = max(max_len, length)
                r += 1
            else:
                refund = costs[l]
                budget += refund
                l += 1

        return max_len
            