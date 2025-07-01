# https://leetcode.com/problems/max-difference-you-can-get-from-changing-an-integer/

class Solution:
    def maxDiff(self, num: int) -> int:
        
        num_str = str(num)
        first_non_9 = ''
        first_non_1 = ''
        first_non_0 = ''
        for c in num_str:
            if c != '9':
                first_non_9 = c
                break
        if first_non_9 == '': first_non_9 = '9'
        for c in num_str:
            if c != '1':
                first_non_1 = c
                break
        if first_non_1 == '': first_non_1 = '1'
        for c in num_str[1:]:
            if c != '0' and c != num_str[0]:
                first_non_0 = c
                break
        if first_non_0 == '': first_non_0 = '0'
            
        a = int(''.join(num_str.replace(first_non_9, '9')))
        b_1 = int(''.join(num_str.replace(first_non_1, '1'))) # can change leading number 1-9
        b_2 = int(''.join(num_str.replace(first_non_0, '0'))) # can change first non leading number 0-9

        if len(str(b_2)) < len(num_str) or b_2 == 0:
            return a - b_1
        return max(a - b_1, a - b_2)
