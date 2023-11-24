class Solution:
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
