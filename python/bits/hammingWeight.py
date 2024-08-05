class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n > 0:
            count += n % 2
            n = n >> 1
        return count
    
    def hammingWeight5Head(self, n: int) -> int:
        count = 0
        while n > 0:
            count += 1
            n = n & (n - 1)
        return count