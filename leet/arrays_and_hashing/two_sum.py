class Solution:
    # O()
    # assume: always 1 solution
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        d = dict()

        for i, num in enumerate(nums):
            need = target - num
            if d.get(need) != None:
                return [d[need], i]
            else:
                d[num] = i

s = Solution()

nums1 = [2,7,11,15]
t1 = 9

s.twoSum(nums1, t1)