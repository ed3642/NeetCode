class Solution:
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
    
s = Solution()

nums = [-4,-1,-1,0,1,2]
nums2 = [-2,0,1,1,2]
nums3 = [-4, -3, -2, -1, -1, 0, 0, 1, 2, 3, 4]
nums4 = [34,55,79,28,46,33,2,48,31,-3,84,71,52,-3,93,15,21,-43,57,-6,86,56,94,74,83,-14,28,-66,46,-49,62,-11,43,65,77,12,47,61,26,1,13,29,55,-82,76,26,15,-29,36,-29,10,-70,69,17,49]

print(s.threeSum(nums4))