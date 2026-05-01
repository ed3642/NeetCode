from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        
        xor = 0

        for num in nums:
            xor ^= num
        
        i = 0
        while True:
            if xor & (1 << i):
                # xor has a 1 in this position, this means the xor of the 2 target numbers differs here
                break
            i += 1
        
        # if we group numbers with a 0 and a 1 in this position then we know the target numbers are separated into those groups, since thats a position they differ at

        i_eq_0 = 0
        i_eq_1 = 0
        for num in nums:
            if num & (1 << i) == 0:
                i_eq_0 ^= num
            else:
                i_eq_1 ^= num
        
        return (i_eq_0, i_eq_1)
    
    def singleNumber(self, nums: list[int]) -> list[int]:
        # add to pool of candidates, prune ones that appear twice
        candidates = set()

        for num in nums:
            if num in candidates: # appeares twice, remove it
                candidates.remove(num)
            else:
                candidates.add(num)
        
        return list(candidates)