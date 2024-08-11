
class Solution:
    # best
    def permute(self, nums: list[int]) -> list[list[int]]:
        def backtrack(start):
            if start == len(nums):
                res.append(nums.copy())
            
            for i in range(start, len(nums)):
                # swap with start
                nums[start], nums[i] = nums[i], nums[start]
                backtrack(start + 1)
                # swap back to original positions
                nums[start], nums[i] = nums[i], nums[start]

        res = []
        backtrack(0)
        return res

    # faster
    def permute1(self, nums: list[int]) -> list[list[int]]:
        def backtrack(builder: list):
            if len(builder) == len(nums):
                perms.append(builder.copy())

            for i in range(len(nums)):
                if not index_used[i]:
                    index_used[i] = True
                    builder.append(nums[i])
                    backtrack(builder)
                    index_used[i] = False
                    builder.pop()

        perms = []
        index_used = [False] * len(nums)
        backtrack([])
        return perms

    # slower, still more practical for memory safe
    def permute2(self, nums: list[int]) -> list[list[int]]:
        def backtrack(builder):
            if len(builder) == k:
                res.append(builder.copy())
            
            for num in nums:
                if num not in builder:
                    builder.append(num)
                    backtrack(builder)
                    builder.pop()

        res = []
        k = len(nums)
        backtrack([])
        return res
    
# time
    
import time
def time_functions(func1, func2, *args, **kwargs):
    start_time = time.time()
    func1(*args, **kwargs)
    end_time = time.time()
    print(f"Execution time of {func1.__name__}: {end_time - start_time} seconds")

    start_time = time.time()
    func2(*args, **kwargs)
    end_time = time.time()
    print(f"Execution time of {func2.__name__}: {end_time - start_time} seconds")

sol = Solution()
print("Timing:")
time_functions(sol.permute1, sol.permute2, [i for i in range(11)])