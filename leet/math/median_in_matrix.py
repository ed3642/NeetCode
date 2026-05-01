# https://leetcode.com/problems/minimum-operations-to-make-a-uni-value-grid

from typing import List

class Solution:
    
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        # counting sort is a bit better than regular sort here since its worst case is only O(10 ^ 4) for this problem

        def min_ops(target):
            ops = 0
            for num in nums:
                diff = abs(num - target)
                ops += diff // x
            return ops

        N = len(grid)
        M = len(grid[0])
        nums = []
        global_mod = grid[0][0] % x
        max_num = 0
        for i in range(N):
            for j in range(M):
                if grid[i][j] % x != global_mod:
                    return -1
                nums.append(grid[i][j])
                if grid[i][j] > max_num:
                    max_num = grid[i][j]
        count = [0] * (max_num + 1)

        for num in nums:
            count[num] += 1

        n = len(nums)
        mid = n // 2 + 1 # how many nums we need to kick off to get the median
        median = 0

        for num, c in enumerate(count):
            mid -= c
            if mid <= 0:
                median = num
                break

        return min_ops(median)

    def minOperations(self, grid: List[List[int]], x: int) -> int:

        def min_ops(target):
            ops = 0
            for num in nums:
                diff = abs(num - target)
                ops += diff // x
            return ops

        N = len(grid)
        M = len(grid[0])
        nums = []
        global_mod = grid[0][0] % x
        for i in range(N):
            for j in range(M):
                if grid[i][j] % x != global_mod:
                    return -1
                nums.append(grid[i][j])
        nums.sort()

        n = len(nums)
        mid = n // 2

        return min_ops(nums[mid])

    def minOperations(self, grid: List[List[int]], x: int) -> int:
        
        N = len(grid)
        M = len(grid[0])
        nums = [0] * (N * M)

        i = 0
        for row in grid:
            for num in row:
                nums[i] = num
                i += 1
            
        ops = 0
        nums.sort()
        target = nums[(N * M) // 2]
        for i in range(len(nums)):
            diff = abs(nums[i] - target)
            if diff % x != 0:
                return -1
            ops += abs(nums[i] - target) // x
        
        return ops
    
    # TLE, since quickselect is O(n^2) worst case but O(n) average
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        # there is this algo median-of-median that garantees O(n) time for finding the median but its complicated, maybe look into it later
        
        def quickselect(l, r, target_i):
            if l >= r:
                return 
            
            p = partition(l, r)

            if p < target_i:
                quickselect(p + 1, r, target_i)
            elif p > target_i:
                quickselect(l, p - 1, target_i)

        def partition(l, r):
            p = nums[r]
            pi = l # placer index
            for i in range(l, r):
                if nums[i] <= p:
                    nums[i], nums[pi] = nums[pi], nums[i]
                    pi += 1
            nums[r], nums[pi] = nums[pi], nums[r]
            return pi

        def min_ops(target):
            ops = 0
            for num in nums:
                diff = abs(num - target)
                ops += diff // x
            return ops
        
        # [1,2,3,4,5]
        # [1,2,3,4,5,60]

        N = len(grid)
        M = len(grid[0])
        nums = []
        global_mod = grid[0][0] % x
        for i in range(N):
            for j in range(M):
                if grid[i][j] % x != global_mod:
                    return -1
                nums.append(grid[i][j])

        n = len(nums)
        mid = n // 2
        quickselect(0, n - 1, mid) # puts the right number into mid index
        median = nums[mid] 
            
        return min_ops(median)
            