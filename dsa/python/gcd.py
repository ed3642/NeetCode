class GCD:
    def gcd(self, a, b):
        if a == 0:
            return b

        return self.gcd(b%a, a)