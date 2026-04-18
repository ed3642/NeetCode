class Solution:
    def numberOfChild(self, n: int, k: int) -> int:
        
        moves = 0
        pos = 0
        delta = -1
        while moves < k:
            if pos == n - 1 or pos == 0:
                delta *= -1
            pos += delta
            moves += 1
        
        return pos

s = Solution()
print(s.numberOfChild(3, 5))