from typing import List

class Solution:

    # O(n)
    # should be able to optimize this more with a fenwich product tree since we dont deal with 0s
    def maxProduct1(self, nums: List[int]) -> int:
        
        # processes array without any 0s
        def get_max_product(start, end):
            if start >= end:
                return float('-inf')
            if start == end - 1:
                return nums[start]

            negative_count = 0
            first_neg = -1
            last_neg = -1
            product = 1
            for i in range(start, end):
                product *= nums[i]
                if nums[i] < 0:
                    negative_count += 1
                    if first_neg < 0:
                        first_neg = i
                    last_neg = i

            if negative_count % 2 == 0:
                return product

            # consider taking [start...last negative - 1] [first negative + 1...end] 
            # this excludes one of the odd negatives and checks the biggest arrays possible
            # e.g [-3,-1,-1] -> max([-3,-1], [-1,-1])
            left_prod = 1
            for i in range(start, last_neg):
                left_prod *= nums[i]
            right_prod = 1
            for i in range(first_neg + 1, end):
                right_prod *= nums[i]

            return max(left_prod, right_prod)

        N = len(nums)
        zero_positions = []

        for i in range(N):
            if nums[i] == 0:
                zero_positions.append(i)
        
        best = -float('inf')
        if zero_positions and nums[0] != 0:
            best = max(get_max_product(0, zero_positions[0]), best)

        for i in range(1, len(zero_positions)):
            if zero_positions[i - 1] + 1 == zero_positions[i]:
                continue
            best = max(get_max_product(zero_positions[i - 1] + 1, zero_positions[i]), best)
        
        if not zero_positions:
            best = get_max_product(0, N)
        else:
            best = max(get_max_product(zero_positions[-1] + 1, N), best)
        
        if best > 0:
            return best
        return 0 if len(zero_positions) > 0 else best

    # O(n)
    def maxProduct(self, nums: List[int]) -> int:
        # product kadanes

        max_prod = nums[0]
        min_prod = nums[0]
        global_max_prod = nums[0]

        for num in nums[1:]:
            tentative_max = max_prod * num
            tentative_min = min_prod * num
            max_prod = max(tentative_max, tentative_min, num)
            min_prod = min(tentative_max, tentative_min, num)
            global_max_prod = max(max_prod, global_max_prod)
        
        return global_max_prod
    