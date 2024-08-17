# https://leetcode.com/problems/alternating-groups-ii/description/
class Solution:
    def numberOfAlternatingGroups(self, colors: list[int], k: int) -> int:
        
        for i in range(k - 1):
            colors.append(colors[i])

        n = len(colors)
        length = 1 if colors[0] != colors[1] else 0
        groups = 0
        for i in range(1, n):
            if colors[i] != colors[i - 1]:
                length += 1
            else:
                length = 1
            if length == k:
                groups += 1
                length -= 1

        return groups
        

s = Solution()
print(s.numberOfAlternatingGroups(colors = [0,1,0,0,1,0,1], k = 6))