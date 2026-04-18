class Solution:
    # NOTE: there is a O(1) space bitmask solution but this is fine
    def singleNumber(self, nums: list[int]) -> list[int]:
        # add to pool of candidates, prune ones that appear twice
        candidates = set()

        for num in nums:
            if num in candidates: # appeares twice, remove it
                candidates.remove(num)
            else:
                candidates.add(num)
        
        return list(candidates)