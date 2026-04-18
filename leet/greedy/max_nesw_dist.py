# https://leetcode.com/problems/maximum-manhattan-distance-after-k-changes

class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        
        # try maximizing each of the 4 possible directions
        # NE, NW, SE, SW
        
        def check_direction(directions, actions):
            dist = 0
            max_dist = 0
            
            for c in s:
                if c not in directions:
                    if actions > 0:
                        actions -= 1
                        dist += 1
                    else:
                        dist -= 1
                else:
                    dist += 1
                max_dist = max(dist, max_dist)

            return max_dist

        max_dist = 0
        max_dist = max(check_direction('NE', k), max_dist)
        max_dist = max(check_direction('NW', k), max_dist)
        max_dist = max(check_direction('SE', k), max_dist)
        max_dist = max(check_direction('SW', k), max_dist)

        return max_dist
