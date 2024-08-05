class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        def nSum(size, res: list[int], builder: list[int], target, start):
            if size < 2 or target < nums[start] * size or target > nums[-1] * size:
                return
            elif size == 2:
                l = start
                r = len(nums) - 1
                while l < r:
                    total = nums[l] + nums[r]
                    if total == target:
                        res.append(builder + [nums[l], nums[r]])
                        l += 1
                        r -= 1
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
                        while l < r and nums[r] == nums[r + 1]:
                            r -= 1
                    elif total < target:
                        l += 1
                    elif total > target:
                        r -= 1
            else:
                for i in range(start, len(nums) - size + 1):
                    if i == start or nums[i] != nums[i - 1]:
                        nSum(size - 1, res, builder + [nums[i]], target - nums[i], i + 1)

        response = []
        nums.sort()
        nSum(size=4, res=response, builder=[], target=target, start=0)

        return response