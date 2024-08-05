class Solution:
    def maxDistance(self, position: list[int], balls: int) -> int:
        
        def can_place(force):
            last_placed = position[0]
            remaining = balls - 1 # we always start with the first one placed already
            for pos in position[1:]:
                if pos - last_placed >= force:
                    last_placed = pos
                    remaining -= 1
                if remaining == 0:
                    return True
            return False
        
        position = sorted(position)
        _min = position[0]
        _max = position[-1]

        l = 1 # min possible force
        r = (_max - _min) + 1 # max possible force

        while l < r:
            m = (l + r) // 2
            if can_place(m):
                l = m + 1
            else:
                r = m
        
        return l - 1
    
s = Solution()
print(s.maxDistance([1,2,3,4,7], 3))