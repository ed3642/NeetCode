class Solution:
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


s = Solution()

print(s.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 11))