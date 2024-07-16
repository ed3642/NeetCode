class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        
        n = len(digits)
        digits[n - 1] += 1
        carry = 0
        for i in range(n - 1, -1, -1):
            _sum = digits[i] + carry
            if _sum > 9:
                carry = 1
                digits[i] = 0
            else:
                digits[i] = _sum
                return digits
        if carry == 1:
            digits.insert(0, 1)
        return digits

    def plusOne(self, digits: list[int]) -> list[int]:
        carry_over = 1
        i = len(digits) - 1

        while carry_over and i >= 0:
            total = digits[i] + carry_over
            carry_over = 0
            if total < 10:
                digits[i] = total
            else:
                digits[i] = total - 10
                carry_over = 1
                i -= 1
        
        if carry_over == 1:
            digits.insert(0, 1)
        return digits
