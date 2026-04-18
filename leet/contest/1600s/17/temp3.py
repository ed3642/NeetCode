class Solution:
    def countOfPairs(self, nums: list[int]) -> int:
        
        def try_build(min_a):

            def backtrack(i):
                nonlocal count
                if i >= len(nums):  # got to end
                    print('GOT TO END')
                    print(a)
                    print(b)
                    count += 1
                    return

                print(f'Index: {i}, a: {a}, b: {b}, nums: {nums}')

                # Ensure arr1 is non-decreasing and arr2 is non-increasing
                if nums[i] >= a[i - 1] and nums[i] - a[i - 1] <= b[i - 1]:
                    a[i] = nums[i]
                    b[i] = nums[i] - a[i]
                    if a[i] >= a[i - 1] and b[i] <= b[i - 1]:
                        backtrack(i + 1)
                    a[i] = 0  # backtrack
                    b[i] = 0  # backtrack

                if nums[i] <= b[i - 1] and nums[i] - b[i - 1] >= a[i - 1]:
                    b[i] = nums[i]
                    a[i] = nums[i] - b[i]
                    if a[i] >= a[i - 1] and b[i] <= b[i - 1]:
                        backtrack(i + 1)
                    a[i] = 0  # backtrack
                    b[i] = 0  # backtrack

            count = 0
            a = [0] * len(nums)
            b = [0] * len(nums)
            a[0] = min_a
            b[0] = nums[0] - min_a

            backtrack(1)

            return count

        MOD = 10 ** 9 + 7

        min_a = 0
        total = 0

        for min_a in range(nums[0] + 1):
            total += try_build(min_a)

        return total % MOD
    
s = Solution()
print(s.countOfPairs([2, 3, 2]))