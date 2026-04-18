class Solution:
    # we could also do a next_left, next_right to get the next pointer
    # position depending on the direction but for the given test cases this is faster 
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        
        def two_sum(l, r, target):
            matches = []
            while l < r:
                _sum = nums[l] + nums[r]
                # NOTE: this optimization is correct but it slows it down more than its worth
                # biggest_possible = nums[r] * 2
                # smallest_possible = nums[l] * 2
                # if biggest_possible < target or smallest_possible > target:
                #     return matches

                # slide to different starts and ends
                if _sum < target:
                    l += 1
                elif _sum > target:
                    r -= 1
                else:
                    matches.append([nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    r -= 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1

            return matches

        nums.sort()
        triplets = []
        n = len(nums)
        # [-4,-1,-1,0,1,2]

        i = 0
        while i < n - 2:
            need = -nums[i]
            start = i + 1
            end = n - 1

            found = two_sum(start, end, need)
            if found:
                for match in found:
                    triplets.append([nums[i]] + match)

            # slide i to next distinct start
            i += 1
            while i < n - 2 and nums[i] == nums[i - 1]:
                i += 1
        
        return triplets

    # O(n^2)
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()

        triplets = []
        a = 0
        b = 1
        c = len(nums) - 1

        while nums[a] <= 0 and a < b and b < c:
            while b < c:
                pair_index = self.sortedTwoSum(nums, b, c, -nums[a])
                if pair_index:
                    triplets.append([nums[a], nums[pair_index[0]], nums[pair_index[1]]])
                    b = pair_index[0] + 1
                    c = pair_index[1] - 1
                    if b >= c:
                        break
                else:
                    break

                # slide b
                while b < c and nums[b] == nums[b - 1]:
                    b += 1
                # slide c
                while b < c and nums[c] == nums[c + 1]:
                    c -= 1
            
            # slide a 
            a += 1
            while a < b and nums[a] == nums[a - 1]:
                a += 1
            b = a + 1
            c = len(nums) - 1

        return triplets

    def sortedTwoSum(self, nums, left, right, target) -> list[int]:
        while left < right:
            total = nums[left] + nums[right]
            if total < target:
                left += 1
            elif total > target:
                right -= 1
            else:
                return [left, right]
        return None