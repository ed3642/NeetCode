class Solution:
    def numberOfPairs(self, nums1: list[int], nums2: list[int], k: int) -> int:
        
        n = len(nums1)
        m = len(nums2)
        res = 0
        for i in range(n):
            num1 = nums1[i]
            for j in range(m):
                num2 = nums2[j]
                if num1 % (num2 * k) == 0:
                    res += 1
        
        return res