class Solution:
    def romanToInt(self, s: str) -> int:
        
        symbols = { # letter: (index, value)
            'I': (0, 1),
            'V': (1, 5),
            'X': (2, 10),
            'L': (3, 50),
            'C': (4, 100),
            'D': (5, 500),
            'M': (6, 1000),
        }

        last_letter_i = float('inf')
        last_val = 0
        base_10 = 0
        for token in s:
            curr_i, curr_val = symbols[token]
            if curr_i > last_letter_i:
                base_10 += curr_val - (2 * last_val)
            else:
                base_10 += curr_val
            last_val = curr_val
            last_letter_i = curr_i
        
        return base_10