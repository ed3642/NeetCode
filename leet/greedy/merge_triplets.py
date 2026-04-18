# https://leetcode.com/problems/merge-triplets-to-form-target-triplet/
class Solution:
    def mergeTriplets(self, triplets: list[list[int]], target: list[int]) -> bool:
        
        def is_valid(a, b, c):
            return (
                a <= target[0] and b <= target[1] and c <= target[2]
            )

        curr = [-float('inf'), -float('inf'), -float('inf')]
        for triplet in triplets:
            if is_valid(*triplet):
                curr[0] = max(curr[0], triplet[0])
                curr[1] = max(curr[1], triplet[1])
                curr[2] = max(curr[2], triplet[2])
            if curr == target:
                return True
        
        return False
