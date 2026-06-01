# https://leetcode.com/problems/rotated-digits

class Solution:
    # this could also be done with digit dp but this is good for this project contraints
    def rotatedDigits(self, n: int) -> int:

        def is_valid(num_str):
            required_found = False
            for c in num_str:
                if c not in rotating_nums:
                    return False
                if c in required_nums:
                    required_found = True
            return required_found
        
        rotating_nums = set(['0', '1', '8', '2', '5', '6', '9'])
        required_nums = set(['2', '5', '6', '9'])

        count = 0

        for num in range(1, n + 1):
            num_str = str(num)
            if is_valid(num_str):
                count += 1
        
        return count
