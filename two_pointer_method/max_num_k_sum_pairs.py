from collections import defaultdict

class Solution:
    def maxOperations(self, nums: list[int], k: int) -> int:
        l = 0
        r = len(nums) - 1
        num_operations = 0

        nums.sort()

        while l < r:
            need = k - nums[r]

            if nums[l] == need:
                num_operations += 1
                l += 1
                r -= 1
            else:
                if nums[l] <= need:
                    l += 1
                else:
                    r -= 1
            
        return num_operations

    def maxOperations2(self, nums: list[int], k: int) -> int:
        nums.sort()
        nums_dict = defaultdict(int)
        num_operations = 0

        for num in nums:
            nums_dict[num] += 1

        for num in nums:
            need = k - num
            if need in nums_dict and num in nums_dict:
                if num == need and nums_dict[need] < 2:
                    continue
                if nums_dict[need] == 1:
                    del nums_dict[need]
                else:
                    nums_dict[need] -= 1
                if nums_dict[num] == 1:
                    del nums_dict[num]
                else:
                    nums_dict[num] -= 1
                num_operations += 1
        
        return num_operations