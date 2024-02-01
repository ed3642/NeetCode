class Solution:
    def search(self, nums: list[int], target: int) -> int:
        # min is like the pivot in the rotated array
        def findMin(nums) -> int:
            n = len(nums)
            l = 0
            r = n - 1

            while l <= r:
                mid = (l + r) // 2
                if nums[mid] < nums[r]:
                    r = mid
                else:
                    l = mid + 1
            return l - 1
        
        def binarySearch(l, r) -> int:
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] < target:
                    l = mid + 1
                elif nums[mid] > target:
                    r = mid - 1
                else:
                    return mid
            return -1

        n = len(nums)
        pivot_index = findMin(nums)
        left_side_results = binarySearch(0, pivot_index - 1)
        right_side_results = binarySearch(pivot_index, n - 1)

        return left_side_results if left_side_results != -1 else right_side_results

    def search2(self, nums: list[int], target: int) -> int:
        def binary_search(nums):
            l = 0
            r = len(nums) - 1
            while l <= r:
                m = (l + r) // 2
                if nums[m] < target:
                    l = m + 1
                elif nums[m] > target:
                    r = m - 1
                else:
                    return m
            return -1
        
        # find min in rotated array
        l = 0
        r = len(nums) - 1
        while r - l > 1:
            m = (l + r) // 2
            if nums[m] > nums[r]:
                l = m
            else:
                r = m
        minimum = l if nums[l] < nums[r] else r

        left_side = binary_search(nums[:minimum])
        right_side = binary_search(nums[minimum:])

        return left_side if right_side == -1 else right_side + len(nums[:minimum])
    
    def search3(self, nums: list[int], target: int) -> int:
        def binary_search(nums):
            l = 0
            r = len(nums) - 1
            while l <= r:
                m = (l + r) // 2
                if nums[m] < target:
                    l = m + 1
                elif nums[m] > target:
                    r = m - 1
                else:
                    return m
            return -1
        
        # find min in rotated array
        l = 0
        r = len(nums) - 1
        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        minimum_i = l

        left_side = binary_search(nums[:minimum_i])
        right_side = binary_search(nums[minimum_i:])

        return left_side if right_side == -1 else right_side + len(nums[:minimum_i])