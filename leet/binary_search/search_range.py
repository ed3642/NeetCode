class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        if len(nums) < 1:
            return [-1, -1]

        def binary_search(right_end=False):
            l = 0
            r = len(nums) - 1
            while l < r:
                # this basically makes it so the algorithm is mirrored in a way for each side
                m = (l + r + 1) // 2 if right_end else (l + r) // 2
                if right_end:
                    if nums[m] > target: 
                        r = m - 1
                    else:
                        l = m
                else:
                    if nums[m] < target:
                        l = m + 1
                    else:
                        r = m
            if nums[l] == target: 
                return l
            return -1

        start = binary_search()
        if start == -1:
            return [-1, -1]
        end = binary_search(right_end=True)
        
        return [start, end]