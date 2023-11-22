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
