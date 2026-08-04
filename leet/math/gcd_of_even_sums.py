class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        # observe that gcd(n, n+1) = 1 since consecutive ints are coprime
        return n

    def gcdOfOddEvenSums(self, n: int) -> int:
        
        def gcd(a, b):
            if a == 0:
                return b
            return gcd(b%a, a)

        evens = n*(n+1)
        odds = n**2

        return gcd(evens, odds)