class Solution:

    # nice solution
    def increasingTriplet(self, nums: list[int]) -> bool:
        # keep track of the smallest, and second smallest found so far
        smallest = second_smallest = float('inf')
        for num in nums:
            if num <= smallest:
                smallest = num
            elif num <= second_smallest:
                second_smallest = num
            else:
                return True
        return False

    def increasingTriplet2(self, nums: list[int]) -> bool:
        # [1,5,0,4,1,3]
        # [1,1,0,0,0,0] # min from left
        # [5,5,4,4,3,3] # max from right
        # there should be a num that is between them and in index [1,n-2]

        n = len(nums)
        if n < 3:
            return False
        
        min_from_left = [float('inf')] * n
        max_from_right = [-float('inf')] * n
        curr_min = float('inf')
        curr_max = -float('inf')

        for i in range(n):
            i_reflection = (i * -1) + n - 1
            curr_min = min(curr_min, nums[i])
            min_from_left[i] = curr_min
            curr_max = max(curr_max, nums[i_reflection])
            max_from_right[i_reflection] = curr_max
        
        for i in range(1, n - 1):
            if min_from_left[i - 1] < nums[i] < max_from_right[i + 1]:
                return True

        return False