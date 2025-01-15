# https://leetcode.com/problems/minimize-xor/
class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        
        num_2_bits = bin(num2)[2:]
        num_ones = num_2_bits.count('1')
        num_1_bits = bin(num1)[2:]
        N = len(num_1_bits)
        RES_LEN = 32
        res = ['0'] * RES_LEN

        len_diff = RES_LEN - N

        # cancel out as many ones from the left
        for i in range(N):
            if num_ones > 0 and num_1_bits[i] == '1':
                res_i = i + len_diff
                res[res_i] = '1'
                num_ones -= 1
                if num_ones == 0:
                    break
            
        # cancel out ones from the right with remaining ones
        i = RES_LEN - 1
        while num_ones > 0 and i > 0:
            if res[i] == '0':
                res[i] = '1'
                num_ones -= 1
            i -= 1
    
        return int(''.join(res), 2)
    