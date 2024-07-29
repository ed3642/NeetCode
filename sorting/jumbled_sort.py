# https://leetcode.com/problems/sort-the-jumbled-numbers
class Solution:
    def sortJumbled(self, mapping: list[int], nums: list[int]) -> list[int]:
        
        def mapping_func(num):
            if num == 0: # edge case where num to map is 0
                return mapping[0]
            mapped_num = 0
            mult = 1
            while num > 0:
                digit = mapping[num % 10] # mapped digit
                num //= 10
                mapped_num += digit * mult
                mult *= 10
            return mapped_num
        
        # need to preform a stable sort algorithm
        # pythons sorted, method is stable
        return list(sorted(nums, key=mapping_func))
