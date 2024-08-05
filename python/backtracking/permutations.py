
class Solution:
    # faster
    def permute1(self, nums: list[int]) -> list[list[int]]:
        def backtrack(builder):
            if len(builder) == k:
                res.append(builder.copy())
            
            for i in range(0, len(nums)):
                num = nums[i]
                if not used_elems[i]:
                    used_elems[i] = True
                    builder.append(num)
                    backtrack(builder)
                    used_elems[i] = False
                    builder.pop()

        k = len(nums)
        res = []
        used_elems = [False] * len(nums)
        backtrack([])
        return res

    # slower
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