class Solution:
    # nice solution
    def pivotIndex(self, nums: list[int]) -> int:
        left = 0
        right = sum(nums)

        for i, num in enumerate(nums):
            right -= num

            if left == right:
                return i

            left += num
        
        return -1

    def pivotIndex(self, nums: list[int]) -> int:
        
        def gen_prefix_forward(arr, n):
            curr_sum = 0
            res = [0] * (n + 2)
            for i in range(n):
                curr_sum += arr[i]
                res[i + 1] = curr_sum
            return res
        
        def gen_prefix_backward(arr, n):
            curr_sum = 0
            res = [0] * (n + 2)
            for i in range(n - 1, -1, -1):
                curr_sum += arr[i]
                res[i + 1] = curr_sum
            return res

        n = len(nums)
        prefix_sum = gen_prefix_forward(nums, n)
        postfix_sum = gen_prefix_backward(nums, n)

        for i in range(1, n + 1):
            if prefix_sum[i - 1] == postfix_sum[i + 1]:
                return i - 1
        
        return -1