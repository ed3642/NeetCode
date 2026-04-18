import bisect

class Solution:
    # the only diff between bisect_right and left is that 
    # bisect_right checks for <= and left only for <.
    # this is since in bisect_right we want all the elems <= to target to be to the left of insertion_point
    # in bisect left we dont include the elems equal to target to the left of insertion point
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        
        def bisect_right(arr):
            l = 0
            r = len(arr)

            while l < r:
                m = (l + r) // 2
                if arr[m] <= target:
                    l = m + 1
                else:
                    r = m
            return l
        
        def binary_search(arr):
            l = 0
            r = len(arr) - 1
            while l <= r:
                m = (l + r) // 2
                if arr[m] < target:
                    l = m + 1
                elif arr[m] > target:
                    r = m - 1
                else:
                    return True
            return False
        
        col = [matrix[i][0] for i in range(len(matrix))] # first col

        # the built in bisect func also works
        #insertion_i = bisect.bisect_right(col, target)
        insertion_i = bisect_right(col) # we want the insertion point -1
        return binary_search(matrix[insertion_i - 1])

    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        def binary_search(nums, target):
            l = 0
            r = len(nums) - 1

            while l <= r:
                mid = l + (r - l) // 2
                if target < nums[mid]:
                    r = mid - 1
                elif target > nums[mid]:
                    l = mid + 1
                else:
                    return mid
            return -1
        
        def binary_search_closest_biggest(nums, target):
            l = 0
            r = len(nums) - 1
            last_biggest_mid = -1

            while l <= r:
                mid = l + (r - l) // 2
                if target < nums[mid]:
                    r = mid - 1
                elif target > nums[mid]:
                    last_biggest_mid = mid
                    l = mid + 1
                else:
                    return mid
        
            return last_biggest_mid
        
        left_most_column = [row[0] for row in matrix]
        row_candidate_index = binary_search_closest_biggest(left_most_column, target)
        return binary_search(matrix[row_candidate_index], target) != -1

