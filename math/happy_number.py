class Solution:
    def isHappy(self, n: int) -> bool:
        def nextNum(num):
            total = 0
            while num:
                total += (num % 10) ** 2 # num % 10 gets last digit
                num = num // 10 # this discards last digit
            return total
        
        hs = set([n])

        while n != 1:
            n = nextNum(n)
            if n in hs:
                return False
            hs.add(n)

        return True