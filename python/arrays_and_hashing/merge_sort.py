class Solution:
    # merge sort
    def sortArray(self, nums: list[int]) -> list[int]:
        n = len(nums)
        if n <= 1:
            return nums
        pivot = n // 2
        left = self.sortArray(nums[:pivot])
        right = self.sortArray(nums[pivot:])
        return self.merge(left, right)

    def merge(self, l1, l2):
        res = []
        a = 0
        b = 0
        l1.append(float('inf'))
        l2.append(float('inf'))
        while len(res) < len(l1) + len(l2) - 2:
            if l1[a] < l2[b]:
                res.append(l1[a])
                a += 1
            else:
                res.append(l2[b])
                b += 1
        return res
